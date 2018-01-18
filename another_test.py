import pickle
import os
import datetime
from collections import Counter

def get_file(directory,action):
        str_date=None
        for (root, dirnames, files) in os.walk("data/"+directory):
            date=(os.stat(root+'/'+files[0])).st_mtime
            str_date=files[0]
            if len(files) == 1: return files[0]
            else:
                if action:
                    for i in files:
                        stat_buf=os.stat(root+'/'+i)
                        tmp=stat_buf.st_mtime
                        if date < tmp:
                            date=tmp
                            str_date=i

                else:
                    for i in files:
                        stat_buf=os.stat(root+'/'+i)
                        tmp=stat_buf.st_mtime
                        if date > tmp:
                            date=tmp
                            str_date=i

            return str_date



def open_dataset(name):
    try:
        with open(name, 'rb') as f:
            l = pickle.load(f)
        f.close()
    except IOError:
        print('File not found!')
        exit('Exit')
    return l


for (root, dirnames, files) in os.walk("data/"):
    for name in dirnames:
                l_file=get_file(name,1)
                f_file=get_file(name,0)
                if l_file and f_file:
                    load_list0=open_dataset("data/"+name+'/'+f_file)
                    load_list1=open_dataset("data/"+name+'/'+l_file)
                    diff=len(load_list1)-len(load_list0)
                    print("New video_item for",name,diff,[load_list1[i][3] for i in range(0,diff)])

