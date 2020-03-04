import os

#讀取檔案

def read_file (filename) :
	dia = []
	with open (filename, 'r', encoding ='utf-8-sig' ) as f:
			for line in f:
				dia.append (line.strip())
	return dia


def convert(chat) :
	new = []
	person = None
	for line in chat :
		if line == 'Allen' : 
			person = 'Allen'
			continue 
		elif line == 'Tom' :
			person = 'Tom'
			continue
		if person :
			new.append(person + ':' + line)
	return new 

def write_file (filename, chat ) :
	with open (filename,'w') as f:
		for line in chat :
			f.write(line+ '\n')



def main ():
	filename = 'input.txt'
	if  os.path.isfile (filename) : #檢查檔案在不在
		print ('檔案存在')
		chat = read_file(filename)
		chat = convert(chat)
		write_file('output.txt', chat)
	else :
		print ('找不到檔案不在')
	

main ()