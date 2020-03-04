import os

#讀取檔案

def read_file (filename) :
	dia = []
	with open (filename, 'r', encoding ='utf-8-sig' ) as f:
			for line in f:
				dia.append (line.strip())
	return dia


def convert(lines) :
	
	person = None # 預設值
	Allen_sticker_count = 0
	Allen_image_count = 0 
	Allen_word_count = 0
	vike_word_count = 0
	vike_sticker_count = 0
	vike_image_count = 0
	for line in lines :
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen' :
			if s[2] == '貼圖' :
				Allen_sticker_count += 1
			elif s[2] == '圖片' :
				Allen_image_count += 1
			else :
				for m in s[2:] :
					Allen_word_count += len(m)

		elif name == 'Viki' :
			if s[2] == '貼圖' :
				vike_sticker_count += 1
			elif s[2] == '圖片' :
				vike_image_count += 1
			else :
				for m in s[2:] :
					vike_word_count += len(m)

	print ('Allen 說了', Allen_word_count,'個字')
	print ('Allen 傳了', Allen_sticker_count, '個貼圖' )
	print ('Allen 傳了', Allen_image_count, '個圖片' )
	print ('viki 說了', vike_word_count,'個字') 
	print ('viki 傳了', vike_sticker_count, '個貼圖' )
	print ('viki 傳了', vike_image_count, '個圖片' )
	

def write_file (filename, lines ) :
	with open (filename,'w') as f:
		for line in lines :
			f.write(line+ '\n')



def main ():
	filename = 'LINE-Viki.txt'
	if  os.path.isfile (filename) : #檢查檔案在不在
		print ('檔案存在')
		lines = read_file(filename)
		lines = convert(lines)
		# write_file('output.txt', lines)
	else :
		print ('找不到檔案不在')
	

main ()