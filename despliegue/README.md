### Despliegue

En este último hito se pondrá en práctica todo lo aprendido durante el curso para realizar el despliegue de la infraestructura virtual que alojará la aplicación GEventator.

La aplicación está dividida en tres microservicios que se ejecutarán en tres máquinas virtuales diferentes (usuarios, eventos y transacciones). Se utilizará AWS pues es la plataforma que se ha estado utilizando durante toda la asignatura. Pero en lugar de utilizar una máquina virtual Ubuntu 14.04, se pasará a la última versión 16.04 aunque no cuente con Python2 instalado por defecto (necesario para provisionar con Ansible).

#### Servicios externos

##### mLab

Para facilitar la gestión de la base de datos, se utilizará [mLab](https://mlab.com/) como servicio externo pues nos ofrece hasta 500 MB de almacenamiento en bases de datos MongoDB de forma gratuita. Para ello solo hay que crearse una cuenta y crear una base de datos:

![mLab](https://cloud.githubusercontent.com/assets/6973564/22506587/94b28540-e881-11e6-9580-ed9a54ba0844.png)

Una vez creada, se puede utilizar el URI que proporciona para conectarse con ella. Al usar Flak en la aplicación se puede conectar incluyendo este URI en el código de la aplicaicón, aunque para ello hay que instalar previamente el paquete pip `mongoengine`.

##### Papertrail

Se ha utilizado Papertrail como sistema de *logs* ya que ofrecía una cuenta gratuita de hasta 100 MB/mes. Además, su integración con Python es trivial, pues se integra con el paquete de *logging* de Python y [solo habría que añadir la dirección de la cuenta](http://help.papertrailapp.com/kb/configuration/configuring-centralized-logging-from-python-apps/) a diferencia de otros servicios como [Logz.io](http://logz.io/) que para integrarlo con Python hace falta instalar un paquete que no está disponible para Python3 (la versión que utiliza GEventator).

#### Provisionamiento

Como ya se ha citado anteriormente, se utilizará Ansible. La justificación es la misma que se hizo en su día. Es un sistema de provisionamiento muy sencillo de utilizar y su integración con Vagrant es muy buena.

Al usar las tres máquinas virtuales las mismas tecnologías, no se ha creado un *playbook* personalizado para cada una sino que se ha utilizado el mismo para todas. No obstante, esto puede ser cambiado fácilmente en cualquier momento pues solo habría que modificar el fichero `.yml` que utiliza Vagrant para provisionar la máquina virtual.

Este *playbook* instalará Docker, pues se utilizará un contenedor con todos los paquetes necesarios instalados.

#### Orquestación

La orquestación de estas máquinas virtuales se realizará con la herramienta que hemos visto con más detalle en la asignatura: Vagrant. Con Vagrant orquestaremos las tres máquinas virtuales en AWS citadas anteriormente y serán provisionadas con Ansible (para ello, previamente se instalará Python2). Una vez instalado, se utilizará el *playbook* de Ansible previamente definido para provisionar estas máquinas virtuales.

#### Contenedores

Se ha creado un [contenedor con todos los paquetes utilizados por la aplicación](https://hub.docker.com/r/fblupi/alpine-flask-mongo/) basado en el que creó [frolvlad con python3 en Alpine](https://hub.docker.com/r/frolvlad/alpine-python3/), una imagen linux de tan solo 5 MB, aunque se ve aumentada a 68,2 MB al instalar python y los paquetes de Flask y MongoDB utilizados.
