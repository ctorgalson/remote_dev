import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-unattended-upgrades (jnv.unattended-upgrades) tests. """


@pytest.mark.parametrize('setting', [
    ('"origin=Ubuntu,archive=${distro_codename}-security,label=Ubuntu";'),
    ('"origin=Ubuntu,archive=${distro_codename},label=Ubuntu";'),
    ('Unattended-Upgrade::Automatic-Reboot "true";'),
    ('Unattended-Upgrade::Automatic-Reboot-Time "02:30";'),
])
def test_unattended_upgrades(host, setting):
    f = host.file('/etc/apt/apt.conf.d/50unattended-upgrades')

    assert setting in f.content_string
