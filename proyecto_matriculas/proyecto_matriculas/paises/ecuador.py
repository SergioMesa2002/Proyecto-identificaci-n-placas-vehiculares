import re

class Ecuador:
    def __init__(self):
        self.nombre = "Ecuador"
        self.regiones = {
            'A': 'Azuay',
            'B': 'Bolívar',
            'C': 'Carchi',
            'E': 'Esmeraldas',
            'G': 'Guayas',
            'H': 'Chimborazo',
            'I': 'Imbabura',
            'J': 'Santo Domingo de los Tsáchilas',
            'K': 'Sucumbíos',
            'L': 'Loja',
            'M': 'Manabí',
            'N': 'Napo',
            'O': 'El Oro',
            'P': 'Pichincha',
            'Q': 'Orellana',
            'R': 'Los Ríos',
            'S': 'Pastaza',
            'T': 'Tungurahua',
            'U': 'Cañar',
            'V': 'Morona-Santiago',
            'W': 'Galápagos',
            'X': 'Cotopaxi',
            'Z': 'Zamora-Chinchipe'
        }

    def validar_matricula(self, matricula):
        # Definición de patrones según tipo de vehículo
        patrones = {
            'Particular': r'^[A-Z]{3}-\d{4}$',
            'Público/Comercial': r'^U[A-Z]{2}-\d{4}$',
            'Gubernamental': r'^[A-Z]{3}-\d{4}$',
            'Diplomático': r'^CD-\d{4}$'
        }

        for tipo, patron in patrones.items():
            if re.match(patron, matricula):
                region = self.regiones.get(matricula[0], "Desconocida")
                return True, {
                    "matricula": matricula,
                    "tipo": tipo,
                    "region": region
                }

        return False, {}

    def derivar_matricula(self, partes):
        # Derivación gramatical por la izquierda
        matricula = partes["matricula"]
        pasos = ["<matricula>"]

        # Identificar el tipo de matrícula
        if partes["tipo"] == "Diplomático":
            pasos.append("<diplomatico>")
            pasos.append("CD-<numeros>")
        elif partes["tipo"] == "Público/Comercial":
            pasos.append("<comercial>")
            pasos.append("U<letras>-<numeros>")
            pasos.append(f"U{matricula[1:3]}-<numeros>")
        else:
            pasos.append("<general>")
            pasos.append("<letras>-<numeros>")
            pasos.append(f"{matricula[:3]}-<numeros>")

        # Derivar números
        numeros = matricula.split('-')[-1]
        for i in range(len(numeros)):
            pasos.append(f"{matricula[:4]}{numeros[:i+1]}<numeros>")

        pasos[-1] = pasos[-1].replace("<numeros>", "")
        return pasos
