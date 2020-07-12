import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_node_exporter_package_installed(host):
    assert host.package("google-cloud-sdk").is_installed


def test_node_exporter_binary_exists(host):
    host.file('/usr/local/bin/node_exporter').exists


def test_node_exporter_binary_isfile(host):
    assert host.file('/usr/local/bin/node_exporter').is_file


def test_node_exporter_binary_which(host):
    assert host.check_output('which node_exporter') == \
      '/usr/local/bin/node_exporter'
