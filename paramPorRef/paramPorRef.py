def paramPorRef(num1, num2):
	num1 = 1001
	num2 = 2002
	print('paramPorRef *num1:'+str(num1))
	print('paramPorRef *num2:'+str(num2))
	return num1, num2
	
def paramPorVal(num1, num2):
	num1 = 101
	num2 = 202
	print('paramPorVal num1:'+str(num1))
	print('paramPorVal num2:'+str(num2))
	
def main():
	num1 = 1
	num2 = 2
	print('main_1 num1:'+str(num1))
	print('main_1 num2:'+str(num2))
	
	paramPorVal(num1, num2)
	print('main_2 num1:'+str(num1))
	print('main_2 num2:'+str(num2))

	num1, num2 = paramPorRef(num1, num2)
	print('main_3 num1:'+str(num1))
	print('main_3 num2:'+str(num2))

# #################################################
# Programa principal
# #################################################
if __name__ == "__main__":
	main()
