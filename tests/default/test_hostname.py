import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" hostname (anxs.hostname) tests. """

"""
ANXS.hostname (and other hostname roles) modify /etc/hosts directly. In the
Molecule context, this results in an error: "failed final rename". This in turn
is due to running in a container. Consequently, we do not run the role in
Molecule, and don't test its output. See e.g.:

 - https://git.io/JfW2h
 - https://git.io/JfW2N
"""
