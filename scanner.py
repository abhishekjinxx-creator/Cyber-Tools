import socket

target = "scanme.nmap.org"

# This 'for loop' tells Python to try every number from 75 up to 85
for port in range(75, 86):
    s = socket.socket()
    s.settimeout(1) # Don't wait forever! Wait 1 second per door.
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN!")
    else:
        print(f"Port {port} is closed.")
    
    s.close()
