import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-firewall (geerlingguy.firewall) tests. """


@pytest.mark.parametrize('port,protocol', [
    (22, 'tcp'),
    (80, 'tcp'),
    (123, 'udp'),
    (443, 'tcp'),
    (60033, 'tcp'),
])
def test_open_ports(host, port, protocol):
    r = host.iptables.rules()

    if protocol == 'tcp':
        l = '-A INPUT -p tcp -m tcp --dport {} -j ACCEPT'.format(port)
    else:
        l = '-A INPUT -p udp -m udp --sport {} -j ACCEPT'.format(port)

    assert l in r
