from fabrica.interfaces import SensorTemperatura, ModuloIrrigacao, FabricaAgricultura
from singleton.conexao_xml import ConexaoXML

class SensorTemperaturaEstufa(SensorTemperatura):
    def ler(self):
        xml = ConexaoXML().get_xml()
        return xml.find('./Estufa/SensorTemperatura').text

class ModuloIrrigacaoEstufa(ModuloIrrigacao):
    def acionar(self):
        xml = ConexaoXML().get_xml()
        return xml.find('./Estufa/ModuloIrrigacao').text

class FabricaEstufa(FabricaAgricultura):
    def criar_sensor_temperatura(self):
        return SensorTemperaturaEstufa()

    def criar_modulo_irrigacao(self):
        return ModuloIrrigacaoEstufa()
