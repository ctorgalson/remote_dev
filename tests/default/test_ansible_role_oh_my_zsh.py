import os

import testinfra.utils.ansible_runner

import pytest

import re


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-oh-my-zsh (ctorgalson.oh-my-zsh) tests. """


@pytest.mark.parametrize('plugin', [
  'git',
  'history',
  'history-substring-search',
  'nvm',
  'ssh-agent',
  'z',
])
def test_oh_my_zsh_plugins(host, plugin):
    f = host.file('/home/molecule/.zshrc')
    m = re.search(r'\nplugins=\(([^)]*)\)\n', f.content_string)

    assert plugin in m.groups()[0]
