#!/usr/bin/env bash

python3 -m pip install -U pip

python3 -m pip install --pre \
  "ansible-lint" \
  "flake8" \
  "molecule-ansible" \
  "molecule-docker" \
  "testinfra" \
  "yamllint"
