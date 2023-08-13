from battery_dir.battery import Battery


class Spindler(Battery):
    def __init__(self,last_service_date,current_date) -> None:
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self):
        threshold_date = self._last_service_date.replace(year =self._last_service_date.year +3)
        if self._current_date > threshold_date:
            return True
        else:
            return False


class Nubbin(Battery):
    def __init__(self,last_service_date,current_date) -> None:
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self):
        threshold_date = self._last_service_date.replace(year = self._last_service_date.year +4)
        if self._current_date > threshold_date:
            return True
        else:
            return False
        