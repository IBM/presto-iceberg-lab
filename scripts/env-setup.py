import os
import pandas
import paramiko

REPO_NAME = "presto-iceberg-lab"

ENV_CSV_FILE = "workshop.csv"
PEM_FILE_NAME = "private.pem"

df = pandas.read_csv(ENV_CSV_FILE, index_col="Env Num")
for i, row in df.iterrows():
    # for testing env 1 only
    if i != 1:
        continue

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

    # clone github repo and wait until complete
    print(F"Cloning repository '{REPO_NAME}' docker...")
    ssh.exec_command("ssh-keyscan github.com >> ~/.ssh/known_hosts")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"git clone https://github.com/IBM/{REPO_NAME}.git")
    exit_status = ssh_stdout.channel.recv_exit_status()  # blocking
    if exit_status == 0:
        print(f"\tRepository cloned")
    else:
        print("\tError ", exit_status)
    
    ssh_stdin.close()

    ssh.exec_command(f"chmod +x {REPO_NAME}/scripts/*.sh")

    # install docker and wait until complete
    print("Installing docker...")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"./{REPO_NAME}/scripts/docker-install.sh")
    exit_status = ssh_stdout.channel.recv_exit_status()  # blocking
    if exit_status == 0:
        print("\tDocker installed")
    else:
        print("\tError ", exit_status)
        print(ssh_stderr)
        break

    ssh_stdin.close()

    # close connection and log back in for docker installation to take effect
    ssh.close()
    ssh.connect(hostname=public_ip, username=username, pkey=key, port=port)

    print("Starting pull of docker images in background...")
    ssh.exec_command("mkdir logs")
    ssh.exec_command(f"nohup ./{REPO_NAME}/scripts/docker-images.sh > logs/docker-images.out 2> logs/docker-images.err &")

    ssh.close()









