import random
import nltk
nltk.download('words')
from nltk.corpus import words




def read_dictionary():
	
	nltk.data.path.append('/work/words')
	words_ls = words.words()
	words_fi = [word for word in words_ls if len(word) == 5 ]	

	return	words_fi


def compute_response(target, guess):
	targetl=list(target)
	guessl=list(guess)
	l=['.','.','.','.','.']

	for i in range(len(targetl)):
		if targetl[i] == guessl[i]:
			l[i]=targetl[i].upper()
			guessl[i]='+'
			targetl[i]='+'
			
	for s in range(len(targetl)):
		if guessl[s] != '+':	
			if targetl[s] == guessl[s]:
				l[s]=targetl[s].upper()
				targetl[targetl.index(guess[s])]='+'
			
			if guessl[s] in targetl:
				l[s] = guessl[s].lower()
				targetl[targetl.index(guess[s])]='+'
	return(''.join(l))
		
def is_valid(guess, dictionary):

	if guess.lower() in dictionary :	
		return is_valid
		



dictionary = read_dictionary()

while True:

    choice = input("Play a game? (Y/N): ")
    if choice == 'N':
        break
    else:
        print("Type a 5 letter word")

    target = random.choice(dictionary).upper()      
    turns = 0
    MAX_TURNS = 6
    while True:
        if turns == MAX_TURNS:
            print("Game over! :(")
            print('The word was: {}'.format(target))
            break
        else:
            print(MAX_TURNS-turns,"attempts remaining")
            guess = input().upper()
            while not is_valid(guess, dictionary):
                print('{} is not a valid word!'.format(guess))
                guess = input().upper()

            print("You guessed: {}".format(guess))
            response = compute_response(target, guess)
            print('Response: {}'.format(response))
	    
            if response == guess:
                print("You win! :)")
                break
        turns += 1
        


