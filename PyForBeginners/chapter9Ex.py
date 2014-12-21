# chapter 9 exercise

''' create a class that calculate payroll, pass name, wage, and hours.
create an optional method for overtime. Print name normal hours at wage and
money earned, then hours of overtime, and finally the total.
'''

class payroll:
	def __init__(self, name, wage, hours):
		self.name = name
		self.wage = wage
		self.hours = hours
	def pay(self):
		if(self.hours <= 40):
			pay = self.hours * self.wage
			print('{} earned {} for {} hours\n'.format(self.name, pay, self.hours))
		else:
			pay = self.wage * 40
			print('{} earned {} for {} hours\n'.format(self.name, pay, 40))
	def over(self):
		if(self.hours > 40):
			pay = 40 * self.wage
			overhours = self.hours - 40
			overpay = self.wage * 1.5 * overhours
			totalPay = overpay + pay
			print('{} earned {} for {} hours of overtime\n'.format(self.name, overpay, overhours))
			print('{} was the total pay earned'.format(totalPay))
		else:
			pay = self.hours * self.wage
			print('{} did not work overtime\n'.format(self.name))
			print('{} was the total pay earned'.format(pay))



c = 'y'
while(c == 'y'):
	ename = str(input('enter the employee\'s name:\n'))
	ewage = float(input('enter the employee\'s wage:\n'))
	ehours = float(input('enter the employee\'s hours:\n'))
	employee = payroll(ename, ewage, ehours)
	employee.pay()
	employee.over()
	c = input("continue 'y or n'?:\n")
			
		
