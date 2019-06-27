import jieba
txt = open('zzcfshi.txt','r',encoding='utf-8').read()
file_handle=open('词频统计结果.txt',mode='w')
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        reword = word
        counts[reword] = counts.get(reword, 0) + 1
#转换格式，输出
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(200):
    word, count = items[i]
    file_handle.write('{0:<5}{1:>5}次'.format(word, count)+'\n')
file_handle.close()
