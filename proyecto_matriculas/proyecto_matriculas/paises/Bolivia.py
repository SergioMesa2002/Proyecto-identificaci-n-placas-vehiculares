import re
from paises.pais import Pais

class Bolivia(Pais):
    def __init__(self):
        super().__init__("Bolivia")
        # Diccionario de departamentos con rango de números iniciales
        self.departamentos = {
            "La Paz": (1000, 1999),
            "Santa Cruz": (2000, 2999),
            "Cochabamba": (3000, 3999),
            "Oruro": (4000, 4999),
            "Potosí": (5000, 5999),
            "Tarija": (6000, 6999),
            "Chuquisaca": (7000, 7999),
            "Beni": (8000, 8999),
            "Pando": (9000, 9999)
        }
        # Tipos de servicio por letra final
        self.tipos_servicio = {
            "T": "Transporte Público",
            "O": "Vehículos Oficiales",
            "D": "Vehículos Diplomáticos",
        }

    def validar_matricula(self, matricula):
        """
        Valida si una matrícula es válida en Bolivia.
        :param matricula: Matrícula a validar (ejemplo: '1234-ABC', '1234-AAT', etc.).
        :return: Tuple (bool, dict). El booleano indica si es válida, el dict contiene detalles.
        """
        # Patrones para diferentes tipos de matrícula
        patrones = {
            "Particular": r"^\d{4}-[A-Z]{3}$",  # Ejemplo: 1234-ABC
            "Público": r"^\d{4}-[A-Z]{2}T$",   # Ejemplo: 1234-AAT
            "Oficial": r"^\d{4}-[A-Z]{2}O$",   # Ejemplo: 1234-AAO
            "Diplomático": r"^CD-\d{3}$"      # Ejemplo: CD-123
        }

        for tipo, patron in patrones.items():
            if re.match(patron, matricula):
                # Extraer los datos relevantes según el tipo
                if tipo == "Diplomático":
                    return True, {
                        "matricula": matricula,
                        "tipo": "Vehículo Diplomático",
                        "departamento": "No aplica",
                        "servicio": "Vehículos Diplomáticos"
                    }
                else:
                    # Extraer el número inicial y la letra final
                    numero_inicial = int(matricula.split('-')[0])
                    letra_final = matricula[-1]

                    # Determinar el departamento
                    departamento = "Desconocido"
                    for depto, rango in self.departamentos.items():
                        if rango[0] <= numero_inicial <= rango[1]:
                            departamento = depto
                            break

                    # Determinar el servicio
                    servicio = self.tipos_servicio.get(letra_final, "Vehículos Particulares")

                    return True, {
                        "matricula": matricula,
                        "tipo": tipo,
                        "departamento": departamento,
                        "servicio": servicio
                    }

        return False, {}

    def derivar_matricula(self, partes):
        """
        Realiza una derivación gramatical de la matrícula.
        :param partes: Diccionario con los detalles de la matrícula.
        :return: Lista con los pasos de la derivación gramatical.
        """
        matricula = partes["matricula"]
        pasos = ["<matricula>", "<bolivia>"]

        if partes["tipo"] == "Diplomático":
            pasos.append("CD-<numeros>")
            pasos.append(f"CD-{matricula.split('-')[-1]}")
        else:
            pasos.append("<numeros>-<letras>")
            numeros = matricula.split('-')[0]
            letras = matricula.split('-')[1]
            pasos.append(f"{numeros}-<letras>")
            for i in range(len(letras)):
                pasos.append(f"{numeros}-{letras[:i+1]}<letras>")
            pasos[-1] = pasos[-1].replace("<letras>", "")

        return pasos
