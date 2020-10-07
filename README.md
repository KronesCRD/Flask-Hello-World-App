# Flask-Hello-World-App
Simple "Hello World" app written in Python using the Flask framework.

  #### Two Dockerfiles for different architectures
  + arm32v7.Dockerfile: suitable for Docker builds on Raspberry Pi
  + amd64.Dockerfile: suitable for Docker builds on 64-bit systems

  User "-f" option in for docker build to specify the Dockerfile to be used:
  e.g.: docker build -t *docker registry/repo:tag* -f *Dockerfile* *build context* 