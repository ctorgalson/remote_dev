import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-apt (ctorgalson.apt) tests. """


@pytest.mark.parametrize('package', [
    'byobu',
    'git',
    'htop',
    'httpie',
    'mosh',
    'neofetch',
    'openssh-server',
    'silversearcher-ag',
    'unzip',
    'vim',
    'zsh',
])
def test_packages(host, package):
    p = host.package(package)

    assert p.is_installed
