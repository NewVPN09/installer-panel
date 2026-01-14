VPS Script Installer Panel - Instructions

1. Upload this folder to your web server.

2. Install Python dependencies:
   apt update
   apt install python3-pip -y
   pip3 install flask paramiko

3. Run the backend:
   python3 app.py

4. Access the panel in your browser:
   http://YOUR_SERVER_IP/index.html

5. Fill your VPS IP, Port, Username, Password
   Click "Install Script"
   The script will run on your VPS one time
