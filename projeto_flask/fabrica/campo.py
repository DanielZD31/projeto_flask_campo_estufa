from fabrica.interfaces import SensorTemperatura, ModuloIrrigacao, FabricaAgricultura
from singleton.conexao_xml import ConexaoXML

class SensorTemperaturaCampo(SensorTemperatura):
    def ler(self):
        xml = ConexaoXML().get_xml()
        return xml.find('./Campo/SensorTemperatura').text

class ModuloIrrigacaoCampo(ModuloIrrigacao):
    def acionar(self):
        xml = ConexaoXML().get_xml()
        return xml.find('./Campo/ModuloIrrigacao').text
    
class FabricaCampo(FabricaAgricultura):
    def criar_sensor_temperatura(self):
        return SensorTemperaturaCampo()
    
    def criar_modulo_irrigacao(self):
        return ModuloIrrigacaoCampo()