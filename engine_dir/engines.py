from abc import ABC
from engine_dir.engine import Engine

class WilloughbyEngine(Engine, ABC):
    def __init__(self,last_service_mileage,current_mileage) -> None:
        self._last_service_mileage = last_service_mileage
        self._current_mileage = current_mileage

    def needs_service(self):
        if (self._current_mileage - self._last_service_mileage)>60000:
            return True
        else:
            False

class CapuletEngine(Engine, ABC):
    def __init__(self,last_service_mileage,current_mileage) -> None:
        self._last_service_mileage = last_service_mileage
        self._current_mileage = current_mileage

    def needs_service(self):
        if (self._current_mileage - self._last_service_mileage)>30000:
            return True
        else:
            False
        

class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on):
        
        self._warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self._warning_light_is_on:
            return True
        else:
            return False
