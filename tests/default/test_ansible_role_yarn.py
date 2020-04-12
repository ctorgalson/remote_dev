import os

import testinfra.utils.ansible_runner

import pytest

import re


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-yarn (ocha.yarn) tests. """


@pytest.mark.parametrize('package,version', [
    ('yarn', '1.22'),
])
def test_yarn_packages(host, package, version):
    p = host.package(package)

    assert p.is_installed
    assert version in p.version
