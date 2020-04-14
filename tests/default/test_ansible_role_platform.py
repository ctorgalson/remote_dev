import os

import testinfra.utils.ansible_runner

import pytest


''' ansible-role-platform (ctorgalson.platform) '''


@pytest.mark.parametrize('contents', [
    'PLATFORMSH_CLI_TOKEN',
])
def test_platform_config_in_zshrc(host, contents):
    f = host.file('/home/molecule/.zshrc')

    ''' Todo: ensure not only that the string is IN the rc file, but also that
    it's only in there ONE time. '''
    assert contents in f.content_string
