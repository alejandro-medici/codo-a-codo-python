class Persona():
    """

    Clase persona

    """
    
    def __init__(self, name="there", surname="something"):
        """

        De esta manera inicializamos el objeto, asegurandonos que sus valores
        tiene consistencia aun no asignandole un valor/estado, este tiene que 
        garantizar tener uno.

        """
        self.nombre = name
        self.apellido = surname

    def __str__(self):
        """

        Este metodo es llamado cuando un objeto tiene que ser convertido a
        str, como el caso del uso de la funcion print

        """
        return "soy objeto persona con nombre " + self.nombre

    def comoTeLlamas(self):
        """

        imprime nombre

        """
        print("Me llamo: " + self.nombre)

    @classmethod
    def funcname(cls, parameter_list):
        """
        docstring
        """
        pass

    @staticmethod
    def func2name(x,y):
        """
        docstring
        """
        print(x)