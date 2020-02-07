import nltk

word_data = "Django advertises itself as 'the web framework for perfectionists with deadlines' and 'Django'"
nltk_token = nltk.word_tokenize((word_data))
print(nltk_token)
print('-_-_-_' * 20)
print(' ' * 20)

'''Tokenizing Sentences'''
sentense_data = "Sun rises in the east. Sun sets in the west."
nltk_token = nltk.sent_tokenize(sentense_data)
print(nltk_token)
print('-_-_-_' * 10)
