import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_certbot_installed(host):

    # Certbot command path
    command_path = '/usr/bin/certbot'

    # Check that command exists
    assert host.file(command_path).exists

    # Check that command is file
    assert host.file(command_path).is_file

    # Execute command and get result
    command_run = host.run(command_path + ' --version')

    # Assert that run is OK
    assert command_run.rc == 0
