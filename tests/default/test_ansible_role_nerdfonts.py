import os

import testinfra.utils.ansible_runner

import pytest

from pwd import getpwuid

""" from grp import getgrgid """


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-nerdfonts (ctorgalson.nerdfonts) tests. """

"""
Notes:
  - Paths should be relative to the playbook directory.
  - Temporarily not checking groups until we work out a way to handle the
    differences between local and github actions (probably, we should reproduce
    the user/group of the github actions environment here).
"""


@pytest.mark.parametrize('font_path', [
    'UbuntuMono/Ubuntu Mono Nerd Font Complete.ttf',
])
def test_nerdfonts(host, font_path):
    p = '{}/.local/share/fonts/NerdFonts/{}'.format(os.getcwd(), font_path)
    u = getpwuid(os.getuid()).pw_name

    assert os.path.isfile(p)
    assert getpwuid(os.stat(p).st_uid).pw_name == u
    """ assert getgrgid(os.stat(p).st_gid).gr_name == u """
