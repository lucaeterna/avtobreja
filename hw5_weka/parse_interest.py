import csv

header = ('prevword', 'nextword', 'prevtag', 'nexttag', 'class')
rows = []
punct = '”“".,«»\\/*!:;—()\'-%`.?'

with open('interest.acl94.txt', 'r', encoding='utf-8') as i:
    for line in i:
        if '$$' in line:
            continue
        line = line.strip().replace('[', '').replace(']', '')
        words = line.split()
        for w in range(len(words)):
            try:
                word, tag = words[w].split('/')
                if 'interest' in word and '_' in word:
                    cl = word.split('_')[1]
                    prevword, prevtag = words[w - 1].split('/')
                    if prevword in punct:
                        prevword, prevtag = words[w - 2].split('/')
                    nextword, nexttag = words[w + 1].split('/')
                    if nextword in punct:
                        try:
                            nextword, nexttag = words[w + 2].split('/')
                        except IndexError:
                            pass
                    rows.append((prevword.replace(',', '').replace('\'', ''), nextword.replace(',', '').replace('\'', ''), prevtag.replace('$', ''), nexttag.replace('$', ''), cl))
            except ValueError:
                continue


with open('interest.csv', 'w', encoding='utf-8') as w:
    out = csv.writer(w, delimiter=',')
    out.writerow(header)
    out.writerows(rows)
                
