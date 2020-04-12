import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-ssh-keys (ctorgalson.ssh_keys) tests. """


@pytest.mark.parametrize('key', [
    'id_rsa_molecule.pub',
])
def test_users_authorized_keys(host, key):
    k = open('{}/../files/keys/{}'.format(os.getcwd(), key)).read()
    f = host.file('/home/molecule/.ssh/authorized_keys')

    assert f.exists
    assert k in f.content_string


@pytest.mark.parametrize('user,key,mode', [
    ('molecule', 'id_rsa_molecule', 0o600),
    ('molecule', 'id_rsa_molecule.pub', 0o644),
])
def test_users_ssh_keys(host, user, key, mode):
    k = open('{}/../files/keys/{}'.format(os.getcwd(), key)).read()
    f = host.file('/home/{}/.ssh/{}'.format(user, key))

    assert f.exists
    assert f.mode == mode
    assert f.user == user
    assert f.group == user
    assert k in f.content_string
