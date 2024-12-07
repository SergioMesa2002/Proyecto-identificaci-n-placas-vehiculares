import re
from paises.pais import Pais

class Nicaragua(Pais):
    def __init__(self):
        super().__init__("Nicaragua")
        self.departamentos = {
            'M': 'Managua',
            'LE': 'León',
            'GR': 'Granada',
            'ES': 'Estelí',
            'MT': 'Matagalpa',
            'CO': 'Chontales',
            'MD': 'Madriz',
            'NS': 'Nueva Segovia',
            'BO': 'Boaco',
            'CI': 'Chinandega',
            # Agregar otros departamentos según corresponda
        }

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de Nicaragua.
        Formato: Una o dos letras seguidas de un espacio y luego dos bloques de tres números separados por un guion.
        Ejemplo: M 123-456 o LE 123-456
        """
        patron = re.compile(r'^([A-Z]{1,2}) (\d{3})-(\d{3})$')
        match = patron.match(matricula)
        if match:
            prefijo = match.group(1)
            if prefijo in self.departamentos:
                partes = {
                    'prefijo': prefijo,
                    'numeros': f"{match.group(2)}-{match.group(3)}",
                    'departamento': self.departamentos[prefijo]
                }
                return True, partes
        return False, {}

    def derivar_matricula(self, partes):
        """
        Deriva información adicional de la matrícula.
        """
        derivacion = []
        derivacion.append(f"La letra o letras '{partes['prefijo']}' indican el departamento de {partes['departamento']}.")
        derivacion.append(f"Los números '{partes['numeros']}' representan el identificador único del vehículo en ese departamento.")
        return derivacion
