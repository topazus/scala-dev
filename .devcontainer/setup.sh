#!/usr/bin/env bash

dnf update
dnf install -y git curl wget tree cmake llvm clang

echo 'alias gc1="git clone --depth 1"' >> /home/ruby/.bashrc \
  && source /home/ruby/.bashrc