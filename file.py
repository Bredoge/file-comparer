file1 = input("choose the proper file: ")
file2 = input("choose the wrong file: ")
y = open(file1, "r")
x = open(file2, "r")

#y = open("text1.txt", "r")
#x = open("text2.txt", "r")

i = 0

while 1:
	fr_txt = y.readline()
	sc_txt = x.readline()
	if fr_txt != sc_txt:
		print("\n")
		pizza = 0
		spagetti = 0
		spc_count = 0
		input("there is an error in %d line"%(i + 1))
		while 1:
			if fr_txt[pizza] == "\n":
				break
			if fr_txt[pizza] == " ":
					spc_count = spc_count + 1			
			if fr_txt[pizza] != sc_txt[spagetti]:
				if fr_txt[pizza + 1] == sc_txt[spagetti]:
					pizza = pizza + 1
					input("error is in %d character of whole line & its in %d word"%(spagetti + 1, spc_count + 1))
				elif fr_txt[pizza] == sc_txt[spagetti + 1]:
					spagetti = spagetti + 1
					input("error is in %d character of whole line & its in %d word"%(pizza + 1, spc_count + 1))
				else:
					input("error is in %d character of whole line & its in %d word"%(pizza + 1, spc_count + 1))
			pizza = pizza + 1
			spagetti = spagetti + 1
	i = i + 1

y.close()
x.close()