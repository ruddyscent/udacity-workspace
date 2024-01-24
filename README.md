# udacity-workspace
Replicate Udacity workspaces on a local machine.

## Programs
 * [nd0013-kr](https://github.com/ruddyscent/udacity-workspace/tree/main/nd0013-kr): 자율주행차 엔지니어
 * [nd0013](https://github.com/ruddyscent/udacity-workspace/tree/main/nd0013): Self Driving Car Engineer
 * [nd013](https://github.com/ruddyscent/udacity-workspace/tree/main/nd013): Self-Driving Car Engineer
 * [nd027](https://github.com/ruddyscent/udacity-workspace/tree/main/nd027): Data Engineering with AWS
 * [nd089](https://github.com/ruddyscent/udacity-workspace/tree/main/nd089): AI Programming with Python
 * [nd101](https://github.com/ruddyscent/udacity-workspace/tree/main/nd101): Deep Learning
 * [nd213](https://github.com/ruddyscent/udacity-workspace/tree/main/nd213): C++
 * [nd892](https://github.com/ruddyscent/udacity-workspace/tree/main/nd892): Natural Language Processing
 * [ud210](https://github.com/ruddyscent/udacity-workspace/tree/main/ud210): C++ For Programmers
 * [ud595](https://github.com/ruddyscent/udacity-workspace/tree/main/ud595): Linux Command Line Basics
 * [ud810](https://github.com/ruddyscent/udacity-workspace/tree/main/ud810): Introduction to Computer Vision
 * [cd1822](https://github.com/ruddyscent/udacity-workspace/tree/main/cd1822): RNNs and Transformers
   
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
