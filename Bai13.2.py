import os
ten_thu_muc=input('Nhập tên thư mục: ')
ten_file=input('Nhập tên File: ')
os.mkdir(ten_thu_muc)
os.chdir(ten_thu_muc)
file=open(ten_file,'w')
file.close()