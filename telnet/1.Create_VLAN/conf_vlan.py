import getpass
import telnetlib

# Get credentials from user input
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open(input("Enter filename of switches list: "))

# Loop through list of switches from a file
for LINE in f:
    IP = LINE.strip()
    print("Configuring Switch", IP)
    HOST = IP
    tn = telnetlib.Telnet(HOST)

    # Passing the credentials when prompted by IOS
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    # Passing the configuration
    tn.write(b"conf t\n")
    tn.write(b"vlan 2\n")
    tn.write(b"name HR_VLAN\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name IT_VLAN\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name VOICE_VLAN\n")
    tn.write(b"exit\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))