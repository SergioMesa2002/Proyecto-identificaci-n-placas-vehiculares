import re
from paises.pais import Pais

class Argentina(Pais):
    def __init__(self):
        super().__init__("Argentina")
        self.provincias = {
            'A': 'Salta',
            'B': 'Buenos Aires',
            'C': 'Ciudad Autónoma de Buenos Aires',
            'D': 'San Luis',
            'E': 'Entre Ríos',
            'F': 'La Rioja',
            'G': 'Santiago del Estero',
            'H': 'Chaco',
            'J': 'San Juan',
            'K': 'Catamarca',
            'L': 'La Pampa',
            'M': 'Mendoza',
            'N': 'Misiones',
            'P': 'Formosa',
            'Q': 'Neuquén',
            'R': 'Río Negro',
            'S': 'Santa Fe',
            'T': 'Tucumán',
            'U': 'Chubut',
            'V': 'Tierra del Fuego',
            'W': 'Corrientes',
            'X': 'Córdoba',
            'Y': 'Jujuy',
            'Z': 'Santa Cruz'
        }

    def validar_matricula(self, matricula):
        """
        Valida si la matrícula ingresada corresponde a alguno de los formatos de Argentina.
        Formatos:
        - Actual (desde 2016): AA 123 BB
        - Anterior (1995-2016): AAA 123
        - Provincial (hasta 1994): A 123456
        """
        patrones = {
            'mercosur': re.compile(r'^[A-Z]{2} \d{3} [A-Z]{2}$'),
            'nacional': re.compile(r'^[A-Z]{3} \d{3}$'),
            'provincial': re.compile(r'^[A-z] \d{6}$')
        }
        for tipo, patron in patrones.items():
            if patron.match(matricula):
                partes = self.extraer_partes(matricula, tipo)
                return True, partes
        return False, {}

    def extraer_partes(self, matricula, tipo):
        """
        Extrae las partes de la matrícula según su tipo.
        """
        if tipo == 'mercosur':
            letras1 = matricula[:2]
            numeros = matricula[3:6]
            letras2 = matricula[7:]
            return {
                'tipo': 'Mercosur',
                'letras1': letras1,
                'numeros': numeros,
                'letras2': letras2
            }
        elif tipo == 'nacional':
            letras = matricula[:3]
            numeros = matricula[4:]
            return {
                'tipo': 'Nacional',
                'letras': letras,
                'numeros': numeros
            }
        elif tipo == 'provincial':
            letra = matricula[0]
            numeros = matricula[2:]
            return {
                'tipo': 'Provincial',
                'letra': letra,
                'numeros': numeros,
                'provincia': self.provincias.get(letra, 'Desconocida')
            }

    def derivar_matricula(self, partes):
        """
        Deriva información adicional de la matrícula.
        """
        derivacion = []
        if partes['tipo'] == 'Mercosur':
            derivacion.append(f"Formato Mercosur: {partes['letras1']} {partes['numeros']} {partes['letras2']}.")
        elif partes['tipo'] == 'Nacional':
            derivacion.append(f"Formato Nacional: {partes['letras']} {partes['numeros']}.")
        elif partes['tipo'] == 'Provincial':
            derivacion.append(f"Formato Provincial: Letra '{partes['letra']}' indica la provincia de {partes['provincia']}.")
        return derivacion
