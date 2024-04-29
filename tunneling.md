# 1. To establish a Tunnel from a local machine to a jupyter server installed on a conda environment in a remote machine
- Activate Conda environment
  
  ``` conda activate env_name ```

- start jupyter server on a remote machine

   ```jupyter lab --no-browser --port=8888```
- If using a slurm cluster, of a gpu node, use ```-ip``` flag

  ```jupyter lab --no-browser --ip=0.0.0.0 --port=9999```
- ssh from local to remote

  ```ssh -L 9998:localhost:8889 user_id@remote_ip```
- or if you are using ```-ip``` flag

  ```ssh -L 9998:node_name:8889 user_id@remote_ip```
