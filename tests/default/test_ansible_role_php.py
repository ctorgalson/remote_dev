import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


''' ansible-role-php (geerlingguy.php) tests. '''


@pytest.mark.parametrize('package,version,path', [
    ('php', 'PHP 7.2', '/usr/bin/php'),
])
def test_php_package(host, package, version, path):
    v = '{} --version'.format(package)
    c = 'command -v {}'.format(package)

    assert version in host.run(v).stdout
    assert path in host.run(c).stdout
