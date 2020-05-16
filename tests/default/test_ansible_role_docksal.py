import os

import testinfra.utils.ansible_runner

import pytest


''' ansible-role-docksal (ctorgalson.docksal) '''


@pytest.mark.parametrize('contents', [
    'APACHE_BASIC_AUTH_USER="username"',
    'APACHE_BASIC_AUTH_PASS="password"',
    'DOCKSAL_DNS_DOMAIN="instance.example"',
    'DOCKSAL_VHOST_PROXY_IP="0.0.0.0"',
    'DOCKSAL_VHOST_PROXY_PORT_HTTP="80"',
    'DOCKSAL_VHOST_PROXY_PORT_HTTPS="443"',
    'NGINX_BASIC_AUTH_USER="username"',
    'NGINX_BASIC_AUTH_PASS="password"',
    'SECRET_PLATFORMSH_CLI_TOKEN="109876543210"',
])
def test_docksal_config(host, contents):
    f = host.file('/home/molecule/.docksal/docksal.env')

    assert contents in f.content_string
