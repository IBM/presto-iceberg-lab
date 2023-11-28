import os
import pandas
import paramiko

REPO_NAME = "presto-iceberg-lab"

ENV_CSV_FILE = "workshop.csv"
PEM_FILE_NAME = "private.pem"
INSTALL_SCRIPT = "docker-install.sh"
PULL_SCRIPT = "docker-images.sh"
REPO_LINK = f"https://github.com/IBM/{REPO_NAME}.git"

df = pandas.read_csv(ENV_CSV_FILE, index_col="Env Num")
for i, row in df.iterrows():
    print(f"-------------------- Setting up env {i} --------------------")

    username = row["Username"]
    public_ip = row["Public IP"]
    port = row["SSH Port"]
    pem_contents = row["Download SSH key"]

    # write key contents to file
    with open(PEM_FILE_NAME, 'w') as file:
        file.write(pem_contents)

    print(f"Connecting to host {public_ip}...")
    ssh = paramiko.SSHClient()
    key = paramiko.RSAKey.from_private_key_file(PEM_FILE_NAME)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=public_ip, username=username, pkey=key, port=port)

    # remove created key file
    os.remove(PEM_FILE_NAME)

    print("Transferring local scripts...")
    ftp_client = ssh.open_sftp()
    ftp_client.put(INSTALL_SCRIPT, INSTALL_SCRIPT)
    ftp_client.put(PULL_SCRIPT, PULL_SCRIPT)
    ftp_client.close()
    # change script permissions
    ssh.exec_command("chmod +x *.sh")

    # clone github repo
    ssh.exec_command("ssh-keyscan github.com >> ~/.ssh/known_hosts")
    ssh.exec_command(f"git clone {REPO_LINK}")

    # install docker and wait until complete
    print("Installing docker...")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"./{INSTALL_SCRIPT}")
    exit_status = ssh_stdout.channel.recv_exit_status()  # blocking
    if exit_status == 0:
        print("\tDocker installed")
    else:
        print("\tError ", exit_status)

    # close connection and log back in for docker installation to take effect
    ssh.close()
    ssh.connect(hostname=public_ip, username=username, pkey=key, port=port)

    # pull docker images and wait until complete
    print("Pulling docker images...")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"./{PULL_SCRIPT}")
    exit_status = ssh_stdout.channel.recv_exit_status()  # blocking
    if exit_status == 0:
        print("\tDocker images pulled")
    else:
        print("\tError ", exit_status)

    ssh.close()

    break










