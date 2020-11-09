import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


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


@pytest.mark.parametrize('name,ports', [
    ('docksal-ssh-agent', ''),
    ('docksal-dns', '192.168.64.100:53->53/udp'),
    ('docksal-vhost-proxy', '0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp'),
])
def test_docksal_containers(host, name, ports):
    """ It would make sense to use host.docker() or host.docker.get_containers()
    here, but it's actually simpler to just run the command and look in the
    output. """
    c = 'docker ps --filter name={}'.format(name)
    r = host.run(c)

    assert 'healthy' in r.stdout

    if ports:
        assert ports in r.stdout
