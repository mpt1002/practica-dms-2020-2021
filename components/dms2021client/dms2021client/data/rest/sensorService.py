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
        form : str = urlencode({'sensorname': sensorName})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        direccion = '/sensors'
        connection.request('POST', direccion, form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            response_data_json = response.read()
            response_data = json.loads(response_data_json)
            return response_data[sensorName]
        elif response.status == 404:
            print('Ese sensor no existe')
        else:
            print('Error inesperado ha ocurrido')

    def get_all_values(self) -> dict:
        connection: HTTPConnection = self.__get_connection()
        direccion = '/sensors/values'
        connection.request('GET', direccion)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            response_data_json = response.read()
            response_data = json.loads(response_data_json)
            return response_data
        elif response.status == 400:
            return {}
        else:
            print('Error inesperado ocurrido: ' + str(response.status))
            return {}

    def get_tipos_posibles(self)->dict:
        connection: HTTPConnection = self.__get_connection()
        direccion = '/sensors/types'
        connection.request('GET', direccion)
        response: HTTPResponse = connection.getresponse()
        print(response.status)
        if response.status == 200:
            response_data_json = response.read()
            response_data = json.loads(response_data_json)
            return response_data
        else:
            print('Error inesperado ha ocurrido')
            return {}
