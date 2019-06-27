import bs4,requests,re
file=open('gushi.txt','w',encoding='utf-8')
for i in range(1,1001):
    url= 'https://www.gushiwen.org/shiwen/default_0AA'+str(i)+'.aspx'
    web = requests.get(url)
    soup = bs4.BeautifulSoup(web.text, 'lxml')
    content = soup.select('div[class="main3"]')[0]
    content = content.select('div[class="left"]')[0]
    content = list(content.select('div[class="sons"]'))
    c1=re.compile('<.*?>')
    c2=re.compile('.*?：')
    c3=re.compile(r'\(.*?\)')
    for i in content:
        t=''
        title=str(i.select('b'))
        title=re.sub(c1,'',title)
        title=title.replace('[','')
        title=title.replace(']','')
        author=i.select('p[class="source"]')[0].text
        author=re.sub(c2,'<',author)
        text=i.select('div[class="contson"]')[0].text
        text=re.sub(c3,'',text)
        text = ''.join(text.split())
        t=title+author+'>'+text+'\n'
        t=t.strip(' ').replace('\n','')
        t=t.replace('<','::')
        t=t.replace('>','::')
        file.write(t)
        file.write('\n')
file.close()
