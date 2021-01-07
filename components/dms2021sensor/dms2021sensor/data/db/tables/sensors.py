
from sqlalchemy import Table, MetaData, Column, ForeignKey, String
from dms2021sensor.data.db.tables.db_table import DBTable

class Sensors(DBTable):
    
    def __init__(self, sensor_name: str, sensor_type: str, parameters: str):
        self.sensor_name: str = sensor_name
        self.sensor_type: str = sensor_type
        self.parameters: str = parameters

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        
        return Table(
            'sensors',
            metadata,
            Column('sensor_name', String(32), primary_key=True),
            Column('sensor_type', ForeignKey('sensor_types.sensor_type'),),
            Column('parameters', String(32)),
        )