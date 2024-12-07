import re
from paises.pais import Pais

class Mexico(Pais):
    def __init__(self):
        super().__init__("México")
        # Diccionario de rangos de series por estado
        self.rangos_series = {
            'Aguascalientes': ('AAA', 'AFZ'),
            'Baja California': ('BAA', 'CYZ'),
            'Baja California Sur': ('DAA', 'DEZ'),
            'Campeche': ('DFA', 'DKZ'),
            'Chihuahua': ('DTA', 'ETZ'),
            'Chiapas': ('DSA', 'DSZ'),
            'CDMX': ('A01', 'Z99'),
            'Coahuila': ('EUA', 'FPZ'),
            'Colima': ('FRA', 'FWZ'),
            'Durango': ('FXA', 'GFZ'),
            'Guanajuato': ('GGA', 'GYZ'),
            'Guerrero': ('GZA', 'HFZ'),
            'Hidalgo': ('HGA', 'HRZ'),
            'Jalisco': ('HSA', 'LFZ'),
            'Estado de México': ('LGA', 'PEZ'),
            'Michoacán': ('PFA', 'PUZ'),
            'Morelos': ('PVA', 'RDZ'),
            'Nayarit': ('REA', 'RJZ'),
            'Nuevo León': ('RKA', 'TGZ'),
            'Oaxaca': ('THA', 'TMZ'),
            'Puebla': ('TNA', 'UJZ'),
            'Querétaro': ('UKA', 'UPZ'),
            'Quintana Roo': ('URA', 'UVZ'),
            'San Luis Potosí': ('UWA', 'VEZ'),
            'Sinaloa': ('VFA', 'VSZ'),
            'Sonora': ('VTA', 'WKZ'),
            'Tabasco': ('WLA', 'WWZ'),
            'Tamaulipas': ('WXA', 'XSZ'),
            'Tlaxcala': ('XTA', 'XXZ'),
            'Veracruz': ('XYA', 'YVZ'),
            'Yucatán': ('YWA', 'ZCZ'),
            'Zacatecas': ('ZDA', 'ZHZ')
        }
        # Patrones de placas por tipo de vehículo
        self.patrones_tipos = {
            'Automóvil Particular': re.compile(r'^[A-Z]{3}-\d{4}$'),
            'Camión Privado': re.compile(r'^[A-Z]{2}-\d{5}$'),
            'Motocicleta': re.compile(r'^Y\d{3}[A-Z]{2}$'),
        }

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde al formato de México y determina el tipo de vehículo.
        """
        matricula = matricula.replace(' ', '').upper()

        for tipo, patron in self.patrones_tipos.items():
            if patron.match(matricula):
                if tipo == 'Automóvil Particular':
                    serie_letras = matricula[:3]
                    numero = matricula[4:]
                elif tipo == 'Camión Privado':
                    serie_letras = matricula[:2]
                    numero = matricula[3:]
                elif tipo == 'Motocicleta':
                    serie_letras = matricula[0]
                    numero = matricula[1:]
                else:
                    continue

                for estado, (inicio, fin) in self.rangos_series.items():
                    # Convertir a listas para comparación segura
                    if inicio <= serie_letras <= fin:
                        partes = {
                            'serie_letras': serie_letras,
                            'numero': numero,
                            'estado': estado,
                            'tipo': tipo
                        }
                        return True, partes
        return False, {}

    def derivar_matricula(self, partes):
        """
        Deriva información adicional de la matrícula.
        """
        derivacion = [
            f"La serie de letras '{partes['serie_letras']}' indica que el vehículo está registrado en el estado de {partes['estado']}.",
            f"El número '{partes['numero']}' es el identificador único del vehículo en ese estado.",
            f"El tipo de vehículo es '{partes['tipo']}'."
        ]
        return derivacion
