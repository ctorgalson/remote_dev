import os

import testinfra.utils.ansible_runner

import pytest

import re


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-nvm (ctorgalson.nvm) tests. """


@pytest.mark.parametrize('path', [
  '/home/molecule/.nvm/nvm.sh',
])
def test_manually_installed_packages(host, path):
    f = host.file(path)

    assert f.exists
