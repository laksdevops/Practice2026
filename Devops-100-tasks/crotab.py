import paramiko


class Server:

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.__password = password
        self.ssh = None

    # --------------------------------------------------
    # Connect to remote server
    # --------------------------------------------------
    def connect(self):

        self.ssh = paramiko.SSHClient()

        self.ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )

        self.ssh.connect(
            hostname=self.hostname,
            username=self.username,
            password=self.__password
        )

        print(f"\nConnected to {self.hostname}")

    # --------------------------------------------------
    # Run a sudo command
    # --------------------------------------------------
    def run_sudo_command(self, command):

        sudo_command = f"sudo -S -p '' {command}"

        stdin, stdout, stderr = self.ssh.exec_command(
            sudo_command,
            get_pty=True
        )

        # Send sudo password
        stdin.write(self.__password + "\n")
        stdin.flush()

        # Read command output
        output = stdout.read().decode()

        # Read error output
        error = stderr.read().decode()

        # Get command exit status
        exit_code = stdout.channel.recv_exit_status()

        return output, error, exit_code

    # --------------------------------------------------
    # Install Cronie
    # --------------------------------------------------
    def install_cronie(self):

        print("Installing cronie...")

        output, error, exit_code = self.run_sudo_command(
            "dnf install -y cronie"
        )

        if output:
            print(output)

        if error:
            print(error)

        if exit_code == 0:
            print("Cronie installation successful")
        else:
            print("Cronie installation failed")

    # --------------------------------------------------
    # Start and enable crond
    # --------------------------------------------------
    def start_crond(self):

        print("Starting crond...")

        output, error, exit_code = self.run_sudo_command(
            "systemctl enable --now crond"
        )

        if output:
            print(output)

        if error:
            print(error)

        if exit_code == 0:
            print("crond started successfully")
        else:
            print("Failed to start crond")

    # --------------------------------------------------
    # Add root cron job
    # --------------------------------------------------
    def add_cron_job(self):

        print("Adding root cron job...")

        cron_job = "*/5 * * * * echo hello > /tmp/cron_text"

        command = (
            f"sh -c 'echo \"{cron_job}\" | crontab -'"
        )

        output, error, exit_code = self.run_sudo_command(command)

        if output:
            print(output)

        if error:
            print(error)

        if exit_code == 0:
            print("Cron job added successfully")
        else:
            print("Failed to add cron job")

    # --------------------------------------------------
    # Close SSH connection
    # --------------------------------------------------
    def close(self):

        if self.ssh:
            self.ssh.close()

        print(f"SSH connection closed for {self.hostname}")


# ======================================================
# Create Server objects
# ======================================================

server1 = Server(
    "stapp01",
    "tony",
    "Ir0nM@n"
)

server2 = Server(
    "stapp02",
    "steve",
    "Am3ric@"
)

server3 = Server(
    "stapp03",
    "banner",
    "BigGr33n"
)


# ======================================================
# Store all servers in a list
# ======================================================

servers = [
    server1,
    server2,
    server3
]


# ======================================================
# Execute automation on all servers
# ======================================================

for server in servers:

    try:
        server.connect()

        server.install_cronie()

        server.start_crond()

        server.add_cron_job()

    except Exception as e:

        print(f"Error on {server.hostname}: {e}")

    finally:

        server.close()