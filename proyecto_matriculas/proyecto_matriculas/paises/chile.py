import re
from paises.pais import Pais

class Chile(Pais):
    def __init__(self):
        super().__init__("Chile")
        # Diccionario de regiones y combinaciones asignadas (vigente de 1995 a 2007)
        self.regiones = {
            "Arica y Parinacota": ["AB", "AC"],
            "Tarapacá": ["AD", "AE", "AF"],
            "Antofagasta": ["AG", "AH", "AI"],
            "Atacama": ["AJ", "AK"],
            "Coquimbo": ["AL", "AM", "AN"],
            "Valparaíso": ["AO", "AP", "AQ"],
            "O'Higgins": ["AR", "AS"],
            "Maule": ["AT", "AU"],
            "Ñuble y Biobío": ["AV", "AW"],
            "Araucanía": ["AX", "AY"],
            "Los Ríos y Los Lagos": ["AZ", "BA", "BB"],
            "Aysén": ["BC", "BD"],
            "Magallanes": ["BE"],
            "Metropolitana": ["BF", "BG", "BH"],
        }

    def validar_matricula(self, matricula):
        """
        Valida si una matrícula es válida en Chile.
        :param matricula: Matrícula a validar.
        :return: Tuple (bool, dict). El booleano indica si es válida, el dict contiene detalles.
        """
        # Patrones para diferentes tipos de matrícula
        patrones = {
            "Particular": r"^[A-Z]{2} [A-Z]{2} \d{2}$",  # Ejemplo: AB CD 12
            "Transporte Público": r"^TX [A-Z]{2} \d{2}$",  # Ejemplo: TX AB 34
            "Oficial": r"^GO [A-Z]{2} \d{2}$",  # Ejemplo: GO CD 56
            "Diplomático": r"^CC \d{3}$",  # Ejemplo: CC 123
            "Provisional": r"^PRV [A-Z]{2} \d{2}$",  # Ejemplo: PRV AB 80
        }

        for tipo, patron in patrones.items():
            if re.match(patron, matricula):
                # Extraer detalles según el tipo
                if tipo == "Diplomático":
                    return True, {
                        "matricula": matricula,
                        "tipo": "Vehículo Diplomático",
                        "region": "No aplica",
                        "servicio": "Vehículos Diplomáticos"
                    }
                else:
                    # Identificar región con base en las letras iniciales
                    letras_iniciales = matricula.split()[0]
                    region = "Desconocida"
                    region_comentario = ""

                    for reg, combinaciones in self.regiones.items():
                        if letras_iniciales in combinaciones:
                            region = reg
                            region_comentario = (
                                "El análisis regional es complementario y estuvo vigente entre 1995 y 2007."
                            )
                            break

                    return True, {
                        "matricula": matricula,
                        "tipo": tipo,
                        "region": region,
                        "comentario": region_comentario,
                        "servicio": "Vehículos Particulares" if tipo == "Particular" else tipo
                    }

        return False, {}

    def derivar_matricula(self, partes):
        """
        Realiza una derivación gramatical de la matrícula.
        :param partes: Diccionario con los detalles de la matrícula.
        :return: Lista con los pasos de la derivación gramatical.
        """
        matricula = partes["matricula"]
        pasos = ["<matricula>", "<chile>"]

        if partes["tipo"] == "Diplomático":
            pasos.append("CC <numeros>")
            pasos.append(f"CC {matricula.split()[-1]}")
        else:
            pasos.append("<letras> <letras> <numeros>")
            letras = matricula.split()[:2]
            numeros = matricula.split()[-1]
            pasos.append(f"{' '.join(letras)} <numeros>")
            for i in range(len(numeros)):
                pasos.append(f"{' '.join(letras)} {numeros[:i+1]}<numeros>")
            pasos[-1] = pasos[-1].replace("<numeros>", "")

        return pasos
