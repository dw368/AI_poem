import jieba
import jieba.analyse

poetry_file ='zzcfshi.txt'
n_file = 'freqword_n.txt'
v_file = 'freqword_v.txt'
content = open(poetry_file, encoding='utf-8').read()
result_n = open(n_file,'w+',encoding='utf-8')

for x in jieba.analyse.textrank(content, topK=600, allowPOS=('n', 'nr', 'ns', 'nt', 'nz', 'm')):
    result_n.writelines(x+" ")
result_n.close()

result_v = open(v_file,'w+',encoding='utf-8')

for x in jieba.analyse.textrank(content, topK=600, allowPOS=('vg', 'v', 'vd', 'vn')):
    result_v.writelines(x+" ")
result_v.close()

