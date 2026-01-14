from flask import Flask, request, send_from_directory
import paramiko

app = Flask(__name__)

# Serve the HTML panel at root
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

# Existing install route
@app.route("/install", methods=["POST"])
def install():
    d = request.json
    ip = d["ip"]
    port = int(d["port"])
    user = d["user"]
    password = d["password"]

    cmd = """
    curl -skLO -H "Accept: application/vnd.github.v3.raw" \
    "https://raw.githubusercontent.com/NewVPNPro/ErwanVPN/main/installer.sh" && \
    chmod +x installer.sh && \
    bash installer.sh
    """

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=user, password=password, timeout=10)

        stdin, stdout, stderr = ssh.exec_command(cmd)
        output = stdout.read().decode() + stderr.read().decode()
        ssh.close()

        return f"<pre>{output}</pre>"

    except Exception as e:
        return f"<pre>Error: {e}</pre>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
