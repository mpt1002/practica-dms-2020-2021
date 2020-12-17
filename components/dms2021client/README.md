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
- `1. Crear usuarios`: Permite añadir usuarios al servicio de autenticación. Los usuarios recien creados no tendrán ningún permiso.
- `2. Modificar permisos`: Se pide un usuario y se modifica el permiso introducido a ese usuario. Las posibles modificaciones pueden ser añadir o revocar los permisos. Para poder modificar permisos
			    se ha detener el permiso `AdminRights`.
- `3. Acceder a gestionar sensores`: Permite crear y destruir sensores del servicio sensor. Esta opción todavía no funciona (pues el profesor dijo que no era necesario), pero se planea introducirlo
				      en la entrega 2. Si se ejecuta ahora saldrá un mensaje indicando que esta incompleto. Se ha de tener el permiso AdminSensors
- `4. Modificar las reglas de gestión de cada sensor`: Permite al usuario cambiar las reglas de monitorización del sensor elegido. Los posibles cambios que se pueden realizar sobre los sensores son
							 elegir el tipo de sensor y cambiar los parametros de monitorización de los sensores. Se han de tener los permisos de AdminRules para realizar
							 estos cambios sobre el sensor.
- `5. Obtener valores de monitorización de cada sensor`: Devuelve los valores resultantes de monitorizar cada sensor del servicio sensor elegido. Se ha de tener el permiso de ViewReports.
- `6. Salir`: Cierra la sesion del usuario y termina el programa.
