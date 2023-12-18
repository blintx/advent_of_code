data = []

with open('data/input5.txt','r',encoding='utf-8')as f :
    for i in f.readlines():
        data.append(i.strip())
        

        

dictionary = {}

dictionary.update({data[0].split(':')[0]:data[0].split(':')[1].replace(' ','',1).replace(' ',';').split(';')})


for i in range(len(data)):
    if data[i] =='':
        data[i+1] = data[i+1].replace(':','')
        dictionary.update({data[i+1]:[]})
        j = 0
        while data[i+j] != '':
            
            dictionary[data[i+1]].append(data[i+j])
            if i+j >= len(data):
                break
            else:
                j+=1
            
        
print(dictionary)      