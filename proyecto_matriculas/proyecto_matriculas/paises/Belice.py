import re
from paises.pais import Pais


class Belice(Pais):
    def __init__(self):
        super().__init__("Belice")
        # Diccionario de tipos de vehículos basado en el prefijo
        self.tipos_vehiculos = {
            'D': 'Vehículo particular',
            'C': 'Vehículo comercial',
            'T': 'Taxi',
            'G': 'Vehículo del gobierno',
            'M': 'Motocicleta'
        }
        # Patrón para validar el formato general de las matrículas beliceñas
        # Formato: X-00000
        self.patron_matricula = re.compile(r'^[DCTGM]-\d{1,5}$')

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de Belice.
        """
        # Eliminar espacios innecesarios
        matricula = matricula.strip().upper()

        # Validar formato general
        if not self.patron_matricula.match(matricula):
            return False, {}

        # Extraer prefijo y números
        prefijo, numeros = matricula.split('-')

        # Verificar si el prefijo está en el diccionario de tipos de vehículos
        if prefijo in self.tipos_vehiculos:
            partes = {
                'prefijo': prefijo,
                'numeros': numeros,
                'tipo': self.tipos_vehiculos[prefijo]
            }
            return True, partes

        # Si no coincide, es inválida
        return False, {}

    def derivar_matricula(self, partes):
        """
        Deriva información adicional de la matrícula.
        """
        derivacion = [
            f"El prefijo '{partes['prefijo']}' indica que el vehículo es de tipo '{partes['tipo']}'.",
            f"El número '{partes['numeros']}' identifica de manera única al vehículo."
        ]
        return derivacion
