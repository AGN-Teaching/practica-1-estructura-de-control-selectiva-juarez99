def calcular_sueldo_neto():
    # Solicitar datos de entrada
    salario_hora = float(input("Ingrese su salario por hora: "))
    horas_trabajadas = float(input("Ingrese el número de horas trabajadas en el mes: "))

    # Preguntar por participación en caja de ahorros
    print("¿Seleccione su tipo de participación en la caja de ahorros? ")
    print("1. No participar")
    print("2. Cuota fija ($1,000)")
    print("3. 3% del sueldo bruto")
    print("4. 5% del sueldo bruto")
    opcion_caja = int(input("Opción: "))

    # Preguntar por participación en ahorro solidario
    print("Seleccione su tipo de participación en el ahorro solidario:")
    print("1. No participar")
    print("2. 1% del sueldo bruto")
    print("3. 2% del sueldo bruto")
    opcion_ahorro = int(input("Opción: "))

    # Calcular sueldo bruto
    if horas_trabajadas <= 160:
        sueldo_bruto = salario_hora * horas_trabajadas
    elif horas_trabajadas <= 200:
        sueldo_bruto = (160 * salario_hora) + ((horas_trabajadas - 160) * salario_hora * 1.5)
    else:
        sueldo_bruto = (160 * salario_hora) + (40 * salario_hora * 1.5) + ((horas_trabajadas - 200) * salario_hora * 2)

    # Calcular ISR
    isr = calcular_isr(sueldo_bruto)

    # Calcular deducciones
    seguridad_social = sueldo_bruto * 0.025

    if opcion_caja == 2:
        caja_ahorros = 1000
    elif opcion_caja == 3:
        caja_ahorros = sueldo_bruto * 0.03
    elif opcion_caja == 4:
        caja_ahorros = sueldo_bruto * 0.05
    else:
        caja_ahorros = 0

    if opcion_ahorro == 2:
        ahorro_solidario = sueldo_bruto * 0.01
    elif opcion_ahorro == 3:
        ahorro_solidario = sueldo_bruto * 0.02
    else:
        ahorro_solidario = 0

    # Calcular sueldo neto
    sueldo_neto = sueldo_bruto - (isr + seguridad_social + caja_ahorros + ahorro_solidario)

    # Mostrar resultados
    print("\n--- Resumen de Pago ---")
    print(f"Sueldo Bruto: ${sueldo_bruto:.2f}")
    print(f"ISR: ${isr:.2f}")
    print(f"Seguridad Social: ${seguridad_social:.2f}")
    print(f"Caja de Ahorros: ${caja_ahorros:.2f}")
    print(f"Ahorro Solidario: ${ahorro_solidario:.2f}")
    print(f"Sueldo Neto: ${sueldo_neto:.2f}")


def calcular_isr(sueldo_bruto):
    tabla_isr = [
        (0.01, 746.04, 0.00, 0.0192),
        (746.05, 6332.05, 14.32, 0.064),
        (6332.06, 11128.01, 371.83, 0.1088),
        (11128.02, 12935.82, 893.63, 0.16),
        (12935.83, 15487.71, 1182.88, 0.1792),
        (15487.72, 31236.49, 1640.18, 0.2136),
        (31236.50, 49233.00, 5004.12, 0.2352),
        (49233.01, 93993.90, 9236.89, 0.30),
        (93993.91, 125325.20, 22665.17, 0.32),
        (125325.21, 375975.61, 32691.18, 0.34),
        (375975.62, float('inf'), 117912.32, 0.35)
    ]

    for limite_inf, limite_sup, cuota_fija, porcentaje in tabla_isr:
        if limite_inf <= sueldo_bruto <= limite_sup:
            excedente = sueldo_bruto - limite_inf
            return cuota_fija + (excedente * porcentaje)
    return 0


# Ejecutar el programa
calcular_sueldo_neto()
