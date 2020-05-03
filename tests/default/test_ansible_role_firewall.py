import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-firewall (geerlingguy.firewall) tests. """


@pytest.mark.parametrize('service_or_port', [
    22,
    60033,
])
def test_open_ports(host, service_or_port):
    r = host.iptables.rules()
    l = '-A INPUT -p tcp -m tcp --dport {} -j ACCEPT'.format(service_or_port)

    assert l in r
