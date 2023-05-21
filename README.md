# udacity-workspace
Replicate Udacity workspaces on a local machine.

## Common environment variables
You can set the environment variable in the `.env` file in the project root directory. There are the following common variables. If the projects may have a special variable, the `README.md` at the project root directory explains the variable.

### GPU_DEVICES
This variable sets the GPU ID to be used inside the container.
```
GPU_DEVICES=1
```
```
GPU_DEVICES=0,1
```

### JUPYTER_TOKEN
This variable sets the security token to access the JupyterLab server.
```
JUPYTER_TOKEN=letmein
```
You need to specify the token when you connect to the server.
```
http://localhost?token=letmein
```

### JUPYTER_PORT
You need to specify the port number of the JupyterLab server.
```
JUPYTER_PORT=8888
```
You need to specify the token when you connect to the server.
```
http://localhost:8888
```

### TENSORBOARD_PORT
You need to specify the port number of the TensorBoard.
```
TENSORBOARD_PORT=6006
```
You need to specify the token when you connect to the TensorBoard.
```
http://localhost:6006
```
