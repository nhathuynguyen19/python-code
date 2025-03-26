number = 10

# khai bao bien
HoTen = 'Nguyen Dinh Nhat Huy'
print(HoTen)

# thay doi bien ho ten
HoTen = 'Nguyen Dinh Nhat Hoang'
print(HoTen)

# gan nhieu gia tri cho nhieu bien
HoTen, NgaySinh, ThangSinh, NamSinh = 'Nguyen Dinh Nhat Huy', 19, 9, 2005
print(f"{HoTen} sinh ngay {NgaySinh}/{ThangSinh}/{NamSinh}")

#gan cung mot gia tri cho nhieu bien 
Lop = NgaySinh = 9
print(f"Huy hoc lop {Lop} sinh ngay {NgaySinh}")

#in hang tu constant, hang so khong the thay doi
import constant
print(constant.PI)
print(constant.trong_luc)

#hoac tao hang so bang cach viet hoa ten bien nhung hang so nhu vay van co the thay doi
PI = 3.14
TRONG_LUC = 9.8

print(PI)
print(TRONG_LUC)

# chu, literals, chuoi ky tu
ten_trang_web = 'google.com'
so_dien_thoai = 964926945
print(f"{ten_trang_web} {so_dien_thoai}")

# chu dac biet trong python
chu_dac_biet = None
print(chu_dac_biet)

# list, tuple, dict and set literal
list_literal = ["xoai","man","oi"]
tuple_literal = (1,'hai',3)
dict_literal = {'a':'apple','b':'ball','c':'cat'}
set_literal = {'a','b','c'}

print(list_literal)
print(tuple_literal)
print(dict_literal)
print(set_literal)

# in bien tuy chon trong danh sach (list)
print(list_literal[0])

# truy cap tuple literal, tuple literal khong the thay doi
print(tuple_literal[1])

# in tap hop set_literal va kieu
print(set_literal)
print(type(set_literal))

# truy cap dict_literal
print(dict_literal['a'])




