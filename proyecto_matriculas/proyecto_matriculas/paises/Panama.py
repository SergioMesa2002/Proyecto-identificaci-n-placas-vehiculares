import re
from paises.pais import Pais


class Panama(Pais):
    def __init__(self):
        super().__init__("Panamá")
        # Diccionario de tipos de vehículos basado en el prefijo
        self.tipos_vehiculos = {
            'PT': 'Transporte público (buses)',
            'MT': 'Motocicletas',
            'C': 'Vehículos comerciales',
            'OF': 'Vehículos oficiales',
            'E': 'Vehículos exonerados de impuestos',
            'D': 'Vehículos diplomáticos',
            '0': 'Vehículos particulares'  # Sin prefijo
        }
        # Patrón para validar el formato general de las matrículas panameñas
        self.patron_matricula = re.compile(r'^(PT|MT|C|OF|E|D|0)?\d{5,6}$')

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de Panamá.
        """
        # Eliminar espacios o guiones
        matricula = matricula.replace(' ', '').replace('-', '').upper()

        # Validar formato general
        if not self.patron_matricula.match(matricula):
            return False, {}

        # Extraer el prefijo (si existe) y los números
        prefijo = ''
        numeros = ''
        if matricula[:2] in self.tipos_vehiculos:  # Prefijos de dos letras
            prefijo = matricula[:2]
            numeros = matricula[2:]
        elif matricula[:1] in self.tipos_vehiculos:  # Prefijos de una letra
            prefijo = matricula[:1]
            numeros = matricula[1:]
        else:
            # Si no tiene prefijo, es un vehículo particular
            prefijo = '0'
            numeros = matricula

        # Verificar si el prefijo está en el diccionario de tipos de vehículos
        if prefijo in self.tipos_vehiculos:
            partes = {
                'prefijo': prefijo,
                'numeros': numeros,
                'tipo': self.tipos_vehiculos[prefijo]
            }
            return True, partes

        # Si el prefijo no coincide, es inválida
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
