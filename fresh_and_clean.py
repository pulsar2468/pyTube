####################################
#file_name: fresh_and_clean.py     #
#author: Riccardo La Grassa        #
#data created: 16/11/2016          #
#data last modified: 2/12/2017     #
#Python interpreter: 3.5.2         #
#mail: riccardo2468@gmail.com      #
####################################

import re

def load_stop_word(path):
    #grammar file. i will erase all the useless words
    grammarlist=[]
    try:
        with open(path, 'r') as f:
            grammarlist.append(f.read().splitlines())
        f.close()
        return grammarlist

    except IOError:
        print('stop word file not found!\nabort')
        exit()



def clean_text(original_list,grammarlist):
    list_splitted=[]
    list_clean=[]
    for i in original_list:
        if i:
            list_splitted.append((i.split()))
    clean_title=[]

    for i in range(0, len(list_splitted)):
        for j in range(0, len(list_splitted[i])):
            if not re.search('https?|RT|href=|class=|src=|align=|border=|height=|width=|alt=|<p>|reading|@', list_splitted[i][j]):
                list_splitted[i][j]=re.sub('[\U0001F300-\U0001F6FF]|•|‘|\'s|\'|"|”|!|’s|“|,|:|&|;|/|\+|\?|…|[.]+|-|–|—|→|\(|\)|#|', '', list_splitted[i][j]) #i clean the text from link replytweet and @tag
                if not (len(list_splitted[i][j]) < 3):
                    if not (any(list_splitted[i][j].lower() in s for s in grammarlist)):
                        clean_title.append(list_splitted[i][j].lower())
        list_clean.append([i for i in clean_title])
        clean_title.clear()
    return list_clean