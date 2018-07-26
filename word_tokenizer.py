import pprint
pp = pprint.PrettyPrinter(indent=2)

from nltk.tokenize import word_tokenize

example_text = "Hello Mr. Stefan, how are you doing today? The weather is great and this lesson is awesome. The sky is grayish-red. You shoudn't eat dill, right?! Cool."

pp.pprint(word_tokenize(example_text))
