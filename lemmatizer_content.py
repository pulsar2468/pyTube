####################################
#file_name: lemmatizer_content.py  #
#author: Riccardo La Grassa        #
#data created: 20/11/2016          #
#data last modified: 9/01/2018-01-19     #
#Python interpreter: 3.5.2         #
#mail: riccardo2468@gmail.com      #
####################################

from nltk.stem import WordNetLemmatizer

def lemmatizer_words(clean_mashup):
    wordnet_lemmatizer = WordNetLemmatizer()
    list_lemmatizer=[]
    for term in clean_mashup:
            list_lemmatizer.append((wordnet_lemmatizer.lemmatize(term,'v')))
    return list_lemmatizer
