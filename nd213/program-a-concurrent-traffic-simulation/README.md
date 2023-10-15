# Program a Concurrent Traffic Simulation

In the .env file, set the value of the environment variable, DISPLAY:
```shell
DISPLAY=[IP ADDRESS]:0
```
or set the environment variable on the shell:
```shell
$ export DISPLAY=[IP ADDRESS]:0
```
[IP ADDRESS] is the Internet IP address of the computer where the app will be displayed. On a Mac, this IP address can be found with the command:
```shell
$ ipconfig getifaddr en0
```

## FAQ
# gdb failure on M1 mac.
Run arm64 containers on M1 hardware.
https://github.com/docker/for-mac/issues/5191#issuecomment-834154431
