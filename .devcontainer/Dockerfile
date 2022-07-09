FROM fedora:36

WORKDIR /home

RUN dnf -y update && \
  dnf -y install gcc gcc-g++ nano wget


RUN useradd -m -G wheel ruby
# Change to non-root privilege
USER ruby