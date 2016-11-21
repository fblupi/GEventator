Al igual que con Ansible, se utiliza una imagen de Ubuntu Server 14.04 en AWS.

Para provisionar con chef. Lo primero que hay que hacer es instalarlo en la máquina virtual. Para ello hay que conectarse mediante ssh y ejecutar:

```
curl -L https://www.opscode.com/chef/install.sh | sudo bash
```

A continuación instalar Git para clonar el repositorio con los archivos necesarios:

```
sudo apt-get install git
```

Y clonarlo:

```
git clone https://github.com/fblupi/GEventator.git
```

Provisionar con chef-solo:

```
sudo chef-solo -c GEventator/provsion/Chef/chef/solo.rb
```
