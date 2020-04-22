import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-apt (ctorgalson.apt) tests. """


@pytest.mark.parametrize('package', [
    'byobu',
    'curl',
    'git',
    'git-extras',
    'htop',
    'httpie',
    'mosh',
    'neofetch',
    'openssh-server',
    'pv',
    'silversearcher-ag',
    'unzip',
    'vim',
    'zsh',
])
def test_packages(host, package):
    p = host.package(package)

    assert p.is_installed
