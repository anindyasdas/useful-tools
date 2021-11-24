## KILL the Server running locally at any port(8080,9000,8000,9999)
- list the processes running at the port 9997
```
lsof -i:9997
```

Output:
```
COMMAND   PID          USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python  29708 anindya06.das    4u  IPv4 613531      0t0  TCP *:9997 (LISTEN)
```

- to kill forcefully (-9) a process with PID (29708 in this case)
```
kill -9 29708
```
- Netstat is results from network and statistics. It shows open ports on the host device and their corresponding addresses, the routing table, and masquerade connections.
```
netstat -n
```
- Find the Process id of the Process Using the Given Port (WINDOWS)
```
netstat -aon | findstr <port_number>
```
- Find the Process/Application Name Using the Given Port Using the Process id Found in Previous Step (WINDOWS)
```
tasklist | findstr <process_id>
```
- Find the Process id of the Process Using a Process With the Given Name (WINDOWS)
```
tasklist | findstr <application_name/process_name>
```
- Find the Port Being Used by the Process id Found in Prev step (WINDOWS)
```
netstat -aon | findstr 9260
```
