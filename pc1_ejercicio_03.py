#Ejercicio 3: realizar un programa que nos pida el ingreso total de un hogar y vaya pidiendo posibles gastos. Como resultado debe decir todos los egresos y ahorro. 
print("Evaluación de los ingresos y gastos mensuales del hogar") 
ingreso_total = float(input("indicar cuánto es el ingreso mensual total de su hogar: "))
print("A continuación, indicar cuánto es el gasto mensual del hogar en los siguientes segmentos de consumo")
serv_luz = float(input("gasto mensual por servicio de luz: "))
serv_agua = float(input("gasto mensual por servicio de agua: "))
alquiler = float(input("gasto mensual por alquiler de vivienda: "))
alimentacion = float(input("gasto mensual por alimentación: "))
transporte = float(input("gasto mensual por servicios de transporte: "))
educación = float(input("gasto mensual por servicios de educación: "))
otros = float(input("gasto mensual en otros bienes/servicios: "))
import math 
egreso_total = serv_luz+serv_agua+alquiler+alimentacion+transporte+educación+otros
ahorro = ingreso_total - egreso_total
msg = f"el ingreso mensual total de su hogar es de {ingreso_total} soles, \npero en total gasta mensualmente {egreso_total} soles, \npor lo tanto, su ahorro mensual es de {ahorro} soles"
print(msg)