from spellchecker import SpellChecker
spell=SpellChecker()

while true:
	text=input("Enter the sentence to autocorrect: ")
	words=text.split()
	corrected_words=[]
	for word in words:
		if not spell.unknown=([word]):
			corrected_words.append(word)
		else:
			corrected_words.append(spell.correction(word))
	corrected_text=' '.join(corrected_words)
	print(corrected_text)