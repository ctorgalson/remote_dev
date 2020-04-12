import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-environment (weareinteractive.environment) tests. """


@pytest.mark.parametrize('name,value', [
    ('LC_ALL', 'en_US.UTF-8'),
])
def test_packages(host, name, value):
    f = host.file('/etc/environment')
    e = '{}=\'{}\''.format(name, value)

    assert e in f.content_string
