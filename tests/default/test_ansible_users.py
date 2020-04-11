import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-users (weareinteractive.users) tests. """


@pytest.mark.parametrize('user,group,uid,gid,shell', [
    ('molecule', 'molecule', 1000, 1000, '/usr/bin/zsh'),
])
def test_users(host, user, group, uid, gid, shell):
    u = host.user(user)

    assert u.uid == uid
    assert u.gid == gid
    assert u.group == group
    assert u.shell == shell
