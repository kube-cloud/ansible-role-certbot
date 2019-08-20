import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_certbot_installed(host):

    # Certbot command path
    command_path = '/usr/local/bin/certbot-auto'

    # Certbot command link path
    command_link_path = '/usr/local/bin/certbot-auto'
    
    # Check that command exists
    assert host.file(command_path).exists

    # Check that command is file
    assert host.file(command_path).is_file

    # Check that command link exists
    assert host.file(command_link_path).exists

    # Check that command link is symlink
    assert host.file(command_link_path).is_symlink

    # Check symlink target
    assert host.file(command_link_path).linked_to == command_path

    # Execute command and get result
    command_run = host.run(command_link_path)

    # Assert that run is OK
    assert command_run.rc == 0
