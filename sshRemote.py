from pathlib import Path
from paramiko.client import AutoAddPolicy, SSHClient
from scp import SCPClient

def cmx_scp(instrument_hostname: str, src: str, dst: Path):
    # Default credentials for CMX
    username = "root"
    pwd = "temp"

    try:
        with SSHClient() as ssh:

            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(instrument_hostname, username=username, password=pwd)

            stdin, stdout, stderr = ssh.exec_command("df -h")
            print(stdout.read().decode('utf-8'))

            with SCPClient(ssh.get_transport()) as scp:
                scp.get(remote_path=str(src), local_path=str(dst))

            ssh.close()

    except Exception as error_:  # pylint: disable=broad-except
        print("Copy log exception: %s, %s", error_, src)


if __name__ == '__main__':
  src = r"/home/instrument/fw/log/2022-04-27_10-24-54/sfa/NetworkEmulation32/signaling.msglog"
  dest = Path(r"C:\Users\wan_f\Desktop\tem\New folder")
  cmx_scp("cmx50070-101689", src, dest)
