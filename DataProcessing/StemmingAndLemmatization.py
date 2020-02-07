import nltk
from nltk.stem.porter import PorterStemmer

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

porter_stemmer  =PorterStemmer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"

# First Word tokenization
nltk_token = nltk.word_tokenize(word_data)

# Next find the roots of the word
for word in nltk_token:
    print('Actual: %s Stem: %s' % (word, porter_stemmer.stem(word)))
    print('-_-_-_-_' * 5)
    print(' ' * 20)


for word in nltk_token:
    print("Actual: %s | Lemma: %s" % (word, wordnet_lemmatizer.lemmatize(word)))
    print(' LEMMATIZATION ')
    print('-_-_-_-_' * 5)
