import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-security (geerlingguy.security) tests. """


@pytest.mark.parametrize('option', [
    'PasswordAuthentication no',
    'PermitRootLogin no',
    'PermitEmptyPasswords no',
])
def test_ssh_config(host, option):
    f = host.file('/etc/ssh/sshd_config')

    assert option in f.content_string


@pytest.mark.parametrize('user', [
    'molecule'
])
def test_sudoers(host, user):
    c = 'sudo -l -U {}'.format(user)
    r = host.run(c)

    assert 'ALL' in r.stdout
