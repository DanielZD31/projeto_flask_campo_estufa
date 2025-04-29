from fabrica.estufa import FabricaEstufa
from fabrica.campo import FabricaCampo

class FabricaCreator:
    @staticmethod
    def obter_fabrica(tipo_ambiente):
        if tipo_ambiente.lower() == 'estufa':
            return FabricaEstufa()
        elif tipo_ambiente.lower() == 'campo':
            return FabricaCampo()
        else:
            raise ValueError("Tipo de ambiente inválido.")
