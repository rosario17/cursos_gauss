A=0
while True:
    print("Teclee una operacion (+, -, *, /, 0 para salir")
    operacion=raw_input()
    if operacion == '0':
        break
    print("Teclee un numero")
    num1=int(raw_input())
    if operacion== "+":
         A= A+num1
    elif operacion == "-":
         A= A-num1
    elif operacion == "*":
         A= A*num1
    elif operacion == "/":
     	if A==0:
     		print("Division entre cero")
     	else:	
           A = A/num1
    else:
      print("operacion erronea")
    print ("resultado: ", str(A))
print "resultado final: " +str(A)