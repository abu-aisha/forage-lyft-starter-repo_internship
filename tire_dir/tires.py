from tire_dir.tire import Tire


class Carrigan(Tire):
    def __init__(self,tire_worn_rslt_array:list) -> None:
        self._tire_worn_rslt_array = tire_worn_rslt_array
        

    def needs_service(self):
        bool_arr = [True for ii in self._tire_worn_rslt_array if ii >= 0.9]
        if bool_arr:
            return True
        else:
            return False


class OctoPrime(Tire):
    def __init__(self,tire_worn_rslt_array:list) -> None:
        self._tire_worn_rslt_array = tire_worn_rslt_array

    def needs_service(self):
        arr_sum = sum(self._tire_worn_rslt_array)
        if arr_sum >= 3:
            return True
        else:
            return False
        