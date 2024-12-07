import re
from paises.pais import Pais


class Guatemala(Pais):
    def __init__(self):
        super().__init__("Guatemala")
        # Diccionario de tipos de vehículos basado en el prefijo (letra o letras iniciales)
        self.tipos_vehiculos = {
            'A': 'Vehículo de alquiler',
            'C': 'Vehículo comercial',
            'M': 'Motocicletas y ciclomotores',
            'O': 'Vehículo oficial',
            'P': 'Vehículo privado',
            'U': 'Bus urbano',
            'CC': 'Cuerpo consular',
            'CD': 'Cuerpo diplomático',
            'MI': 'Misión internacional',
            'TC': 'Remolque'
        }
        # Patrón para validar el formato general de las matrículas guatemaltecas
        self.patron_matricula = re.compile(r'^[A-Z]{1,2}\d{4}[A-Z]{0,2}$')

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de Guatemala.
        """
        # Eliminar espacios o guiones
        matricula = matricula.replace(' ', '').replace('-', '').upper()

        # Validar formato general
        if not self.patron_matricula.match(matricula):
            return False, {}

        # Extraer prefijo (una o dos letras)
        prefijo = ''
        numeros = ''
        sufijo = ''

        # Validar prefijos de una o dos letras
        if len(matricula) > 6 and matricula[:2] in self.tipos_vehiculos:
            prefijo = matricula[:2]
            numeros = matricula[2:6]
            sufijo = matricula[6:] if len(matricula) > 6 else ''
        elif matricula[:1] in self.tipos_vehiculos:
            prefijo = matricula[:1]
            numeros = matricula[1:5]
            sufijo = matricula[5:] if len(matricula) > 5 else ''
        else:
            return False, {}

        # Verificar si el prefijo está en el diccionario de tipos de vehículos
        if prefijo in self.tipos_vehiculos:
            partes = {
                'prefijo': prefijo,
                'numeros': numeros,
                'sufijo': sufijo,
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
            f"El número '{partes['numeros']}' identifica de manera única al vehículo.",
        ]
        if partes['sufijo']:
            derivacion.append(f"El sufijo '{partes['sufijo']}' puede representar información adicional específica.")
        return derivacion
