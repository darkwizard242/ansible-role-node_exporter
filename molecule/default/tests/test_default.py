import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


NE_USER = "node_exporter"
NE_BINARY_FILE = "/usr/local/bin/node_exporter"
NE_SERVICE_FILE = "/etc/systemd/system/node_exporter.service"
NE_SERVICE_NAME = "node_exporter"


def test_node_exporter_user_exists(host):
    """Tests if node_exporter user exists."""
    host.user(NE_USER).exists


def test_node_exporter_binary_exists(host):
    """Tests if /usr/local/bin/node_exporter file exists."""
    host.file(NE_BINARY_FILE).exists


def test_node_exporter_binary_isfile(host):
    """Tests if /usr/local/bin/node_exporter file type is file."""
    assert host.file(NE_BINARY_FILE).is_file


def test_node_exporter_binary_which(host):
    """Tests output of command matches /usr/local/bin/node_exporter"""
    assert host.check_output('which node_exporter') == NE_BINARY_FILE


def test_node_exporter_service_file_exists(host):
    """Tests if /etc/systemd/system/node_exporter.service file exists."""
    host.file(NE_SERVICE_FILE).exists


def test_node_exporter_service_is_enabled(host):
    """Tests if node_exporter.service is enabled."""
    assert host.service(NE_SERVICE_NAME).is_enabled


def test_node_exporter_service_is_running(host):
    """Tests if node_exporter.service is running."""
    assert host.service(NE_SERVICE_NAME).is_running
