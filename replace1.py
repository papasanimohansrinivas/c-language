word=raw_input('enter a word')
char1=raw_input('enter a character to replce')
char2=raw_input('enter new character')
def replace(word,char1,char2):
    newString = ""
    for next_char in word:         # for each character in the word
        if next_char == char1:     # if it is the character you want to replace
            newString += char2     # add the new character to the new string
        else:                      # otherwise
            newString += next_char # add the original character to the new string
    return newString


print replace(word,char1,char2)    