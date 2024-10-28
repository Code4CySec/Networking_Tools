# Networking Tools

# Python networking tools to help out when dealing with an environment where there are no tools installed.
# Here you will find several tools written in Python to help your asessment.

Tools:

#tcp_client.py
  
#Ecample Usage

./tcp_client.py 
  
#udp_client.py
  
#Example Usage

./udp_client.py

#netcat.py

#Example Usage

./netcat.py --help

python netcat.py -t 192.168.1.12 -p 4444 -l -c

python netcat.py -t 192.16.1.12 -p 4444 -l -e="cat /etc/passwd"

#proxy.py

#Example Usage

sudo python proxy.py 1902.168.1.12 21 ftp.sun.ca.za True

#Open a new Terminal an enter:

ftp 127.16.1.12:21

#ssh_cmd.py

#Example Usage

#First make sure to install 'paramiko'

pip install paramiko

pytho ssh_cmd.py

#ssh_rcmd.py

#Example Usage

#This script is modified to run commands on a remote Windows machine

#You'll need to ssh_server.py on your host

#ssh_server.py

#Example usage:

#Run the script on your host

python ssh_server.py

#Now run on the WIndows target host

python ssh_rcmd.py

#This will connact back to the server running on your Kali machine

#rforward.py

#Example usage

#SSh Tunneling Tool

#From the Windows machine launch the script to be the middle man to tunnel traffic from a web serveer to your Kali machine

python rforward.py 192.168.1.12 -p 8081 192.16.1.13:3000 --user=hacker
