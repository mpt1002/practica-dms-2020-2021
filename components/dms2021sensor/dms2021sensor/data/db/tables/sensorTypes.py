from sqlalchemy import Table, MetaData, Column, String
from dms2021sensor.data.db.tables.db_table import DBTable

class SensorTypes(DBTable):

    def __init__(self, sensor_type: str):
        self.sensor_type: str = sensor_type

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        
        return Table(
            'sensor_types',
            metadata,
            Column('sensor_type', String(32), primary_key=True),
        )