from datetime import datetime
# ==========================================
# MODELOS INICIALES DEL SISTEMA RURAL-PE
# ==========================================
# Clase principal Persona
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    #Getter: permitira consultar el nombre
    @property
    def nombre(self):
        return self.__nombre

    #Setter: permitira modificar el nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if not nuevo_nombre.string():
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre=nuevo_nombre

    def mostrar_datos(self):
        return self.__nombre

# Clase Paciente: hereda de Persona
class Paciente(Persona):
    def __init__(self, nombre, codigo_paciente):
        super().__init__(nombre)
        self.__codigo_paciente = codigo_paciente

    #Getter: permitira consultar el codigo
    @property
    def codigo_paciente(self):
        return self.__codigo_paciente
    
    def mostrar_datos(self):
        return f"Paciente: {self.nombre} - Código: {self.codigo_paciente}"

# Clase Medico: hereda de Persona
class Medico(Persona):
    def __init__(self, nombre, codigo_medico, especialidad):
        super().__init__(nombre)
        self.__codigo_medico = codigo_medico
        self.__especialidad = especialidad

    # Getter: consultar código del médico
    @property
    def codigo_medico(self):
        return self.__codigo_medico

    # Getter: consultar especialidad
    @property
    def especialidad(self):
        return self.__especialidad

    # Setter: modificar especialidad
    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        if not nueva_especialidad.strip():
            raise ValueError("La especialidad no puede estar vacia")
        self.__especialidad=nueva_especialidad

    def mostrar_datos(self):
        return f"Médico: {self.nombre} - Especialidad: {self.especialidad}"

# Clase CentroSalud
class CentroSalud:
    def __init__(self, nombre, direccion, distrito):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__distrito = distrito

    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccion(self):
        return self.__direccion

    @property
    def distrito(self):
        return self.__distrito
    
    def mostrar_informacion(self):
        return f"{self.nombre} - {self.distrito}"

# Clase AreaAtencion
class AreaAtencion:
    def __init__(self, codigo, nombre, piso, puerta):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__piso = piso
        self.__puerta = puerta

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def piso(self):
        return self.__piso

    @property
    def puerta(self):
        return self.__puerta
    
    def mostrar_ubicacion(self):
        return f"{self.nombre} - Piso {self.piso} - Puerta {self.puerta}"

# Clase CitaMedica
class CitaMedica:
    def __init__(self, codigo, paciente, medico, centro, area, fecha, hora_inicio, hora_fin):
        self.__codigo = codigo
        self.__paciente = paciente
        self.__medico = medico
        self.__centro = centro
        self.__area = area
        self.__estado = "Programada"

        #Registrar y validar la fecha y el horario
        self.modificar(fecha, hora_inicio, hora_fin)

    # Getters para consultar los atributos
    @property
    def codigo(self):
        return self.__codigo

    @property
    def paciente(self):
        return self.__paciente

    @property
    def medico(self):
        return self.__medico

    @property
    def centro(self):
        return self.__centro

    @property
    def area(self):
        return self.__area

    @property
    def fecha(self):
        return self.__fecha

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @property
    def hora_fin(self):
        return self.__hora_fin

    @property
    def estado(self):
        return self.__estado

    #Modificar y validar fechay horario
    def modificar(self, fecha, hora_inicio, hora_fin):
        fecha_validada= datetime.strptime(fecha, "%Y-%m-%d")
        inicio=datetime.strptime(hora_inicio, "%H:%M")
        fin=datetime.strptime(hora_fin, "%H:%M")

        if fin <= inicio:
            raise ValueError("La hora final debe ser posterior a la inicial")
        self.__fecha = fecha_validada.strftime("%Y-%m-%d")
        self.__hora_inicio = inicio.strftime("%H:%M")
        self.__hora_fin = fin.strftime("%H:%M")

    def cancelar(self):
        self.__estado = "Cancelada"

    def mostrar_detalle(self):
        return (
            f"Cita: {self.codigo}\n"
            f"Paciente: {self.paciente.nombre}\n"
            f"Médico: {self.medico.nombre}\n"
            f"Centro: {self.centro.nombre}\n"
            f"Area: {self.area.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Horario: {self.hora_inicio} - {self.hora_fin}\n"
            f"Estado: {self.estado}"
        )

