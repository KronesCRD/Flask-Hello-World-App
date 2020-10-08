# Flask-Hello-World-App
Simple "Hello World" app written in Python using the Flask framework.

#### Two Dockerfiles for different architectures:
+ arm32v7.Dockerfile: suitable for Docker builds on Raspberry Pi
+ amd64.Dockerfile: suitable for most modern devices

User "-f" option in for docker build to specify the Dockerfile to be used:
```shell
build -t registry/repo:tag -f amd64.Dockerfile .
```
or
```shell
build -t registry/repo:tag -f arm32v7.Dockerfile .
```