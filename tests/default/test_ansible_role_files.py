import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-files (ctorgalson.files) tests. """


@pytest.mark.parametrize('path,type', [
    ('Projects', 'directory'),
    ('Projects/Client', 'directory'),
])
def test_users(host, path, type):
    f = host.file('/home/molecule/{}'.format(path))

    assert f.exists
    assert f.user == 'molecule'
    assert f.group == 'molecule'

    if type == 'directory':
        assert f.is_directory
    elif type == 'file':
        assert f.is_file
    elif type == 'symlink':
        assert f.is_symlink
