import struct
import math
import Image
import sys
import os
import random

def imgtofile(filename,savefile,key):
	inhash = hash(key)
	filed = open(savefile,'wb')
	dataimg = Image.open(filename)
	pimg = dataimg.load()
	size = dataimg.size
	for i in range(size[0]):
		for j in range(size[1]):
			if(pimg[i,j] == (0,0,0)):
				filed.close()
				return
			else:
				index = i*size[0]+j
				y = (inhash%(index+1))%3
				filed.write(struct.pack('B',pimg[i,j][y]))
				
def filetoimg(filename,key):
	inhash = hash(key)
	filesize = os.path.getsize(filename)
	sqrtxy = int(math.sqrt(filesize))+1
	size = (sqrtxy,sqrtxy)
	print size
	dataimg = Image.new('RGB', size)
	pimg = dataimg.load()
	f = open(filename,'rb')
	f.seek(0,0)
	for i in range(size[0]):
		for j in range(size[1]):
			temp = f.read(1)
			if(len(temp)>0):
				code = struct.unpack('B',temp)[0]
				index = i*size[0]+j
				y = (inhash%(index+1))%3
				if(y == 0):
					pimg[i,j] = (code,random.randint(1,255),random.randint(1,255))
				elif(y == 1):
					pimg[i,j] = (random.randint(1,255),code,random.randint(1,255))
				else:
					pimg[i,j]= (random.randint(1,255),random.randint(1,255),code)
			else:
				f.close()
				dataimg.save('svae.bmp')
				print 'saved file:save.bmp'
				return
	
if __name__ == "__main__":
	if(sys.argv[1] == 'en'):
		filetoimg(sys.argv[2],sys.argv[4])
	elif(sys.argv[1] == 'un'):
		imgtofile(sys.argv[2],sys.argv[3],sys.argv[4])
	else:
		print 'plase sure commen is ok!'
