# Práctica 1. Estructura de control selectiva
Cálculo del Sueldo Neto
Presentación del problema
En esta práctica se desarrolla un programa en Python que permite calcular el sueldo neto de una persona empleada en una empresa, considerando su salario por hora y el número de horas trabajadas en el mes. El cálculo del sueldo bruto debe seguir las reglas de pago establecidas para horas normales y extras. Además, se aplican deducciones por ISR, seguridad social, caja de ahorros (si aplica) y ahorro solidario (si aplica). El resultado final es el sueldo neto que recibe la persona.
Diseño del algoritmo
El algoritmo sigue los siguientes pasos:
Entrada de datos: Se solicita al usuario su salario por hora, el número de horas trabajadas y su participación en la caja de ahorros y el ahorro solidario.
Cálculo del sueldo bruto:
Si las horas trabajadas son hasta 160, se multiplica por el salario por hora.
Si las horas están entre 161 y 200, las primeras 160 se pagan normales y las extras a 1.5x.
Si las horas superan 200, se aplica el criterio anterior y las horas extras después de 200 se pagan al doble.
Cálculo del ISR: Se busca el rango en la tabla del SAT y se calcula el impuesto aplicando la cuota fija y el porcentaje correspondiente.
Cálculo de deducciones:
Seguridad social (2.5% del sueldo bruto).
Caja de ahorros (según la opción seleccionada por el usuario: fijo, 3% o 5%).
Ahorro solidario (según la opción: 1% o 2%).
Cálculo del sueldo neto: Se restan todas las deducciones al sueldo bruto.
Salida de datos: Se imprime el desglose del cálculo con todas las percepciones y deducciones.
Implementación en Python
El programa se implementó en Python utilizando funciones para estructurar el código de manera clara y modular. Se creó una función principal calcular_sueldo_neto() que gestiona la entrada de datos, el cálculo del sueldo y la impresión de resultados. Además, se definió la función calcular_isr() para determinar el ISR de manera eficiente según la tabla proporcionada.
Se utilizaron condicionales if-elif-else para determinar las tarifas de pago de las horas trabajadas y para calcular las deducciones de manera adecuada. La estructura modular del código facilita su mantenimiento y comprensión.
Comentarios finales
El programa desarrollado permite calcular el sueldo neto de manera precisa y flexible, adaptándose a las diferentes opciones de participación en la caja de ahorros y el ahorro solidario. Además, el uso de funciones mejora la claridad del código y facilita futuras modificaciones. Se recomienda probar el programa con diferentes valores de entrada para verificar su correcto funcionamiento en todos los casos posibles.



