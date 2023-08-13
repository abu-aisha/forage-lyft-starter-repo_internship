from abc import ABC,abstractmethod



class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass

    # def engine_should_be_serviced(self):
    #     return self.current_mileage - self.last_service_mileage > 30000
