import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-composer (geerlingguy.composer) tests. """


@pytest.mark.parametrize('version', [
  'Composer version 2',
])
def test_composer_packages(host, version):
    c = 'composer --version'
    r = host.run(c)

    assert version in r.stdout
