import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


''' ansible-volume (anarcher.volume) tests.

We don't currently have a convenient way to test this in Molecule. This empty
test file included for completeness. '''
