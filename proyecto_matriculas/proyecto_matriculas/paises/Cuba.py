import re
from paises.pais import Pais


class Cuba(Pais):
    def __init__(self):
        super().__init__("Cuba")
        # Diccionario de tipos de vehículos basado en la letra inicial
        self.tipos_vehiculos = {
            'A': 'Vehículos de la administración',
            'C': 'Cuerpo Consular',
            'D': 'Cuerpo Diplomático',
            'E': 'Vehículo de embajada',
            'F': 'Fuerzas Armadas',
            'K': 'Personal extranjero',
            'M': 'Ministerio del Interior (Policía)',
            'T': 'Turista',
            # Letras para vehículos privados
            'P': 'Vehículo privado',
            'B': 'Vehículo privado',
            'G': 'Vehículo privado',
            'H': 'Vehículo privado',
            'J': 'Vehículo privado',
            'L': 'Vehículo privado',
            'N': 'Vehículo privado',
            'R': 'Vehículo privado',
            'U': 'Vehículo privado',
            'V': 'Vehículo privado',
            'X': 'Vehículo privado',
            'Y': 'Vehículo privado'
        }
        # Patrón para validar el formato de la matrícula cubana
        self.patron_matricula = re.compile(r'^[A-Z]\d{6}$')

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de Cuba.
        """
        # Eliminar espacios o guiones
        matricula = matricula.replace(' ', '').replace('-', '').upper()

        # Verificar longitud exacta
        if len(matricula) != 7:
            return False, {}

        # Validar formato general
        if not self.patron_matricula.match(matricula):
            return False, {}

        # Extraer la letra inicial y los números
        letra = matricula[0]
        numeros = matricula[1:]

        # Verificar si la letra inicial está en el diccionario de tipos de vehículos
        if letra in self.tipos_vehiculos:
            partes = {
                'letra': letra,
                'numeros': numeros,
                'tipo': self.tipos_vehiculos[letra]
            }
            return True, partes

        # Si la letra no coincide, es inválida
        return False, {}

    def derivar_matricula(self, partes):
        """
        Deriva información adicional de la matrícula.
        """
        derivacion = [
            f"La letra inicial '{partes['letra']}' indica que el vehículo es de tipo '{partes['tipo']}'.",
            f"El número '{partes['numeros']}' identifica de manera única al vehículo."
        ]
        return derivacion
