import json
from urllib.parse import urlencode
from http.client import HTTPConnection, HTTPResponse, HTTPException
from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError

class SensorService():
    """ REST client to connect to the sensor service.
    """

    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port

    def __get_connection(self) -> HTTPConnection:
        return HTTPConnection(self.__host, self.__port)

    def is_running(self) -> bool:
        try:
            connection: HTTPConnection = self.__get_connection()
            connection.request('GET', '/')
            response: HTTPResponse = connection.getresponse()
            if response.status == 200:
                return True
            return False
        except HTTPException:
            return False
        except ConnectionRefusedError:
            return False

    def get_sensor_value(self, sensorName : str):
        connection: HTTPConnection = self.__get_connection()
        direccion = '/sensor/' + str(sensorName) + '/value'
        connection.request('GET', '/')
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            #Falta devolver el valor del sensor
            pass
        elif response.status == 404:
            print('Ese sensor no existe')
        else:
            print('Error inesperado ha ocurrido')
