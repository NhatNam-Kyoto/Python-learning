class InpOupString():
	def __init__(self):
		self.s =''
	def getString(self):
		self.s = input('Nhap gi do: ')
	def PrintString(self):
		print(self.s.upper())
test = InpOupString()
test.getString()
test.PrintString()