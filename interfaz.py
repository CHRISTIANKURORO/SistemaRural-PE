# ==========================================
# INTERFAZ GRAFICA - SISTEMA RURAL-PE
# ==========================================
import tkinter as tk
from tkinter import ttk
from modelos import Paciente, Medico, CentroSalud, AreaAtencion
from gestor import GestorCitas

# Datos ficticios para las pruebas
pacientes = {
    "P001": Paciente("Ana Torres", "P001"),
    "P002": Paciente("Pedro Ruiz", "P002")
}

medicos = {
    "M001": Medico("Luis Perez", "M001", "Medicina General")
}

centro = CentroSalud(
    "Centro de Salud Rural Santa Rosa",
    "Av. Principal s/n",
    "Chugur"
)

area = AreaAtencion("A001", "Medicina General", 1, 1)

gestor = GestorCitas()
contador_citas = 1

# Crear la ventana principal
ventana = tk.Tk()

ventana.title("SistemaRural-PE - Gestion de Citas")
ventana.geometry("1000x750")
ventana.resizable(False, False)

# Titulo principal
titulo = tk.Label(
    ventana,
    text="SISTEMA RURAL-PE",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=15)

subtitulo = tk.Label(
    ventana,
    text="Centro de Salud Rural Santa Rosa - Chugur, Cajamarca",
    font=("Arial", 11)
)
subtitulo.pack()

# Crear un marco para organizar el contenido
marco = ttk.Frame(ventana, padding=20)
marco.pack(fill="both", expand=True)

# Mensaje de bienvenida
bienvenida = ttk.Label(
    marco,
    text="Sistema de Gestion de Citas Medicas",
    font=("Arial", 15, "bold")
)
bienvenida.pack(pady=20)

# Formulario para registrar una cita
formulario = ttk.LabelFrame(
    marco,
    text="Registro de citas",
    padding=15
)
formulario.pack(pady=10)

# Campo para el codigo del paciente
ttk.Label(formulario, text="Codigo del paciente:").grid(
    row=0, column=0, padx=10, pady=8, sticky="w"
)
entrada_paciente = ttk.Entry(formulario, width=25)
entrada_paciente.grid(row=0, column=1, padx=10, pady=8)

# Campo para el codigo del medico
ttk.Label(formulario, text="Codigo del medico:").grid(
    row=1, column=0, padx=10, pady=8, sticky="w"
)
entrada_medico = ttk.Entry(formulario, width=25)
entrada_medico.grid(row=1, column=1, padx=10, pady=8)

# Campo para la fecha
ttk.Label(formulario, text="Fecha (AAAA-MM-DD):").grid(
    row=2, column=0, padx=10, pady=8, sticky="w"
)
entrada_fecha = ttk.Entry(formulario, width=25)
entrada_fecha.grid(row=2, column=1, padx=10, pady=8)

# Campo para la hora de inicio
ttk.Label(formulario, text="Hora de inicio (HH:MM):").grid(
    row=3, column=0, padx=10, pady=8, sticky="w"
)
entrada_inicio = ttk.Entry(formulario, width=25)
entrada_inicio.grid(row=3, column=1, padx=10, pady=8)

# Campo para la hora final
ttk.Label(formulario, text="Hora final (HH:MM):").grid(
    row=4, column=0, padx=10, pady=8, sticky="w"
)
entrada_fin = ttk.Entry(formulario, width=25)
entrada_fin.grid(row=4, column=1, padx=10, pady=8)


# Funcion para registrar una cita desde la interfaz
def registrar_cita():
    global contador_citas

    try:
        codigo_paciente = entrada_paciente.get().strip()
        codigo_medico = entrada_medico.get().strip()
        fecha = entrada_fecha.get().strip()
        hora_inicio = entrada_inicio.get().strip()
        hora_fin = entrada_fin.get().strip()

        paciente = pacientes[codigo_paciente]
        medico = medicos[codigo_medico]

        codigo_cita = f"C{contador_citas:03d}"

        cita = gestor.registrar_cita(
            codigo_cita,
            paciente,
            medico,
            centro,
            area,
            fecha,
            hora_inicio,
            hora_fin
        )

        contador_citas += 1
        actualizar_tabla()
        resultado.config(
            text=f"Cita {cita.codigo} registrada correctamente",
            foreground="green"
        )

    except KeyError:
        resultado.config(
            text="Codigo de paciente o medico no valido",
            foreground="red"
        )

    except ValueError as error:
        resultado.config(
            text=str(error),
            foreground="red"
        )


# Funcion para mostrar las citas registradas
def actualizar_tabla():
    # Limpiar los datos anteriores de la tabla
    for fila in tabla.get_children():
        tabla.delete(fila)

    # Obtener las citas registradas
    citas = gestor.consultar_citas()

    # Mostrar cada cita en la tabla
    for cita in citas:
        tabla.insert(
            "",
            "end",
            values=(
                cita.codigo,
                cita.paciente.nombre,
                cita.medico.nombre,
                cita.fecha,
                f"{cita.hora_inicio} - {cita.hora_fin}",
                cita.estado
            )
        )


# Funcion para consultar los detalles de una cita seleccionada
def consultar_cita():
    seleccion = tabla.selection()

    if not seleccion:
        resultado.config(
            text="Selecciona una cita de la tabla",
            foreground="red"
        )
        return

    datos = tabla.item(seleccion[0], "values")
    codigo = datos[0]

    try:
        cita = gestor.buscar_cita(codigo)

        resultado.config(
            text=(
                f"{cita.codigo} | {cita.paciente.nombre} | "
                f"{cita.medico.nombre} | {cita.fecha} | "
                f"{cita.hora_inicio}-{cita.hora_fin} | "
                f"{cita.estado}"
            ),
            foreground="blue"
        )

    except ValueError as error:
        resultado.config(
            text=str(error),
            foreground="red"
        )


# Funcion para modificar una cita seleccionada
def modificar_cita():
    seleccion = tabla.selection()

    if not seleccion:
        resultado.config(
            text="Selecciona una cita de la tabla",
            foreground="red"
        )
        return

    datos = tabla.item(seleccion[0], "values")
    codigo = datos[0]

    try:
        fecha = entrada_fecha.get().strip()
        hora_inicio = entrada_inicio.get().strip()
        hora_fin = entrada_fin.get().strip()

        cita = gestor.modificar_cita(
            codigo,
            fecha,
            hora_inicio,
            hora_fin
        )

        actualizar_tabla()

        resultado.config(
            text=f"Cita {cita.codigo} modificada correctamente",
            foreground="green"
        )

    except ValueError as error:
        resultado.config(
            text=str(error),
            foreground="red"
        )

# Funcion para cancelar una cita seleccionada
def cancelar_cita():
    seleccion = tabla.selection()

    if not seleccion:
        resultado.config(
            text="Selecciona una cita de la tabla",
            foreground="red"
        )
        return

    datos = tabla.item(seleccion[0], "values")
    codigo = datos[0]

    try:
        cita = gestor.cancelar_cita(codigo)

        actualizar_tabla()

        resultado.config(
            text=f"Cita {cita.codigo} cancelada correctamente",
            foreground="green"
        )

    except ValueError as error:
        resultado.config(
            text=str(error),
            foreground="red"
        )

# Boton para registrar
boton_registrar = ttk.Button(
    formulario,
    text="Registrar cita",
    command=registrar_cita
)
boton_registrar.grid(
    row=5, column=0, columnspan=2, pady=15
)
# Boton para consultar una cita seleccionada
boton_consultar = ttk.Button(
    formulario,
    text="Consultar cita",
    command=consultar_cita
)
boton_consultar.grid(
    row=7, column=0, columnspan=2, pady=5
)
# Boton para modificar una cita
boton_modificar = ttk.Button(
    formulario,
    text="Modificar cita",
    command=modificar_cita
)
boton_modificar.grid(
    row=8, column=0, columnspan=2, pady=5
)
# Boton para cancelar una cita
boton_cancelar = ttk.Button(
    formulario,
    text="Cancelar cita",
    command=cancelar_cita
)
boton_cancelar.grid(
    row=9, column=0, columnspan=2, pady=5
)
# Mensaje del resultado
resultado = ttk.Label(formulario, text="")
resultado.grid(row=6, column=0, columnspan=2, pady=5)


# Tabla para visualizar las citas
tabla = ttk.Treeview(
    marco,
    columns=("codigo", "paciente", "medico", "fecha", "horario", "estado"),
    show="headings",
    height=6
)

tabla.heading("codigo", text="Codigo")
tabla.heading("paciente", text="Paciente")
tabla.heading("medico", text="Medico")
tabla.heading("fecha", text="Fecha")
tabla.heading("horario", text="Horario")
tabla.heading("estado", text="Estado")

tabla.pack(pady=10, fill="x")

# Boton inicial
boton_salir = ttk.Button(
    marco,
    text="Salir",
    command=ventana.destroy
)
boton_salir.pack(pady=15)

# Mantener la ventana abierta
ventana.mainloop()
