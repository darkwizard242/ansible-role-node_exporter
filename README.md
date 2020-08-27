[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-node_exporter.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-node_exporter) ![Ansible Role](https://img.shields.io/ansible/role/42050?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/42050?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/42050?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-node_exporter&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-node_exporter) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-node_exporter?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-node_exporter?color=orange&style=flat-square)

# Ansible Role: Node Exporter

Role to install (_by default_) `node_exporter` on **Debian/Ubuntu** and **EL** systems.

## Requirements

None per se.

The systemd service file created for node_exporter streams standard output and standard error to `syslog` and the **SyslogIdentifier** is set as `node_exporter`. Hence, you can review `node_exporter` logs by executing the command `journalctl -u node_exporter.service` on the system. Additionally, you may wish to configure **rsyslog** to collect logs with _programname_ `node_exporter` and output to a specific file for maintaining log files. For log rotation, **darkwizard242.logrotate** role is available on Ansible Galaxy.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
node_exporter_app: node_exporter
node_exporter_version: 0.12.20
node_exporter_osarch: linux_amd64
node_exporter_dl_url: https://releases.hashicorp.com
node_exporter_dl_loc: /tmp
node_exporter_bin_path: /usr/local/bin
```

### Variables table:

Variable               | Value (default)                  | Description
---------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------
node_exporter_app      | node_exporter                    | Defines the app to install i.e. **node_exporter**
node_exporter_version  | 0.12.20                          | Defined to dynamically fetch the desired version to install. Defaults to: **0.12.20**
node_exporter_osarch   | linux_amd64                      | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux_amd64**
node_exporter_dl_url   | <https://releases.hashicorp.com> | Defines URL to download the node_exporter binary from.
node_exporter_dl_loc   | /tmp                             | Defined to dynamically set where to place the binary archive for `node_exporter` temporarily. Defaults to: **/tmp**
node_exporter_bin_path | /usr/local/bin                   | Defined to dynamically set the appropriate path to store node_exporter binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **node_exporter**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.node_exporter
```

For customizing behavior of role (i.e. specifying the desired **node_exporter** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.node_exporter
      vars:
        node_exporter_version: 0.12.20
```

For customizing behavior of role (i.e. placing binary of **node_exporter** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.node_exporter
      vars:
        node_exporter_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-node_exporter/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
