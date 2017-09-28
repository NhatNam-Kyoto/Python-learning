from abc import ABC,abstractmethod
class mayIn(ABC):
	"""docstring for MayIn"""
	#Sử dụng tính trừu tường
	@abstractmethod
	def __init__(self, ID, tenmay,thuongHieu, giaThanh):
		#dùng __ để ẩn thuộc tính
		self.__ID =ID
		self.__tenmay = tenmay
		self.__thuongHieu = thuongHieu
		self.__giaThanh = giaThanh
	@abstractmethod
	def inthongtin(self):
		print('ID: ',self.__ID)
		print('tenmay: ',self.__tenmay)
		print('thuongHieu: ',self.__thuongHieu)
		print('giaThanh: ',self.__giaThanh)
class mayInKim(mayIn):
	"""docstring for mayInKim"""
	def __init__(self, ID, tenmay,thuongHieu, giaThanh, soKim):
		super().__init__(ID, tenmay, thuongHieu, giaThanh)
		self.__soKim= soKim
	def inthongtin(self):
		super().inthongtin()
		print('So kim: ',self.__soKim)
class mayInMuc(mayIn):
	def __init__(self, ID, tenmay,thuongHieu, giaThanh, loaiMuc):
		super().__init__(ID, tenmay,thuongHieu, giaThanh)
		self.__loaiMuc = loaiMuc
	def inthongtin(self):
		super().inthongtin()
		print("Loai muc: ", self.__loaiMuc)
may1 = mayInKim(1,'DBRING', 'Canon',9000000,3)
may2 = mayInMuc(2,'Test','Canon',10000000,'Đen')
may1.inthongtin()
may2.inthongtin()