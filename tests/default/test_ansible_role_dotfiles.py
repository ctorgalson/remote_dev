import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-dotfiles (ctorgalson.dotfiles) tests. """


@pytest.mark.parametrize('dotfile_symlink,dotfile_contents', [
    ('.vimrc', 'colorscheme solarized'),
    ('.gitconfig', 'Torgalson'),
    ('.gitignore_global', '*.retry'),
])
def test_dotfiles(host, dotfile_symlink, dotfile_contents):
    h = '/home/molecule'
    s = host.file('{}/{}'.format(h, dotfile_symlink))

    assert s.exists
    assert s.is_symlink
    assert s.linked_to == '{}/.ansible-managed-config/dotfiles/{}'.format(
        h, dotfile_symlink)
    assert dotfile_contents in s.content_string
