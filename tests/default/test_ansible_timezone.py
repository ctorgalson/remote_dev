import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-timezone (yatesr.timezone) tests. """


@pytest.mark.parametrize('timezone', [
    'Europe/Paris',
])
def test_timezone(host, timezone):
    f = host.file('/etc/timezone')

    assert timezone in f.content_string
