import pprint
pp = pprint.PrettyPrinter(indent=2)

from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello Mr. Stefan, how are you doing today? The weather is great and this lesson is awesome. The sky is grayish-red. You shoudn't eat dill, right?! Cool."


tokenized_text = []
for sentence in sent_tokenize(text):
    tokenized_text.append(word_tokenize(sentence))

pp.pprint(tokenized_text)
