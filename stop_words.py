import pprint
pp = pprint.PrettyPrinter(indent=2)

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, RegexpTokenizer


text = "Hello Mr. Stefan, how are you doing today? The weather is great and this lesson is awesome. The sky is grayish-red. You shoudn't eat cardboard, right?! Cool."

stop_words = set(stopwords.words("english"))
pp.pprint(stop_words)


tokenizer = RegexpTokenizer(r'\w+')
filtered_sentences = []
for sentence in sent_tokenize(text):
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [token for token in tokens if not token in stop_words]
    filtered_sentences.append(filtered_words)


pp.pprint(filtered_sentences)
