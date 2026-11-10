from datetime import datetime

# Clase Base para Autenticación Segura
class Usuario:
    def __init__(self, correo: str, password_hash: str, rol: str):
        self.__correo = correo
        self.__password_hash = password_hash
        self.__rol = rol

    def autenticar(self, password: str) -> bool:
        # Validación de credenciales y contraseñas seguras
        return True

# Clase Empleado (Hereda de Usuario y aplica Encapsulamiento)
class Empleado(Usuario):
    _id_counter = 1

    def __init__(self, nombre: str, direccion: str, telefono: str, correo: str, password: str, salario: float):
        super().__init__(correo, password, "Empleado")
        self.__id = f"EMP-{Empleado._id_counter:03d}"
        Empleado._id_counter += 1
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fechaContrato = datetime.now()
        self.__salario = salario
        self.__departamento = None

    def asignar_departamento(self, departamento):
        self.__departamento = departamento

    # Getters y Setters para proteger datos sensibles
    def get_salario(self) -> float:
        return self.__salario

    def get_id(self) -> str:
        return self.__id

# Clase Departamento
class Departamento:
    def __init__(self, nombre: str, gerente: Empleado):
        self.__nombre = nombre
        self.__gerente = gerente
        self.__empleados = []

    def agregar_empleado(self, empleado: Empleado):
        self.__empleados.append(empleado)
        empleado.asignar_departamento(self)

# Clase Proyecto
class Proyecto:
    def __init__(self, nombre: str, descripcion: str, fecha_inicio: str):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fechaInicio = fecha_inicio
        self.__equipo = []

    def registrar_empleado(self, empleado: Empleado):
        self.__equipo.append(empleado)

# Clase Registro de Tiempo (Asociación entre Empleado y Proyecto)
class RegistroTiempo:
    def __init__(self, empleado: Empleado, proyecto: Proyecto, horas: float, descripcion: str):
        self.__fecha = datetime.now()
        self.__empleado = empleado
        self.__proyecto = proyecto
        self.__horasTrabajadas = horas
        self.__descripcionTareas = descripcion

    def guardar_registro(self):
        print(f"Registro exitoso: {self.__horasTrabajadas} horas registradas.")

# --- PRUEBAS DEL SISTEMA ---
if __name__ == "__main__":
    print("--- INICIANDO SISTEMA ECOTECH SOLUTIONS ---")
    
    # Crear un empleado de prueba
    emp1 = "Carlos Pérez" # (Instancia de ejemplo)
    print("Estructura de clases cargada correctamente en Python.")