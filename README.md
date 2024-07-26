Ansidocker
=========

An Ansible role to install docker on Ubuntu/Debian.
![Ansible Role](https://img.shields.io/ansible/role/d/walidsa3d/docker)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/walidsa3d/ansidocker/main.yml)

Install
------------
```
ansible-galaxy role install walidsa3d.docker

```

Requirements
------------

- Ansible
- Molecule

Variables
--------------
```yaml
data_dir: "/var/lib/docker"
```

Dependencies
------------
- None

Example Playbook
----------------
```yaml
- hosts: all
  roles:
    - walidsa3d.docker
```
License
-------

MIT