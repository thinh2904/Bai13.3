import string
size=int(input('Nhập giới hạn dữ liệu (MB): '))
while size<1 or size>1024:
	size=int(input('Nhập lại giới hạn giới hạn dữ liệu: '))
one_file=1000*1024
nguyen=size*(2**20)//(one_file)
du=size*(2**20)%(one_file)
ky_tu=string.ascii_lowercase*100000
for i in range(nguyen):
	file=open('File'+str(i),'w')
	file.write(a=''.join(ky_tu,one_file)) 
	file.close()
file_cuoi=open('File cuối','w')
file_cuoi.write(''.join(random.sample(ky_tu,du)))
file_cuoi.close()
print('Kết thúc chương trình')
