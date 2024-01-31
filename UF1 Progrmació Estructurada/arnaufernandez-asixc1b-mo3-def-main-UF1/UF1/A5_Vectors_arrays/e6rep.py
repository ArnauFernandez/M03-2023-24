# Definir una lista con la información de los meses (número de días y nombre del mes)
info_meses = [
    {"dies": 31, "nom": "gener"},
    {"dies": 28, "nom": "febrer"},
    {"dies": 31, "nom": "març"},
    {"dies": 30, "nom": "abril"},
    {"dies": 31, "nom": "maig"},
    {"dies": 30, "nom": "juny"},
    {"dies": 31, "nom": "juliol"},
    {"dies": 31, "nom": "agost"},
    {"dies": 30, "nom": "setembre"},
    {"dies": 31, "nom": "octubre"},
    {"dies": 30, "nom": "novembre"},
    {"dies": 31, "nom": "desembre"}
]

while True:
    # Solicitar al usuario un número de mes
    num_mes = int(input("Introdueix un número de mes (1-12): "))

    # Validar que el número de mes esté entre 1 y 12
    if 1 <= num_mes <= 12:
        break
    else:
        print("Error: Introdueix un número de mes vàlid (entre 1 i 12).")

# Obtener la información del mes seleccionado
mes_seleccionat = info_meses[num_mes - 1]

# Mostrar en pantalla la cantidad de días y el nombre del mes
print(f"{mes_seleccionat['nom']} té {mes_seleccionat['dies']} dies.")
