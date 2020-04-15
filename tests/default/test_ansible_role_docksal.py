import os

import testinfra.utils.ansible_runner

import pytest


''' ansible-role-docksal (ctorgalson.docksal) '''


@pytest.mark.parametrize('contents', [
    'DOCKSAL_VHOST_PROXY_IP="0.0.0.0"',
    'SECRET_PLATFORMSH_CLI_TOKEN="109876543210"',
])
def test_docksal_config(host, contents):
    f = host.file('/home/molecule/.docksal/docksal.env')

    assert contents in f.content_string
