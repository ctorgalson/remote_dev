import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-security (geerlingguy.security) tests. """


@pytest.mark.parametrize('service', [
    'clamav-daemon',
    'clamav-freshclam',
])
def test_services(host, service):
    s = host.service(service)

    assert s.is_enabled
    assert s.is_running
