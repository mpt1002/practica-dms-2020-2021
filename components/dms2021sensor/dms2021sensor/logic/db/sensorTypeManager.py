from dms2021sensor.data.db import Schema
from dms2021sensor.data.db.resultsets import SensorType
from sqlalchemy.orm import Session  # type: ignore

class SensorTypeManager:
    
    def __init__(self, schema: Schema):
        """ Constructor method.
        Initializes the manager.
        ---
        Parameters:
            - schema: The database schema instance to use.
        """
        self.__set_schema(schema)

    def add_sensor_type(self, new_sensor_type: str):
        session: Session = self.get_schema().new_session()
        SensorType.create(session, new_sensor_type)

    def remove_sensor_type(self, sensor_type: str):
        session: Session = self.get_schema().new_session()
        SensorType.delete(session, sensor_type)

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