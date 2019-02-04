import os
import sys
import time

def in_mins(time_):
    time_ = time_.split(':')
    mins = int(time_[0]) * 60 + int(time_[1])
    return mins

def as_time(mins):
    # Rjust, min 2 spaces, replace gaps with '0'
    hrs = str(int(mins / 60)).rjust(2, '0')
    mins = str(int(mins % 60)).rjust(2, '0')
    return("%s:%s" %(hrs, mins))

# User using Mac, Win or unsupported
if os.sys.platform == 'darwin':
    hosts_path = r'/etc/hosts'
elif os.sys.platform == 'win32':
    hosts_path = r'C:\Windows\System32\drivers\etc\host'
else:
    print("%s not yet supported, sorry.\nExiting now" %user_sys)
    sys.exit(0)

# Read users host file to store it's contents before anything else
with open(hosts_path, "r") as hosts:
    original_hosts = hosts.read()

print("Running...")

redirect = "127.0.0.1"
block_list = ["www.facebook.com", "facebook.com", "wwww.youtube.com", "youtube.com"]

# Check if user wants to restore file
if

# Create a copy of hosts file and append sites to block
block_hosts = original_hosts
for u in block_list:
    if u not in original_hosts:
        block_hosts += ("\n%s\t%s" %(redirect, u))


start_mins = in_mins(time.strftime("%H:%M")) + 1
end_mins = in_mins(time.strftime("%H:%M")) + 2

blocking = False 

while True:

    time.sleep(3)
    time_now = in_mins(time.strftime("%H:%M"))

    if time_now in range(start_mins, end_mins) and not blocking:
        with open(hosts_path, "w") as hosts:
            hosts.write(block_hosts)
        blocking = True
        print("\nBlocking:\n")
        for u in block_list:
            print("\t%s" %u)
        print("\nUntil %s" %as_time(end_mins))

    elif time_now not in range(start_mins, end_mins) and blocking:
        with open(hosts_path, "w") as hosts:
            hosts.write(original_hosts)
        blocking = False
        print("\n\nBlocking disabled")
        print("Web access unrestricted until %s" %as_time(start_mins))
