def add_numbers(a, b):
	return a+b

def subtract numbers(a , b):
	return a - b

def multiply_numbers(a,b):
	return a* b

def divide_numbers(a, b):
	if b== 0:
		raise ValueError("Dzielenie przez zerojest niedozwolone.")
	return a /b

if  name  == "  main  ":
	num1 = 10
	num2 = 5
	print(f"Dodawanie: {add_numbers(num1, num2)}")
	print(f"Odejmowanie: {subtract_numbers(num1, num2)}")
	print(f"Mnożenie: {multiply_numbers(num1, num2)}")
	print(f"Dzielenie: {divide_nubers(num1, num2)}")
