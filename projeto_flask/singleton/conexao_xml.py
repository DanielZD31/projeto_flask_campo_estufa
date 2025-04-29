import os
import xml.etree.ElementTree as ET

class ConexaoXML:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._load_xml()
        return cls._instancia

    def _load_xml(self):
        caminho = os.path.join(os.path.dirname(__file__), '..', 'dados', 'banco.xml')
        caminho = os.path.abspath(caminho)
        self.tree = ET.parse(caminho)
        self.root = self.tree.getroot()

    def get_xml(self):
        return self.root
