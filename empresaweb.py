

class Curso:
    def __init__(self, id_curso, categoria, fecha_de_comienzo, titulo, descripcion, 
                 objetivos, programa, costo, duracion_en_meses, foto, estado = "disponible"):
        self._id_curso = id_curso
        self._categoria = categoria
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
    def categoria(self):
        return self._cateoria
    
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
        
    @categoria .setter
    def categoria(self, values):
        self._categoria= values
    
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
        
class Categoria:
    def __init__(self, inicial, intermedio, avanzado):
        self.inicial = inicial
        self.intermedio = intermedio
        self.avanzado = avanzado

class Clase:
    def __init__(self, fecha, titulo, contenido, URLDrive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.URLDrive = URLDrive


class Docente:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, 
                 codigo_postal, provincia, telefono_celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email


class Estado:
    def __init__(self, disponible, no_disponible):
        self.disponible = disponible
        self.no_disponible= no_disponible


class Usuario:
    def __init__(self):
        self.activo = True
        self.password = ""
        self.password_confirmacion = ""
        self.estado = "Disponible"


class Rol:
    def __init__(self, nombre):
        self.nombre = nombre


class MedioPago:
    def __init__(self, tipo):
        self.tipo = tipo


class TarjetaCredito(MedioPago):
    def __init__(self, tipo, numero, fecha_vencimiento, codigo_seguridad):
        super().__init__(tipo)
        self.numero = numero
        self.fecha_vencimiento = fecha_vencimiento
        self.codigo_seguridad = codigo_seguridad


class TarjetaDebito(MedioPago):
    def __init__(self, tipo, numero, fecha_vencimiento):
        super().__init__(tipo)
        self.numero = numero
        self.fecha_vencimiento = fecha_vencimiento


class Transferencia(MedioPago):
    def __init__(self, tipo, datos_bancarios):
        super().__init__(tipo)
        self.datos_bancarios = datos_bancarios


class UsuarioFinal:
    def __init__(self, nombre_usuario, contrasena, estado="Activo",
                nombre, apellido, dni, 
                 fecha_nacimiento, direccion, localidad, codigo_postal, provincia, 
                 telefono_celular, email):
        super().__init__()
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.estado = estado
        self.nombre =nombre
        self.apellido= apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email


class Compra:
    def __init__(self, fecha, usuario, monto_total, medio_pago, confirmacion=False):
        self.fecha = fecha
        self.usuario = usuario
        self.monto_total = monto_total
        self.medio_pago = medio_pago
        self.confirmacion = confirmacion


class CarritoCompras:
    def __init__(self):
        self.cursos = []
        self.usuario = None
        self.confirmacion = False
        self.fecha_compra = None

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def eliminar_curso(self, curso):
        self.cursos.remove(curso)

    def confirmar_compra(self, usuario, fecha_compra, monto_total):
        self.confirmacion = True
        self.usuario = usuario
        self.fecha_compra = fecha_compra
        self.monto_total = monto_total


