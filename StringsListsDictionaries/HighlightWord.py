def highlight_word(sentence, word):
	todo = word.upper()
	s_result = sentence.replace(word,todo)
	return(s_result)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))