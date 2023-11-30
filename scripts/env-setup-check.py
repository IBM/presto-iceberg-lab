import argparse
import os
import pandas
import paramiko

REPO_NAME = "presto-iceberg-lab"

ENV_CSV_FILE = "workshop.csv"
PEM_FILE_NAME = "private.pem"


def parse_row(row):
    return row["Username"], row["Public IP"], row["SSH Port"], row["Download SSH key"]  


def get_key(pem_contents):
    # write key contents to file
    with open(PEM_FILE_NAME, 'w') as file:
        file.write(pem_contents)

    key = paramiko.RSAKey.from_private_key_file(PEM_FILE_NAME)

    # remove created key file
    os.remove(PEM_FILE_NAME)

    return key


def clone_repo(ssh, ws=""):
    print(f"{ws}Cloning repository '{REPO_NAME}' docker...")
    ssh.exec_command("ssh-keyscan github.com >> ~/.ssh/known_hosts")
    ssh_stdin, ssh_stdout, _ = ssh.exec_command(f"git clone https://github.com/IBM/{REPO_NAME}.git")
    
    exit_status = ssh_stdout.channel.recv_exit_status()  # blocking
    if exit_status == 0:
        print(f"\t{ws}Repository cloned")
    else:
        print(f"\t{ws}Error {exit_status}")
        ssh_stdin.close()
        return 1
    
    ssh.exec_command(f"chmod +x {REPO_NAME}/scripts/*.sh")
    
    ssh_stdin.close()
    return 0


def install_docker(ssh, ws=""):
    print(f"{ws}Installing docker...")
    ssh_stdin, ssh_stdout, _ = ssh.exec_command(f"./{REPO_NAME}/scripts/docker-install.sh")

    exit_status = ssh_stdout.channel.recv_exit_status()  # blocking
    if exit_status == 0:
        print(f"\t{ws}Docker installed")
    else:
        print(f"\t{ws}Error {exit_status}")
        ssh_stdin.close()
        return 1

    ssh_stdin.close()
    return 0


def pull_images(ssh, ws=""):
    print(f"{ws}Starting pull of docker images in background...")
    ssh.exec_command("mkdir logs")
    ssh.exec_command(f"nohup ./{REPO_NAME}/scripts/docker-images.sh > logs/docker-images.out 2> logs/docker-images.err &")


def set_up():
    df = pandas.read_csv(ENV_CSV_FILE, index_col="Env Num")
    for i, row in df.iterrows():
        # for testing env 1 only
        if i != 1:
            continue

        print(f"-------------------- Setting up env {i} --------------------")

        username, public_ip, port, pem_contents = parse_row(row)
        key = get_key(pem_contents)

        print(f"Connecting to host {public_ip}...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=public_ip, username=username, pkey=key, port=port)

        # clone repo
        error = clone_repo(ssh)
        if error:
            ssh.close()
            continue

        # install docker
        error = install_docker(ssh)
        if error:
            ssh.close()
            continue

        # close connection and log back in for docker installation to take effect
        ssh.close()
        ssh.connect(hostname=public_ip, username=username, pkey=key, port=port)

        # pull images in background
        pull_images(ssh)
        ssh.close()

        print("")


def check():
    df = pandas.read_csv(ENV_CSV_FILE, index_col="Env Num")
    for i, row in df.iterrows():
        # for testing env 1 only
        if i != 1:
            continue

        print(f"-------------------- Checking env {i} --------------------")

        username, public_ip, port, pem_contents = parse_row(row)
        key = get_key(pem_contents)

        print(f"Connecting to host {public_ip}...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=public_ip, username=username, pkey=key, port=port)

        print(f"Checking that repository is cloned...")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls ~")
        if REPO_NAME not in ssh_stdout.read().decode('ascii'):
            print("\tRepository not present in home directory")
            ssh_stdin.close()

            # try again
            error = clone_repo(ssh, "\t")
            if error:
                ssh.close()
                continue

        if ssh_stderr.read():
            print("\tError checking for repository")
            ssh_stdin.close()
            ssh.close()
            continue

        ssh_stdin.close()

        print("Checking that docker is installed...")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"which docker")
        cmd_output = ssh_stdout.read().decode('ascii')
        if "not found" in cmd_output or not cmd_output:
            print("\tDocker not installed")
            ssh_stdin.close()

            # try again
            error = install_docker(ssh, "\t")
            if error:
                ssh.close()
                continue

        if ssh_stderr.read():
            print("\tError checking for docker")
            ssh_stdin.close()
            ssh.close()
            continue
        
        ssh_stdin.close()

        print("Checking that docker images have been built/pulled...")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"docker image list")
        images = ["conf-hive-metastore", "prestodb/presto", "minio/minio", "mysql"]
        cmd_output = ssh_stdout.read().decode('ascii')
        image_missing = False
        for image in images:
            if image not in cmd_output:
                image_missing = True
                print(f"\tImage '{image}' not installed")

        if image_missing:
            # try again
            pull_images(ssh, "\t")

        if ssh_stderr.read():
            print("\tError checking docker images")
            ssh_stdin.close()
            ssh.close()
            continue
        
        ssh_stdin.close()
        ssh.close()
        
        print("")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help='setup or check')
    args = parser.parse_args()

    if args.mode == "setup":
        set_up()
    elif args.mode == "check":
        check()
    else:
        print(f"Invalid selection '{args.name}'")


if __name__ == '__main__':
    main()
