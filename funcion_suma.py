def funcion_Suma(A,num1):
	A= A+int(num1)
	return A

def funcion_Resta(A,num2):
	A=A-int(num1)
	return A	

def funcion_Multiplica(A,num1):
	A=A*int(num1)
	return A

def funcion_Divide(A,num1):
	A=A/int(num1)
	return A

A=0
while True:
	operacion=raw_input("Teclee una operacion +,-,*,/, 0 para salir    ")
	if operacion == "0":
		break	
	num1=raw_input("Teclee un numero ")
	if operacion== "+":
		A=funcion_Suma(A,num1)
	elif operacion == "-":
		A=funcion_Resta(A,num1)
	elif operacion=="*"	:
		A= funcion_Multiplica(A,num1)
	elif operacion=="/":
		if A==0:
			print("division entre cero  no permitida")
		else:
			A=funcion_Divide(A,num1)
	else:
		print ("Operacion erronea")
print "RESULTADO :" +str(A)