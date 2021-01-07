from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2021sensor.data.db.tables import SensorTypes
from dms2021sensor.data.db.exceptions import SensorTypeExistException

class SensorType():

    @staticmethod
    def create(session: Session, sensor_type: str) -> SensorTypes:

        try:
            new_sensor_type = SensorTypes(sensor_type)
            session.add(new_sensor_type)
            session.commit()
            return new_sensor_type
        except IntegrityError as ex:
            raise SensorTypeExistException(
                'Sensor type ' + sensor_type + ' already exists.'
                ) from ex

    @staticmethod
    def delete(session: Session, sensor_type: str):
        try:
            sensor = session.query(SensorTypes).filter_by(sensor_type=sensor_type).first()
            session.delete(sensor)
        except NoResultFound as ex:
            """Sensor type does not exists. No need to nothing"""

    @staticmethod
    def sensor_exists(session: Session, sensor_type) -> bool:
        try:
            query = session.query(SensorTypes).filter_by(sensor_type=sensor_type)
            query.one()
        except NoResultFound:
            return False
        return True