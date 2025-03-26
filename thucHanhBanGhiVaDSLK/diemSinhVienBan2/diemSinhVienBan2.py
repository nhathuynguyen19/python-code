
class date:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

class sinhvien:
    def __init__(self, masinhvien, hoten, ngaysinh, diem):
        self.masinhvien = masinhvien
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.diem = diem

ar = []



n = int(input())

for i in range(n):
    ma = int(input())
    hoten = input()
    ngay, thang, nam = map(int, input().split())
    ns = date(ngay, thang, nam)

    diem = float(input())

    sv = sinhvien(ma, hoten, ns, diem)
    ar.append(sv)

for sv in ar:
    if sv.diem >= 5.0:
        print(f"{sv.masinhvien}, {sv.hoten}, {sv.ngaysinh.ngay}/{sv.ngaysinh.thang}/{sv.ngaysinh.nam}, {sv.diem}")
print("**********")

for sv in ar:
    if sv.ngaysinh.nam == 2003:
        print(f"{sv.masinhvien}, {sv.hoten}, {sv.ngaysinh.ngay}/{sv.ngaysinh.thang}/{sv.ngaysinh.nam}, {sv.diem}")
print("**********")

for sv in ar:
    tachten = sv.hoten.split()
    ten = tachten[-1]

    if ten == 'Tuan':
        print(f"{sv.masinhvien}, {sv.hoten}, {sv.ngaysinh.ngay}/{sv.ngaysinh.thang}/{sv.ngaysinh.nam}, {sv.diem}")