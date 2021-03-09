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
