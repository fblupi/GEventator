---
layout: index
---

# GEventator

## Introducción

### Descripción del problema

Gestionar un evento no es una tarea fácil, se mueve una gran cantidad de dinero, que no es tuyo y por tanto recae sobre ti una enorme responsabilidad. Hacerlo entre un grupo de personas puede ayudar a la hora de repartirse tareas, pero pueden surgir problemas a la hora de coordinarse. Si cada organizador lleva su propio control de la contabilidad se replica información y a menudo surgen incongruencias.

### Solución propuesta

La idea es desarrollar un software para facilitar toda esta gestión y que sea accesible en todo momento para cualquier organizador. La funcionalidad principal de éste es poder llevar a cabo la gestión económica de un evento (compras, ventas, inversiones, donaciones, patrocinios...). Por otra parte también se podrá gestionar la tabla de actividades que se realizarán durante el evento.

## Tecnología utilizada

### Arquitectura

Se utilizará una arquitectura basada en microservicios, la cual se caracteriza por usar servicios desplegados independiente y que funcionan también independientemente unos de otros.

El núcleo de esta arquitecutra es una API REST programada en [Flask](http://flask.pocoo.org/).

#### Microservicios

Se podrían tener tres microservicios actuando de forma independiente los unos con los otros (correspondientes a cada uno de los módulos de la aplicación):

- Gestión de usuarios
- Gestión de eventos
- Gestión de transacciones

Cada uno de estos con su correspondiente base de datos.

!["arquitectura de microservicios"](https://github.com/fblupi/GEventator/raw/gh-pages/img/microservicios.png)

### Back-end

Se utilizará [Flask](http://flask.pocoo.org/) como framework para desarrollar el back-end (tanto la API REST como los distintos microservicios) junto con varias bases de datos [MongoDB](https://www.mongodb.com/).

### Front-end

Si se llega a desarrollar el front-end, se usará HTML, CSS y JavaScript usando [Materialize](http://materializecss.com/) como framework.

## Licencia

El software está sujeto a la licencia [GNU GPL v3](https://github.com/fblupi/master_informatica-CC/blob/master/LICENSE).
