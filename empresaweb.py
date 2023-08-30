

class Curso_inicial:
    def __init__(self, id_curso, fecha_de_comienzo, titulo, descripcion, 
                 objetivos, programa, costo, duracion_en_meses, foto, estado):
        self._id_curso = id_curso
        self._fecha_de_comienzo = fecha_de_comienzo
        self._titulo = titulo
        self._descripcion = descripcion
        self._objetivos = objetivos
        self._programa = programa
        self._costo = costo
        self._duracion_en_meses = duracion_en_meses
        self._foto = foto
        self._estado = estado
    
    @property
    def id_curso(self):
        return self._id_curso
    
    @property
    def fecha_de_comienzo(self):
        return self._fecha_de_comienzo
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def objetivos(self):
        return self._objetivos
    
    @property
    def programa(self):
        return self._programa
    
    @property
    def costo(self):
        return self._costo
    
    @property
    def duracion_en_meses(self):
        return self._duracion_en_meses
    
    @property
    def foto(self):
        return self._foto
    
    @property
    def estado(self):
        return self._estado
    
    @id_curso.setter
    def id_curso(self, value):
        self._id_curso = value
    
    @fecha_de_comienzo.setter
    def fecha_de_comienzo(self, value):
        self._fecha_de_comienzo = value
    
    @titulo.setter
    def titulo(self, value):
        self._titulo = value
    
    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value
    
    @objetivos.setter
    def objetivos(self, value):
        self._objetivos = value
    
    @programa.setter
    def programa(self, value):
        self._programa = value
    
    @costo.setter
    def costo(self, value):
        self._costo = value
    
    @duracion_en_meses.setter
    def duracion_en_meses(self, value):
        self._duracion_en_meses = value
    
    @foto.setter
    def foto(self, value):
        self._foto = value
    
    @estado.setter
    def estado(self, value):
        self._estado = value


curso = Curso_inicial(
    id_curso=1,
    fecha_de_comienzo="2023-09-01",
    titulo="Curso de lengua de señas",
    descripcion="Aprende lengua de señas",
    objetivos="Dominar los conceptos básicos de las señas",
    programa="Introducción a lengua de señas, entendimiento neurologico, neurolinguistica",
    costo=6000,
    duracion_en_meses=6,
    foto="imagen_curso.jpg",
    estado="activo"
)


curso.titulo = "Profesor De Lengua De Señas"
curso.costo = "$ 9000"

print(curso.titulo)
print(curso.costo)
   
        
        
     
     