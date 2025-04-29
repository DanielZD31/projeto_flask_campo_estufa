from abc import ABC, abstractmethod

class SensorTemperatura(ABC):
    @abstractmethod
    def ler(self):
        pass

class ModuloIrrigacao(ABC):
    @abstractmethod
    def acionar(self):
        pass

class FabricaAgricultura(ABC):
    @abstractmethod
    def criar_sensor_temperatura(self):
        pass

    @abstractmethod
    def criar_modulo_irrigacao(self):
        pass
