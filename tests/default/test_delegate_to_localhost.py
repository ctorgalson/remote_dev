import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" Tests for localhost-delegated operations not associated with any role. """

""" Paths should be relative to the playbook directory. """
@pytest.mark.parametrize('string', [
    'REMOTE_USER=molecule',
    'REMOTE_IP=172.17.0.3',
    'REMOTE_MOSH_PORT=60033',
    'REMOTE_SSH_PORT=22',
])
def test_rdev_sh(host, string):
    p = '{}/{}'.format(os.getcwd(), 'rdev.sh')

    c = open(p).read()

    assert os.path.isfile(p)
    assert string in c
