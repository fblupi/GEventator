---
layout: index
---

# GEventator

## Provisionamiento

### Ansible

En primer lugar cambiar el fichero `ansible_hosts` con la ip correspondiente a una máquina virtual AWS que contenga una imagen de Ubuntu 14.04.

Copiar la clave privada (archivo `.pem`) para conectarse a esa máquina virtual en este directorio y ponerle como nombre `key.pem`.

Ejecutar la orden:

```
ansible-playbook -i ansible_hosts --private-key key.pem -b playbook.yml
```

---

Volver a [home](index)