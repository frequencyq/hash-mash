import hashlib
db = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

x = input(": ")
xs = x.split()
lc = 0
pc = ""
pp = []
for i in xs:
	pp.append(len(i))
for i in xs:
	lc += len(i)
	pc += i
pcs = pc
counter = 0
def plumber(text, test):
	co = 0
	kk = text
	for i in text:
		if test[co] == "1":
			kk = kk[:co] + db[i] + kk[co+1:]
		co += 1
	return kk

cx = ""
ver = True
while cx != "1"*lc :
	pc = pcs
	counter += 1
	cx = bin(counter)[2:].zfill(lc)
	ll = (plumber(pc,cx))
	data = ""
	for i in pp:
		data += ll[:i] + " "
		ll = ll[i:]
	pol = hashlib.sha256(data.encode('utf-8'))
	pol = pol.hexdigest()
	if pol[-3:] == "111":
		print(f"{data}\n{pol}")
		ver = False
		break	

if ver:
	print("the text that you provided doesn't have possible way\nto make hash without nonce with!")

