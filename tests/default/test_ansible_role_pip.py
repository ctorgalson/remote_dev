import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


''' ansible-role-pip (geerlingguy.pip) tests. '''


@pytest.mark.parametrize('package', [
    'ansible',
    'ansible-lint',
    'docker',
    'flake8',
    'molecule',
    'testinfra',
    'yamllint',
])
def test_pip_packages(host, package):
    p = host.pip_package.get_packages(pip_path='/usr/bin/pip3')

    assert package in p
