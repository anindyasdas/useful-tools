-- To view results while running (accesible from local machine only)
```
tensorboard --logdir <dir_name>
```
E.g.,
```
tensorboard --host 0.0.0.0 --logdir tb_logs/ --port 6005
```
-- When running in remote server use --host 0.0.0.0  to make the remote server accesible through ip adress
```
tensorboard --host 0.0.0.0 --logdir tb_logs/ --port 6005
```


