import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_node_exporter_group_exists(host):
    host.user('node_exporter').exists


def test_node_exporter_group_check(host):
    host.user('node_exporter').group == 'node_exporter'


def test_node_exporter_home_check(host):
    host.user('node_exporter').home == '/bin/false'


def test_node_exporter_binary_exists(host):
    host.file('/usr/local/bin/node_exporter').exists


def test_node_exporter_binary_isfile(host):
    assert host.file('/usr/local/bin/node_exporter').is_file


def test_node_exporter_binary_which(host):
    assert host.check_output('which node_exporter') == \
      '/usr/local/bin/node_exporter'


def test_node_exporter_service_file_exists(host):
    host.file('/etc/systemd/system/node_exporter.service').exists


def test_node_exporter_service_is_enabled(host):
    assert host.service('node_exporter').is_enabled


def test_node_exporter_service_is_running(host):
    assert host.service('node_exporter').is_running
