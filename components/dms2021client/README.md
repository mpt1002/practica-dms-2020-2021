# DMS 2020-2021 Client application

This applicationserves as the control console for the different services of the appliance.

## Installation

Run `./install.sh` for an automated installation.

To manually install the service:

```bash
# Install the service itself.
./setup.py install
```

## Configuration

Configuration will be loaded from the default user configuration directory, subpath `dms2021client/config.yml`. This path is thus usually `${HOME}/.config/dms2021client/config.yml` in most Linux distros.

The configuration file is a YAML dictionary with the following configurable parameters:

- `debug`: If set to true, the service will run in debug mode.
- `auth_service`: A dictionary with the configuration needed to connect to the authentication service.
  - `host` and `port`: Host and port used to connect to the service.
- `sensors`: A dictionary with the configuration needed to connect to the different sensor services. Each key identifies a sensor, and their values are themselves dictionaries with the connection information:
  - `host` and `port`: Host and port used to connect to the service.

## Running the service

Just run `dms2021client` as any other program.

## Contenido

El programa te permite navegar a través de un programa que permite gestionar distintos aspectos de los servicios de autenticación y de los sensores.
Las acciones que puedes realizar en este programa son:
- `1. Crear usuarios`: Permite añadir usuarios al servicio de autenticación. Los usuarios recien creados no tendrán ningún permiso. Para poder crear usuarios se ha de tener el permiso `AdminUsers`.
- `2. Modificar permisos`: Se pide un usuario y se modifica el permiso introducido a ese usuario. Las posibles modificaciones pueden ser añadir o revocar los permisos. Para poder modificar permisos
			    se ha detener el permiso `AdminRights`.
- `3. Acceder a gestionar sensores`: Permite crear y destruir sensores del servicio sensor. Esta opción todavía no funciona (pues el profesor dijo que no era necesario), pero se planea introducirlo
				      en la entrega 2. Si se ejecuta ahora saldrá un mensaje indicando que esta incompleto. Se ha de tener el permiso `AdminSensors`
- `4. Modificar las reglas de gestión de cada sensor`: Permite al usuario cambiar las reglas de monitorización del sensor elegido. Los posibles cambios que se pueden realizar sobre los sensores son
							 elegir el tipo de sensor y cambiar los parametros de monitorización de los sensores. Se han de tener los permisos de `AdminRules` para realizar
							 estos cambios sobre el sensor.
- `5. Obtener valores de monitorización de cada sensor`: Devuelve los valores resultantes de monitorizar cada sensor del servicio sensor elegido. Se ha de tener el permiso de `ViewReports`.
- `6. Salir`: Cierra la sesion del usuario y termina el programa.

## Arquitectura
### Diagrama UML
Ver imagen Clases1.3.png

### Descripción de la arquitectura
dms2021client esta dividido en tres carpetas: `data`, `logic` y `presentation`. Estas tres carpetas siguen un planteamiento MVC (modelo, vista, controlador).
En la carpeta `data` hay dos subcarpetas: la carpeta `config`, que se utiliza para obtener los datos necesarios para establecer contacto con los servicios sensores y el servicio de autenticación. La
otra carpeta es la carptea `rest`, que contiene las clases necesarias para comunicarse con los servicios de autenticacion (con `authservice.py`) y los servicios sensores (con `sensorService.py`).
En la carpeta `logic` se encuentra la clase `ManejadorPagina.py` que se encarga de manejar el viaje entre páginas de la aplicación. Al iniciar el servicio cliente se llema a esta clase, que asume el
rol de guiar al usuario entre páginas.
En la carpeta `presentation` se encuentran las páginas entre las que se viaja y la clase de la que todas estas heredan (`serviciosEstado.py`). El viaje entre páginas implementa el patron estado. El 
`contexto` del patrón es la clase `ManejadorPagina`, que se encargará de viajar entre páginas. Los `estados` serán las posibles páginas entre las que se puede navegar, siendo el `estado abstracto` la
clase `ServiciosEstado` y los `estados concretos` que heredan de este `AjusteSensoresEstado`, `CrearUsuariosEstado`, `ExitEstado`, `GestionarSensoresEstado`, `MenuEstado`, `ModificarPermisosEstado` y 
`MonitorizarSensoresEstado`.

### Relaciones entre clases
- `AjusteSensoresEstado`, `CrearUsuariosEstado`, `ExitEstado`, `GestionarSensoresEstado`, `MenuEstado`, `ModificarPermisosEstado` y `MonitorizarSensoresEstado` heredan de `ServiciosEstado`.
- `ManejadorPagina` se encarga de la transición entre los distintos `estados concretos`.
- `ManejadorPagina` entra en pide a `ClientConfiguration` (`config/clientConfig.py`) los datos necesarios para establecer contacto con los servicios sensores y el servicio de autenticacion.
- Los `estados concretos` hacen uso de las clases `AuthService` y `SensorService`para comunicarse con los servicios de autenticación y los servicios sensores y pedir y modificar datos de los servicios.
- `ManejadorPagina` asigna a los `estados concretos` los servicios con los que van a interacituar.
