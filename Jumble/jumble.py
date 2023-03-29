import itertools
import os
import time
import string
import json

######### to make a index file from dictionry ########
def getword_list():
	with open(f"{os.getcwd()}/Jumble/dictionary2.0.txt",'r') as file:
			words = file.readlines()

			words_lis = []
			for i in words:
				words_lis.append(i.lower().strip())

			alpha_range = {}
			found_char = 0
			alphabates = string.ascii_lowercase
			for i in alphabates:
				for j in words_lis:
					if j.startswith(f"{i}") and found_char == 0:
						alpha_range[i] = [words_lis.index(j)]
						found_char = 1
					elif not j.startswith(f'{i}') and found_char == 1:
						alpha_range[i].append(words_lis.index(j))
						found_char = 0

			alpha_range[i].append(None)

	with open(f"{os.getcwd()}/Jumble/dictionryIndex.json", 'w') as file:
		json.dump(alpha_range, file)
	print("json index file dumped")
	return words_lis



########  solve jumble word ###########
def solve(jumble, words_lis):
	with open(f"{os.getcwd()}/Jumble/dictionryIndex.json", 'r') as file:
		content = file.read()
		alpha_range = json.loads(content)

	lis = []
	a = itertools.permutations(jumble)
	for i in a :
		i = "".join(i)
		lis.append(i)

	match_words = []
	start = time.time()
	for word in lis:
		word = word.lower()
		if word in words_lis[alpha_range[word[0]][0]:alpha_range[word[0]][1]]:
			match_words.append(word)
	return match_words



	

if __name__ == "__main__":
	message = """your computer might get hanged so
if you have 4 gb of ram :
enter a jumble word lessthen or equal to 10 letters.
if you have 8 gb of ram :
enter a jumble word lessthen or equal to 11 letters."""
	print(message)
	word_list = getword_list()
	while True :
		jumble = input("enter word : ")
		if jumble == "q" or jumble == "quit":
			break
		words = solve(jumble, word_list)
		print(words)
