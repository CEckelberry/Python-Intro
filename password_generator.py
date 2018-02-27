# Use an import statement at the top

import random


word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces

def generate_password(input_material):
	#created output string, and turns for the loop
	pwd_output = ""
	turns = 0
	while turns < 3:
		#t is our variable to hold the random numbers which assures us the selection of the word from the "word list" is actually at random
		t = random.randint(0, len(word_list))
		print(t)
		pwd_output = pwd_output + word_list[t]
		turns += 1
	return pwd_output


# test your function
print(generate_password(word_file))