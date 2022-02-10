[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-node_exporter.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-node_exporter) ![Ansible Role](https://img.shields.io/ansible/role/50612?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/50612?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/50612?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-node_exporter&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-node_exporter) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-node_exporter?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-node_exporter?color=orange&style=flat-square)

# Ansible Role: Node Exporter

Role to install (_by default_) [node_exporter](https://github.com/prometheus/node_exporter) on **Debian/Ubuntu** and **EL** systems.

## Requirements

None per se.

The systemd service file created for node_exporter streams standard output and standard error to `syslog` and the **SyslogIdentifier** is set as `node_exporter`. Hence, you can review `node_exporter` logs by executing the command `sudo journalctl -u node_exporter.service` on the system. Additionally, you may wish to configure **rsyslog** to collect logs with _programname_ `node_exporter` and output to a specific file for maintaining log files. For log rotation, **darkwizard242.logrotate** role is available on [Ansible Galaxy](https://galaxy.ansible.com/darkwizard242/logrotate).

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
node_exporter_app: node_exporter
node_exporter_version: 1.3.1
node_exporter_osarch: linux-amd64
node_exporter_archive_format: tar.gz
node_exporter_dl_url: "https://github.com/prometheus/{{ node_exporter_app }}/releases/download/v{{ node_exporter_version }}/{{ node_exporter_app }}-{{ node_exporter_version }}.{{ node_exporter_osarch }}.{{ node_exporter_archive_format }}"

node_exporter_app_group: "{{ node_exporter_app }}"
node_exporter_app_group_desired_state: present

node_exporter_app_user: "{{ node_exporter_app }}"
node_exporter_app_user_desired_state: present
node_exporter_app_user_home_state: no
node_exporter_app_user_shell: /bin/false

node_exporter_temp_path: /tmp

node_exporter_bin_path: /usr/local/bin
node_exporter_bin_path_mode: '0755'
node_exporter_bin_path_remote_src: yes

node_exporter_systemd_service_setup: true
node_exporter_systemd_service_name: "{{ node_exporter_app }}"
node_exporter_systemd_service_flags: --collector.systemd --collector.processes --collector.mountstats
node_exporter_systemd_service_template: "{{ node_exporter_app }}.service.j2"
node_exporter_systemd_service_template_dest: "/etc/systemd/system/{{ node_exporter_app }}.service"
node_exporter_systemd_service_template_user: root
node_exporter_systemd_service_template_group: root
node_exporter_systemd_service_template_dest_mode: '0644'
node_exporter_systemd_service_template_backup: yes
node_exporter_systemd_service_desired_state: restarted
node_exporter_systemd_service_desired_boot_enabled: yes

node_exporter_app_port: 9100
node_exporter_app_check_status_code: 200
node_exporter_app_check_status_code_retries: 10
node_exporter_app_check_status_code_delay: 5
```

### Variables table:

Variable                                           | Description
-------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------
node_exporter_app                                  | Defines the app to install i.e. **node_exporter**
node_exporter_version                              | Defined to dynamically fetch the desired version to install. Defaults to: **1.0.1**
node_exporter_osarch                               | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux-amd64**
node_exporter_archive_format                       | Defined to use while downloading the archive.
node_exporter_dl_url                               | Defines URL to download the node_exporter binary from.
node_exporter_app_group                            | Name of the group that the node_exporter owner will belong to. Defaults to `node_exporter`.
node_exporter_app_group_desired_state              | present indicates creating the group if it doesn't exist. Alternative is absent.
node_exporter_app_user                             | Name of the user that node_exporter will be owned by. Defaults to `node_exporter`.
node_exporter_app_user_desired_state               | present indicates creating the user if it doesn't exist. Alternative is absent.
node_exporter_app_user_home_state                  | Set to 'no' to not create a home directory for `node_exporter` user.
node_exporter_app_user_shell                       | Variable is used to define if the user should have a default shell. Set to `/bin/false` as not required.
node_exporter_temp_path                            | Temporary path where node_exporter archive is downloaded and extracted.
node_exporter_bin_path                             | Path in which to place the actual `node_exporter` in.
node_exporter_bin_path_mode                        | Permissions for `node_exporter` binary.
node_exporter_bin_path_remote_src                  | Defined to let ansible handle unarchive operation on remote hosts.
node_exporter_systemd_service_setup                | Utilized as a when condition to setup a systemd service file for `node_exporter`. If set to `false`. Systemd service file for `node_exporter` will be created.
node_exporter_systemd_service_name                 | Name of the systemd service file when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_flags                | Variable to store and pass any commandline flags of `node_exporter` in it's service file when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_template             | Jinja2 source systemd service template file to place on host role is applied on when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_template_dest        | Destination filename of node_exporter systemd service when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_template_user        | Owner of node_exporter systemd service file when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_template_group       | Group of node_exporter systemd service file when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_template_dest_mode   | Mode of node_exporter systemd service file when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_template_backup      | To backup any existing node_exporter systemd service file when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_desired_state        | Desired state of node_exporter systemd service when node_exporter_systemd_service_setup is set to true.
node_exporter_systemd_service_desired_boot_enabled | To set node_exporter service as enabled when node_exporter_systemd_service_setup is set to true.
node_exporter_app_port                             | As the default port of node_exporter is 9100, this variable is utilized in a handler that checks for whether node_exporter is running on port 9100 or not.
node_exporter_app_check_status_code                | Status code that the handler looks for when running the check for node_exporter.
node_exporter_app_check_status_code_retries        | Number of times handler tries to check for node_exporter running.
node_exporter_app_check_status_code_delay          | Number of time of delays in seconds that the handler waits for in between checks for node_exporter.

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
        node_exporter_version: 1.0.1
```

For customizing behavior of role (i.e. disabling the setup **node_exporter** systemd service) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.node_exporter
      vars:
        node_exporter_systemd_service_setup: false
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-node_exporter/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
