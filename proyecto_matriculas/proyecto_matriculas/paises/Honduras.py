import re
from paises.pais import Pais

class Honduras(Pais):
    def __init__(self):
        super().__init__("Honduras")
        self.tipos_vehiculo = {
            'GBA': 'Motocicleta Nacional',
            'CDH': 'Cuerpo Diplomático (Carros)',
            'CBD': 'Cuerpo Diplomático (Motos)',
            'GHA': 'Carros Nacionales',
            'MIH': 'Misión Internacional (Carros)',
            'VTA': 'Régimen de Importación Temporal (Carros)',
            'CCB': 'Cuerpo Consular (Motos)',
            'CCH': 'Cuerpo Consular (Carros)',
            'MIB': 'Misión Internacional (Motos)'
        }

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de Honduras.
        Formato general: Tres letras seguidas de cuatro números (LLL NNNN)
        """
        patron = re.compile(r'^[A-Z]{3} \d{4}$')
        if patron.match(matricula):
            prefijo = matricula[:3]
            if prefijo in self.tipos_vehiculo:
                partes = {
                    'prefijo': prefijo,
                    'numeros': matricula[4:],
                    'tipo_vehiculo': self.tipos_vehiculo[prefijo]
                }
                return True, partes
        return False, {}

    def derivar_matricula(self, partes):
        """
        Deriva información adicional de la matrícula.
        """
        derivacion = []
        derivacion.append(f"El prefijo '{partes['prefijo']}' indica un {partes['tipo_vehiculo']}.")
        derivacion.append(f"Los números '{partes['numeros']}' representan el identificador único del vehículo.")
        return derivacion
