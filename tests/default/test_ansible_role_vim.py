import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-vim (ctorgalson.vim) tests. """


@pytest.mark.parametrize('plugin', [
    'ale',
    'editorconfig-vim',
    'emmet-vim',
    'fzf.vim',
    'goyo.vim',
    'lightline.vim',
    'nerdcommenter',
    'nerdtree',
    'vim-better-whitespace',
    'vim-colors-solarized',
    'vim-css-color',
    'vim-devicons',
    'vim-fugitive',
    'vim-javascript',
    'vim-polyglot',
    'vim-surround',
    'vim-gitgutter',
])
def test_vim_plugins(host, plugin):
    u = 'molecule'
    p = '/home/{}/.vim/pack/ansible-managed'.format(u)
    c = ('find {} -type d -maxdepth 2'.format(p))
    with host.sudo('molecule'):
        r = host.run(c)

    assert plugin in r.stdout
