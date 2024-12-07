
class Pais:
    def __init__(self, nombre):
        self.nombre = nombre

    def validar_matricula(self, matricula):
        """
        Este método debe implementarse en las subclases.
        """
        raise NotImplementedError("Este método debe implementarse en las subclases.")

    def derivar_matricula(self, partes):
        """
        Implementación predeterminada del método derivar_matricula.
        Puede ser sobreescrito por las subclases.
        """
        return ["<matricula>", f"<{self.nombre.lower()}>"]
