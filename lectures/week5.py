import os
from practice import toolkit_config as cfg
IOS=os.path.join(cfg.DATADIR, 'iso.txt')


def freqword(filepath):
    with open(filepath) as file:
        counts =dict()
        for line in file:
            words=line.split()
            for word in words:
                counts[word]=counts.get(word,0)+1
        maxcount=None #FIND THE MOST frequent word
        maxword=None
        for word,count in counts.items():
            if maxcount is None or count > maxcount :
                maxcount= count
                maxword = word
    return(f"The most frequent word is:{maxword},and the number of times appeared is:{maxcount}")
freqword('iso.txt')


