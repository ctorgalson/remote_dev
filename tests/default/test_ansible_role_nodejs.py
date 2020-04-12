import os

import testinfra.utils.ansible_runner

import pytest

import re


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-nodejs (geerlingguy.nodejs) tests. """


@pytest.mark.parametrize('tool,version', [
    ('node', '^v12'),
    ('npm', '^6'),
])
def test_node_tools(host, tool, version):
    c = '{} --version'.format(tool)
    with host.sudo('molecule'):
        r = host.run(c)

    '''
    Notes:
      - Use `re.match()` rather than `==` to avoid the necessity of being too
        fussy about specific versions.
    '''
    assert bool(re.match(r'{}'.format(version), r.stdout))
