# data =['Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53','Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19','Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1','Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83','Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36','Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
data = []

with open('data/input4.txt', 'r', encoding='utf-8')as f:
    for line in f.readlines():
        data.append(line.strip())

dictionary = {}

separate_card = lambda x: [x.split(':')[0].replace('Card','').replace(' ',''),x.split(':')[1].replace(' ','',1).replace('  ',' ').replace(' | ','|').replace(' ',';').split('|')]

for j in range(len(data)):
    tmp = separate_card(data[j])
    
    dictionary.update({tmp[0]:tmp[1]})
    
    dictionary[tmp[0]] = [dictionary[tmp[0]][0].split(';'),dictionary[tmp[0]][1].split(';')]
    
    if dictionary[tmp[0]][0][0] == '':
        del dictionary[tmp[0]][0][0]
    if dictionary[tmp[0]][1][0] == '':
        del dictionary[tmp[0]][1][0]
    

    dictionary[tmp[0]][0] = list(map(lambda x:int(x),dictionary[tmp[0]][0]))
    dictionary[tmp[0]][1] = list(map(lambda x:int(x),dictionary[tmp[0]][1]))

    point = 0
    for i in dictionary[tmp[0]][1]:
        if i in dictionary[tmp[0]][0]:
            point +=1
    dictionary[tmp[0]] = point




for i in dictionary.keys():
    dictionary[i] = [1,dictionary[i]]
    



szumma = 0
for x in dictionary.keys():
    for j in range(dictionary[x][0]):
        for i in range(int(x)+1,dictionary[x][1]+1+int(x)):
            dictionary[str(i)][0]+=1
            
for x in dictionary.keys():
    szumma += dictionary[x][0]
    
    
    
print(szumma)

            
            

        
        
        
    









