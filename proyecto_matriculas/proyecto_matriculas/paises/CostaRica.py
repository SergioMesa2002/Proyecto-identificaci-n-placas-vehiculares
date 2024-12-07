import re
from paises.pais import Pais


class CostaRica(Pais):
    def __init__(self):
        super().__init__("Costa Rica")
        # Diccionario de tipos de vehículos basado en el prefijo
        self.tipos_vehiculos = {
            'AAA': 'Vehículos particulares',
            'TSJ': 'Taxis',
            'CMB': 'Transporte público (buses)',
            'MC': 'Motocicletas',
            'CR': 'Vehículos comerciales',
            'OF': 'Vehículos oficiales',
            'DIP': 'Vehículos diplomáticos'
        }
        # Patrón para validar el formato general de las matrículas costarricenses
        # Formato: XXX-000 o XXX-000-AA
        self.patron_matricula = re.compile(r'^[A-Z]{2,3}-\d{3,6}$')

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de Costa Rica.
        """
        # Eliminar espacios o guiones extras
        matricula = matricula.replace(' ', '').upper()

        # Validar formato general
        if not self.patron_matricula.match(matricula):
            return False, {}

        # Extraer prefijo y números
        prefijo, numeros = matricula.split('-')[0], matricula.split('-')[1]

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
