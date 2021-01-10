from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2021sensor.data.db.tables.sensors import Sensors
from dms2021sensor.data.db.exceptions import SensorAlreadyExistException, SensorNotFoundException


class Sensor():
    
    @staticmethod
    def create(session: Session, sensor_name: str, sensor_type: str, parameters: str) -> Sensors:

        try:
            new_sensor = Sensors(sensor_name, sensor_type, parameters)
            session.add(new_sensor)
            session.commit()
            return new_sensor
        except IntegrityError as ex:
            raise SensorAlreadyExistException(
                'A sensor with name ' + sensor_name + ' already exists.'
                ) from ex

    @staticmethod
    def update_sensor(session: Session, sensor_name: str, new_sensor_type: str, new_parameters: str)-> Sensors:
        try:
            sensor = session.query(Sensors).filter_by(sensor_name=sensor_name).first()
            session.delete(sensor)
            sensor_update = Sensors(sensor_name, new_sensor_type, new_parameters)
            session.add(sensor_update)
            session.commit()
            return sensor_update
        except NoResultFound as ex:
            raise SensorNotFoundException(
                'A sensor with name ' + sensor_name + ' doesnt not exists.'
                ) from ex

    @staticmethod
    def get_all_sensor(session: Session)-> Sensors:
        try:
            sensor = session.query(Sensors).all()
            return sensor
        except NoResultFound:
            return None

    @staticmethod
    def sensor_exists(session: Session, sensor_name: str, sensor_type: str) -> bool:
        try:
            query = session.query(Sensors).filter_by(sensor_name=sensor_name, sensor_type=sensor_type)
            query.one()
        except NoResultFound:
            return False
        return True
