subtraction = lambda num1, num2: num1-num2

def cal(num1,num2):
	summ = summation(num1, num2)
	subb = subtraction(num1, num2)
	return subb, summ

def summation(n1, n2):
	return n1+ n2

cal(int(input()), int(input()))