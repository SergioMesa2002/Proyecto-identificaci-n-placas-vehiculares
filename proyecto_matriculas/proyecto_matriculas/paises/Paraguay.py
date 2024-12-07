import re

from paises.pais import Pais

class Paraguay(Pais):
    def __init__(self):
        super().__init__("Paraguay")
        self.departamentos = {
            'A': 'Alto Paraguay',
            'B': 'Alto Paraná',
            'C': 'Amambay',
            'D': 'Asunción (Capital)',
            'E': 'Boquerón',
            'F': 'Caaguazú',
            'G': 'Caazapá',
            'H': 'Canindeyú',
            'I': 'Central',
            'J': 'Concepción',
            'K': 'Cordillera',
            'L': 'Guairá',
            'M': 'Itapúa',
            'N': 'Misiones',
            'O': 'Ñeembucú',
            'P': 'Paraguarí',
            'Q': 'Presidente Hayes',
            'R': 'San Pedro'
        }

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de Paraguay.
        Formato: ABCD 123 (cuatro letras seguidas de tres números)
        """
        patron = re.compile(r'^[A-Z]{4} \d{3}$')
        if patron.match(matricula):
            partes = {
                'letras': matricula[:4],
                'numeros': matricula[5:],
                'departamento': self.departamentos.get(matricula[0], 'Desconocido')
            }
            return True, partes
        return False, {}

    def derivar_matricula(self, partes):
        """
        Deriva información adicional de la matrícula.
        """
        derivacion = []
        derivacion.append(f"La primera letra '{partes['letras'][0]}' indica el departamento de {partes['departamento']}.")
        derivacion.append(f"Las letras '{partes['letras']}' corresponden a la serie asignada.")
        derivacion.append(f"Los números '{partes['numeros']}' representan el número secuencial del vehículo.")
        return derivacion
