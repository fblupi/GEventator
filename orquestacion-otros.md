---
layout: index
---

## Orquestación de compañeros

### Griger

[Enlace a su issue](https://github.com/Griger/CC/issues/11#issuecomment-266542156).

```
Bringing machine 'local' up with 'virtualbox' provider...
Bringing machine 'data' up with 'aws' provider...
Bringing machine 'ppal' up with 'aws' provider...
==> local: Box 'ubuntu/trusty64' could not be found. Attempting to find and install...
    local: Box Provider: virtualbox
    local: Box Version: >= 0
==> local: Loading metadata for box 'ubuntu/trusty64'
    local: URL: https://atlas.hashicorp.com/ubuntu/trusty64
==> local: Adding box 'ubuntu/trusty64' (v20161207.0.0) for provider: virtualbox
    local: Downloading: https://atlas.hashicorp.com/ubuntu/boxes/trusty64/versions/20161207.0.0/providers/virtualbox.box
==> local: Successfully added box 'ubuntu/trusty64' (v20161207.0.0) for 'virtualbox'!
==> local: Importing base box 'ubuntu/trusty64'...
==> local: Matching MAC address for NAT networking...
==> local: Checking if box 'ubuntu/trusty64' is up to date...
==> local: Setting the name of the VM: Local
==> local: Clearing any previously set forwarded ports...
==> local: Clearing any previously set network interfaces...
==> local: Preparing network interfaces based on configuration...
    local: Adapter 1: nat
==> local: Forwarding ports...
    local: 22 (guest) => 2222 (host) (adapter 1)
==> local: Booting VM...
==> local: Waiting for machine to boot. This may take a few minutes...
    local: SSH address: 127.0.0.1:2222
    local: SSH username: vagrant
    local: SSH auth method: private key
    local: Warning: Remote connection disconnect. Retrying...
    local:
    local: Vagrant insecure key detected. Vagrant will automatically replace
    local: this with a newly generated keypair for better security.
    local:
    local: Inserting generated public key within guest...
    local: Removing insecure key from the guest if it's present...
    local: Key inserted! Disconnecting and reconnecting using new SSH key...
==> local: Machine booted and ready!
==> local: Checking for guest additions in VM...
    local: The guest additions on this VM do not match the installed version of
    local: VirtualBox! In most cases this is fine, but in rare cases it can
    local: prevent things such as shared folders from working properly. If you see
    local: shared folder errors, please make sure the guest additions within the
    local: virtual machine match the version of VirtualBox you have installed on
    local: your host and reload your VM.
    local:
    local: Guest Additions Version: 4.3.36
    local: VirtualBox Version: 5.1
==> local: Mounting shared folders...
    local: /vagrant => /home/fblupi/.vagrant/dummy
==> local: Running provisioner: ansible...
    local: Running ansible-playbook...
[DEPRECATION WARNING]: Instead of sudo/sudo_user, use become/become_user and
make sure become_method is 'sudo' (default).
This feature will be removed in a
future release. Deprecation warnings can be disabled by setting
deprecation_warnings=False in ansible.cfg.

PLAY [all] *********************************************************************

TASK [setup] *******************************************************************
ok: [local]

TASK [Actualizar cache para distros tipo Debian] *******************************
changed: [local]

TASK [Actualizar cache para distros tipo CentOS] *******************************
skipping: [local]

TASK [instalar Flask] **********************************************************
changed: [local]

TASK [instalar PyMongo] ********************************************************
changed: [local]

TASK [instalar MongoDB] ********************************************************
changed: [local]

PLAY RECAP *********************************************************************
local                      : ok=5    changed=4    unreachable=0    failed=0   

==> data: Warning! The AWS provider doesn't support any of the Vagrant
==> data: high-level network configurations (`config.vm.network`). They
==> data: will be silently ignored.
==> data: Launching an instance with the following settings...
==> data:  -- Type: t2.micro
==> data:  -- AMI: ami-01f05461
==> data:  -- Region: us-west-2
==> data:  -- Keypair: fblupi-key-pair-uswest2
==> data:  -- Security Groups: ["vagrant"]
==> data:  -- Block Device Mapping: []
==> data:  -- Terminate On Shutdown: false
==> data:  -- Monitoring: false
==> data:  -- EBS optimized: false
==> data:  -- Source Destination check:
==> data:  -- Assigning a public IP address in a VPC: false
==> data:  -- VPC tenancy specification: default
==> data: Waiting for instance to become "ready"...
==> data: Waiting for SSH to become available...
==> data: Machine is booted and ready for use!
==> data: Running provisioner: ansible...
    data: Running ansible-playbook...
[DEPRECATION WARNING]: Instead of sudo/sudo_user, use become/become_user and
make sure become_method is 'sudo' (default).
This feature will be removed in a
future release. Deprecation warnings can be disabled by setting
deprecation_warnings=False in ansible.cfg.

PLAY [all] *********************************************************************

TASK [setup] *******************************************************************
ok: [data]

TASK [Actualizar cache para distros tipo Debian] *******************************
changed: [data]

TASK [Actualizar cache para distros tipo CentOS] *******************************
skipping: [data]

TASK [instalar Flask] **********************************************************
changed: [data]

TASK [instalar Pandas] *********************************************************
changed: [data]

PLAY RECAP *********************************************************************
data                       : ok=4    changed=3    unreachable=0    failed=0   

==> ppal: Warning! The AWS provider doesn't support any of the Vagrant
==> ppal: high-level network configurations (`config.vm.network`). They
==> ppal: will be silently ignored.
==> ppal: Launching an instance with the following settings...
==> ppal:  -- Type: t2.micro
==> ppal:  -- AMI: ami-01f05461
==> ppal:  -- Region: us-west-2
==> ppal:  -- Keypair: fblupi-key-pair-uswest2
==> ppal:  -- Security Groups: ["vagrant"]
==> ppal:  -- Block Device Mapping: []
==> ppal:  -- Terminate On Shutdown: false
==> ppal:  -- Monitoring: false
==> ppal:  -- EBS optimized: false
==> ppal:  -- Source Destination check:
==> ppal:  -- Assigning a public IP address in a VPC: false
==> ppal:  -- VPC tenancy specification: default
==> ppal: Waiting for instance to become "ready"...
==> ppal: Waiting for SSH to become available...
==> ppal: Machine is booted and ready for use!
==> ppal: Running provisioner: ansible...
    ppal: Running ansible-playbook...
[DEPRECATION WARNING]: Instead of sudo/sudo_user, use become/become_user and
make sure become_method is 'sudo' (default).
This feature will be removed in a
future release. Deprecation warnings can be disabled by setting
deprecation_warnings=False in ansible.cfg.

PLAY [all] *********************************************************************

TASK [setup] *******************************************************************
ok: [ppal]

TASK [Actualizar cache para distros tipo Debian] *******************************
changed: [ppal]

TASK [Actualizar cache para distros tipo CentOS] *******************************
skipping: [ppal]

TASK [instalar Flask] **********************************************************
changed: [ppal]

TASK [instalar PyMongo] ********************************************************
changed: [ppal]

PLAY RECAP *********************************************************************
ppal                       : ok=4    changed=3    unreachable=0    failed=0   
```
