#!/usr/bin/env bash

dnf update
dnf install @development-tools \
  git curl wget
