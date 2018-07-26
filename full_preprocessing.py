import pprint
pp = pprint.PrettyPrinter(indent=2)

from nltk import pos_tag
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords

tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))


def pos_to_wordnet(pos):
    if pos.startswith('J'):
        return wordnet.ADJ
    if pos.startswith('V'):
        return wordnet.VERB
    if pos.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN


text = "Hello Mr. Stefan, how are you doing today? The weather is great and this lesson it is even better. The sky is grayish-red. You shoudn't eat dill, right?! Cool."


sentences = sent_tokenize(text)
tokened_sentences = [tokenizer.tokenize(sentence) for sentence in sentences]

tagged_tokened_sentences = [pos_tag(tokened_sentence)
                            for tokened_sentence in tokened_sentences]

preprocessed_text = []

for sentence in tagged_tokened_sentences:
    preprocessed_sentence = []
    for word in sentence:
        if(word not in stop_words):
            preprocessed_sentence.append(lemmatizer.lemmatize(
                word[0], pos=pos_to_wordnet(word[1])))
    preprocessed_text.append(preprocessed_sentence)

pp.pprint(preprocessed_text)
