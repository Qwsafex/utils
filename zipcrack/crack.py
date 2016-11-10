import sys
import itertools
from functools import reduce
from zipfile import ZipFile


combiningDepth = 2

if len(sys.argv) != 3:
	print("Usage: crack.py tocrack.zip dict.txt")
	exit()


with ZipFile(sys.argv[1]) as zipfile, open(sys.argv[2]) as dictfile:
	passWords = []
	for line in dictfile:
		if line[-1] == '\n':
			line = line[0:-1]
		passWords.append(line)
		linelist = list(line)
		linelist[0] = str(linelist[0]).upper()
		passWords.append("".join(linelist))

	# In case of CAPS LOCK
	new_pass_words = []
	for passWord in passWords:
		newWord = ""
		for c in passWord:
			if c.isupper():
				newWord += c.lower()
			else:
				newWord += c.upper()
		new_pass_words.append(passWord)
		new_pass_words.append(newWord)
	passWords = new_pass_words
	ok = False
	for i in range(1,4):
		passwords = list(itertools.product(passWords, repeat=i))
		passwords = list(map(lambda x : reduce(lambda a,b: a+b, x), passwords))
		for password in passwords:
			try:
				print(password)
				zipfile.extractall(pwd=password.encode())
				print("SUCCESS!!!!", password)
				ok = True
				break
			except Exception:
				pass
		if ok:
			break
