from car import Car
from datetime import datetime
from engine_dir.engines import CapuletEngine,WilloughbyEngine,SternmanEngine
from battery_dir.batteries import Nubbin, Spindler

class CarFactory():

   
    def  create_calliope(current_date: datetime, last_service_date: datetime,\
         current_mileage: int, last_service_mileage: int) -> Car:

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = Spindler(last_service_date,current_date)

        car = Car(car_engine,car_battery)

        return car

    def  create_glissade(current_date: datetime, last_service_date: datetime,\
         current_mileage: int, last_service_mileage: int) -> Car:

        car_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car_battery = Spindler(last_service_date,current_date)

        car = Car(car_engine,car_battery)

        return car

    def  create_palindrome(current_date: datetime, last_service_date: datetime,warning_light_is_on: bool) -> Car:
        
        car_engine = SternmanEngine(warning_light_is_on)
        car_battery = Spindler(last_service_date,current_date)

        car = Car(car_engine,car_battery)

        return car

    def  create_rorschach(current_date: datetime, last_service_date: datetime,\
         current_mileage: int, last_service_mileage: int) -> Car:
        
        car_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car_battery = Nubbin(last_service_date,current_date)

        car = Car(car_engine,car_battery)

        return car

    def  create_thovex(current_date: datetime, last_service_date: datetime,\
         current_mileage: int, last_service_mileage: int) -> Car:
        
        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = Nubbin(last_service_date,current_date)

        car = Car(car_engine,car_battery)

        return car

  