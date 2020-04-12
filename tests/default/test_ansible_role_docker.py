import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-docker (geerlingguy.docker) tests. """


@pytest.mark.parametrize('package,version', [
    ('docker', 'Docker version 19'),
])
def test_docker(host, package, version):
    c = '{} --version'.format(package)
    r = host.run(c)

    assert version in r.stdout
