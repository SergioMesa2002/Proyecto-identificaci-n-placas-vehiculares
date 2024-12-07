import re
from paises.pais import Pais


class RepublicaDominicana(Pais):
    def __init__(self):
        super().__init__("República Dominicana")
        # Diccionario de tipos de vehículos y sus prefijos
        self.tipos_vehiculos = {
            'A': 'Automóvil Particular',
            'AA': 'Automóvil Particular',
            'B': 'Automóvil Interurbano Público',
            'C': 'Automóvil Turístico',
            'D': 'Autobús Público Urbano',
            'F': 'Remolque',
            'G': 'Jeep',
            'L': 'Carga',
            'H': 'Ambulancia',
            'I': 'Autobús Privado',
            'T': 'Automóvil Público Urbano',
            'P': 'Autobús Turístico',
            'U': 'Máquinas Pesadas',
            'J': 'Montacargas',
            'R': 'Autobús Público Interurbano',
            'S': 'Volteo',
            'M': 'Carro Fúnebre',
            # Placas exoneradas y oficiales
            'OE': 'Ejército Nacional',
            'OF': 'Fuerza Aérea',
            'OM': 'Marina de Guerra',
            'OP': 'Policía Nacional',
            'EA': 'Exonerada Estatal',
            'EG': 'Exonerada Estatal',
            'EL': 'Exonerada Estatal',
            'EM': 'Exonerada Estatal',
            'ED': 'Exonerada Estatal',
            'EI': 'Exonerada Estatal',
            'VC': 'Consular',
            'WD': 'Diplomática',
            'OI': 'Organismos Internacionales',
            'EX': 'Exonerada',
            'YX': 'Exonerada',
            'Z': 'Exonerada',
            'NZ': 'Exonerada',
            # Otras placas
            'DD': 'Dealer',
            'PP': 'Provisional',
            'K': 'Motocicleta'
        }

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de la República Dominicana.
        """
        # Remover guiones y espacios
        matricula = matricula.replace('-', '').replace(' ', '').upper()

        # Patrón: Prefijo seguido de dígitos
        patron = r"^([A-Z]{1,2})(\d+)$"
        match = re.match(patron, matricula)
        if match:
            prefijo, numero = match.groups()
            if prefijo in self.tipos_vehiculos:
                partes = {
                    'prefijo': prefijo,
                    'numero': numero,
                    'tipo_vehiculo': self.tipos_vehiculos[prefijo]
                }
                return True, partes
        return False, {}

    def derivar_matricula(self, partes):
        """
        Deriva información adicional de la matrícula.
        """
        derivacion = []
        derivacion.append(
            f"El prefijo '{partes['prefijo']}' indica que el vehículo es de tipo '{partes['tipo_vehiculo']}'.")
        derivacion.append(f"El número '{partes['numero']}' es el identificador único del vehículo.")
        return derivacion
