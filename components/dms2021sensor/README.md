# DMS 2020-2021 Sensor Service

This service provides sensing functionalities to the appliance.

## Installation

Run `./install.sh` for an automated installation.

To manually install the service:

```bash
# Install the service itself.
./setup.py install
```

## Configuration

Configuration will be loaded from the default user configuration directory, subpath `dms2021sensor/config.yml`. This path is thus usually `${HOME}/.config/dms2021sensor/config.yml` in most Linux distros.

The configuration file is a YAML dictionary with the following configurable parameters:

- `db_connection_string` (mandatory): The string used by the ORM to connect to the database.
- `host` (mandatory): The service host.
- `port` (mandatory): The service port.
- `debug`: If set to true, the service will run in debug mode.
- `salt`: A configurable string used to further randomize the password hashing. If changed, existing user passwords will be lost.
- `auth_service`: A dictionary with the configuration needed to connect to the authentication service.
  - `host` and `port`: Host and port used to connect to the service.

## Running the service

As only sensor1 is implemented, it can only be executed throught the command `dms2021sensor1` as any other program.

## REST API specification for sensor1

This service exposes a REST API so other services/applications can interact with it.

- `/` [`GET`]

  Status verification.
  - Returns:
    - `200 OK` if the service is running.
    
- `/sensors/<str: sensorname>/value` [`GET`]
  Gets the value monitorized by the specified sensor
  - Parameters: 
    - `sensorname` [path] (`str`): The sensor name
  -Returns:
    - `200 sensorvalue` if the value of the sensor was sent succesfuly
    - `404 Not foud` if the sensor doesn't existe
    
- `/sensors/<str: sensorname>` [`POST`]
  Gets the value monitorized by the specified sensor
  - Parameters: 
    - `sensorname` [path] (`str`): The sensor name
    - `sensor_type` [from data] (`str`): new type of the sensor
    - `parameters` [from data] (`str''): aditional parameters for the new sensor type
  - Returns:
    - `200 OK` if the sensor was succesfully updated
    - `404 Not found` if the recieved parameters are invalid
    
- `/sensors` [`GET`]
  Gets all the names of the monitorized sensors
  - Returns:
    - `200 sensorsname` if the name of every sensor was sent succesfuly
    - `404 No sensors` if the service has no sensors
    
- `/sensors/types` [`GET`]
  Gets all the posible types of monitorized sensors
  -Returns:
    - `200 sensortypes` if the possible types of sensors was sent succesfuly
    
-`/sensors/values` [`GET`]
  Gets all the values monitorized by all sensors
  -Returns:
    - `200 values of sensors` if the values of every sensor was sent succesfuly
    -`404 Not found`if the sensor service has no sensors


# Arquitectura

## Diagrama UML
Consultar imagen Sensores.png

## Descripción de la arquitectua

dms2021sensor esta dividido en dos carpetas `data` y `logic`. 
 - En la carpeta `data` podemos encontrar:
   - Dentro de la carpeta `config`, un fichero `sensorconfiguration.py` mediante el cual se obtienen los datos necesarios para establecer el servicio.
   - También nos encotramos con el fichero `Sensor.py` donde está definido una clase abstracta denominada 'Sensor' y un método abstracto 'monitorizar'. Esta clase es utilizada para definir los diferentes sensores que componen esta práctica.
   - Finalmente nos encontramos con `SensorFile.py` en el cuál esta definida la clase 'SensorFile' la cuál implementa la clase abtracta anteriormente mencionada 'Sensor' así como el correspondiente método 'monitorizar'. Mediante esta clase se determina la existencia o no, de un determinado fichero en el sistema.
   - Adicionalmente, también encontramos un fichero de texto 'ficheroABuscar.txt' que es usado como fichero por defecto para realizar la búsqueda.
 - En la carpeta `logic` podemos encontrar:
   - Una carpeta denomida 'exc':
     - Donde encontramos `sensorerror.py` donde esta definido `SensorError` que lanza excepciones.
   - Una carpeta 'rest':
     - Que contine el fichero `restSensor.py` que contiene la clase `RestSensor` mediante la cual se establece la conexion del servicio.
