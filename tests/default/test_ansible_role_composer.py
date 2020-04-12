import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-composer (geerlingguy.composer) tests. """


@pytest.mark.parametrize('package', [
  'hirak/prestissimo',
])
def test_composer_packages(host, package):
    c = 'composer global show'
    r = host.run(c)

    assert package in r.stdout
