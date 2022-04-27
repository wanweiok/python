# Drive letter: L
# Shared drive path: \\sshfs\root@cmx50070-101689\..\..
# Username: username
# Password: password
import subprocess

def del_disk_mapping_and_map_cmx_to_disk(cmx_name: str, disk: str, username: str, password: str):
    # Disconnect anything on disk
    remove_com = r"net use " + disk + r": /del"
    subprocess.call(remove_com, shell=True)
    # print(remove_com + " is "+ ("Succes" if (res == 0) else "Failed"))

    cmx_pos = r"\\sshfs\root@"+cmx_name+r"\..\.."
    # Connect to shared drive, use drive letter disk
    map_com = r"net use " + disk + r": " + cmx_pos + r" /user:" + username + " " + password
    subprocess.call(map_com, shell=True)
    # print(map_com + " is " + ("Succes" if (res == 0) else "Failed"))

