# su dung print khong co tham so end
print('hello')
print('huy')

# su dung print co tham so end
print('hello', end = ' ')
print('huy')

# print voi tham so sep
print('chao', 'huy',19, 'nha', sep= '? ')

# in chuoi noi
print('chao ' + 'huy')

# dinh dang dau ra bang {}
tuoi = 18
ten_ban_gai = 'Tam'
print('huy nam nay {} tuoi va co {} la ban gai nam nay bang tuoi voi huy la {} tuoi'.format(tuoi, ten_ban_gai, tuoi))

# lay dau vao tu nguoi dung, doi kieu du lieu
tuoi = int(input('nhap tuoi: '))
print('hien tai ban:',tuoi,'tuoi')
print('kieu du lieu ban nhap la: {}'.format(type(tuoi)))
