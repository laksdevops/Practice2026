import subprocess


class Server:

    def __init__(self, hostname):
        self.hostname = hostname

    def install_nginx(self):
        print("Installing Nginx...")
        subprocess.run(
            ["sudo", "dnf", "install", "-y", "nginx"],
            check=True
        )

    def start_nginx(self):
        print("Starting Nginx...")
        subprocess.run(
            ["sudo", "systemctl", "enable", "--now", "nginx"],
            check=True
        )

    def check_nginx(self):
        result = subprocess.run(
            ["systemctl", "is-active", "nginx"],
            capture_output=True,
"yuminst.py" 37L, 797B