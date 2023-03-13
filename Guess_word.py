import random as r
This_dictionary={
    'classes':['english','maths','science'],
    'fruits':['banana','apple']
}
print(This_dictionary.keys())
to_play=True
while to_play:         #loop which decides to play the game again
    while True:        #this loop decides wheather the input in correct from the list
        user_input = input("Select any word from above keys:")
        if user_input in This_dictionary.keys():
            print()
            break
        else:
            print("Enter the word again from the list")
    list=[x for x in This_dictionary.get(user_input)]
    r_word=r.choice(list)  #selection of word form the list
    len_word=len(r_word)

    guess_count=0
    print("Guess a  " +str(len_word)+"  letter word from the following category: "+user_input)
    blank_list=["-" for x in range(len_word)]

    guess=''
    while guess!=r_word:
        print("".join(blank_list))
        guess = input("Enter the guess:").lower()
        guess_count += 1
        if guess==r_word:
            print("Correct! You guessed the word in"+str(guess_count)+ "guesses.")  #if the guess is write

        else:
            ind = r.randint(0, len_word - 1)                 #if the guess not write
            print("That is not correct. Let us reveal a letter to help you!")
            if blank_list[ind] == "-":
                blank_list[ind] = r_word[ind]
    to_play=input("Enter Y to play again,Enter N to not play again:").lower()
    if to_play!='y':
        to_play=False



