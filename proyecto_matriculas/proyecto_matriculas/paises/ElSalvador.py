import re
from paises.pais import Pais

class ElSalvador(Pais):
    def __init__(self):
        super().__init__("El Salvador")
        self.tipos_vehiculo = {
            'P': 'Vehículo Particular',
            'A': 'Vehículo de Alquiler (Taxi)',
            'C': 'Vehículo Comercial',
            'U': 'Transporte Urbano',
            'M': 'Motocicleta',
            'CD': 'Cuerpo Diplomático',
            'CC': 'Cuerpo Consular',
            'MI': 'Misión Internacional',
            'O': 'Organización Internacional',
            'E': 'Vehículo del Estado',
            'N': 'Institución Gubernamental',
            'D': 'Vehículo para Discapacitados',
            'T': 'Transporte Turístico',
            'R': 'Remolque',
            'S': 'Servicio Público',
            'Z': 'Vehículo Agrícola',
            'X': 'Vehículo Especial',
            'L': 'Alquiler sin Conductor',
            'F': 'Vehículo de Bomberos'
        }

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de El Salvador.
        """
        matricula = matricula.upper().strip()
        for prefijo in sorted(self.tipos_vehiculo.keys(), key=len, reverse=True):
            if matricula.startswith(prefijo):
                numeros = matricula[len(prefijo):].strip()
                if re.fullmatch(r'\d+', numeros):
                    partes = {
                        'prefijo': prefijo,
                        'numeros': numeros,
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
