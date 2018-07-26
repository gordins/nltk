import pprint
pp = pprint.PrettyPrinter(indent=2)

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


lemmatizer = WordNetLemmatizer()


pp.pprint(lemmatizer.lemmatize('cats'))
pp.pprint(lemmatizer.lemmatize('dogs'))
pp.pprint(lemmatizer.lemmatize('cacti'))
pp.pprint(lemmatizer.lemmatize('cactuses'))
pp.pprint(lemmatizer.lemmatize('python'))

pp.pprint(lemmatizer.lemmatize('better'))

pp.pprint(lemmatizer.lemmatize('better', pos=wordnet.ADJ))
