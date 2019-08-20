# Ansible Linux based Docker role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-certbot.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-certbot.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-certbot)
[![Galaxy Role Downloads](https://img.shields.io/ansible/role/d/42882.svg?style=flat)](https://galaxy.ansible.com/jetune/certbot)

Ansible role used to install Certbot on Linux based Operating System.

<a href="https://www.kube-cloud.com/"><img width="300" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="200" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>
<a href="https://certbot.eff.org/"><img width="250" src="https://udona.fr/wp-content/uploads/2018/03/le-certlogo-wide.png" /></a>

# Supported OS

| OS Distribution | OS Version |
| ------ | ------ |
| CentOS | 6, + |
| Ubuntu | Xenial, Bionic, + | 

# Role variables

| Variable | Description | Default value |
| ------ | ------ | ------ |
| install_tool | Flag that specify whether install or not Certbot | true |
| generate_certs | Flag that specify whether or not we generate certificates and install renew cron | false |
| certs_validity | Define the generated certificates validity days (before renew) | 80 |
| extra_packages | Define extra packages to install with certbot (used for certbot plugins installation). |  |
| renew_post_command | Command to execute after certificate renewal (for example : restart nginx). |  |

# Usage

* Install Role ``` ansible-galaxy install jetune.certbot ```
* use in your playbook : case of install from repository
```
---
- hosts: all

  roles:
   - role: jetune.docker
     vars:
      install_tool: true
      generate_certs: true
      certs_validity: 90
      extra_packages:
       - certbot-dns-google
       - certbot-dns-cloudflare
      renew_post_command: "service nginx restart"
      
```
