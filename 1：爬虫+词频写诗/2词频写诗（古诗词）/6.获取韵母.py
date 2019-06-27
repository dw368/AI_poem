rhythm=''
rhythmList=['a','e','i','o','u','v']
verse=pinyin.get(noun,format='strip')
ind=0
for p on range(len(verse)-1,-1,-1):
    if verse[p] in rythmList:
        ind=p
    rhythm=verse[ind:]
