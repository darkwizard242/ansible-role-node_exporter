import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


NODE_EXPORTER_USER = "node_exporter"
NODE_EXPORTER_GROUP = "node_exporter"
NODE_EXPORTER_HOME = "/bin/false"
NODE_EXPORTER_BINARY_FILE = "/usr/local/bin/node_exporter"
NODE_EXPORTER_SERVICE_FILE = "/etc/systemd/system/node_exporter.service"
NODE_EXPORTER_SERVICE_NAME = "node_exporter"


def test_node_exporter_user_exists(host):
    host.user(NODE_EXPORTER_USER).exists


def test_node_exporter_group_check(host):
    host.user(NODE_EXPORTER_USER).group == 'node_exporter'


def test_node_exporter_home_check(host):
    host.user(NODE_EXPORTER_USER).home == '/bin/false'


def test_node_exporter_binary_exists(host):
    host.file(NODE_EXPORTER_BINARY_FILE).exists


def test_node_exporter_binary_isfile(host):
    assert host.file(NODE_EXPORTER_BINARY_FILE).is_file


def test_node_exporter_binary_which(host):
    assert host.check_output('which node_exporter') == \
      NODE_EXPORTER_BINARY_FILE


def test_node_exporter_service_file_exists(host):
    host.file(NODE_EXPORTER_SERVICE_FILE).exists


def test_node_exporter_service_is_enabled(host):
    assert host.service(NODE_EXPORTER_SERVICE_NAME).is_enabled


def test_node_exporter_service_is_running(host):
    assert host.service(NODE_EXPORTER_SERVICE_NAME).is_running
