from dms2021sensor.data.db import Schema
from sqlalchemy.orm import Session  # type: ignore
from dms2021sensor.data.db.resultsets import Sensor

class SensorManager:
    
    def __init__(self, schema: Schema):
        """ Constructor method.
        Initializes the manager.
        ---
        Parameters:
            - schema: The database schema instance to use.
        """
        self.__set_schema(schema)

    def add_sensor(self, sensor_name: str, sensor_type: str, parameters: str):
        session: Session = self.get_schema().new_session()
        Sensor.create(session, sensor_name, sensor_type, parameters)

    def update_sensor(self, session: Session, sensor_name: str, new_sensor_type: str, new_parameters: str):
        session: Session = self.get_schema().new_session()
        Sensor.update_sensor(session, sensor_name, new_sensor_type, new_parameters)

    def get_schema(self) -> Schema:
        """ Gets the schema being used by this instance.
        ---
        Returns:
            The DB schema object used by the validator.
        """
        return self.__schema

    def __set_schema(self, schema: Schema):
        """ Sets the schema to be used by this instance.
        ---
        Parameters:
            - schema: The database schema instance to use.
        """
        self.__schema = schema