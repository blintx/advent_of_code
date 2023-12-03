maxos = {'red':12, 'green' :13, 'blue': 14}
output = []
f = open('data/input2.txt', 'r',encoding='utf-8')
file = f.readlines()
f.close()
f = file[:]
f = map(lambda x : x.strip(),f)


f = map(lambda x : x.split(':'),f)
f=list(f)
for i in range(len(f)):
    
    f[i] = map(lambda x : x.split(';'),f[i])
    f[i]=list(f[i])
    for j in range(len(f[i])):
        f[i][j] = map(lambda x : x.split(','),f[i][j])
        f[i][j]=list(f[i][j])
        
        
        for k in range(len(f[i][j])):
            f[i][j][k] = map(lambda x : x.split(' '),f[i][j][k])
            f[i][j][k]=list(f[i][j][k])
f=list(f)


for i in range(len(f)):
    f[i][0][0][0] = i+1

for x in range(len(f)):
    hiba = False
    for i in range(len(f[x][1])): 
        
        for j in range(len(f[x][1][i])): 
             # 1 fajta
            if int(f[x][1][i][j][1]) > maxos[f[x][1][i][j][2]] and hiba == False: 
                output.append(f[x][0][0][0])
                hiba = True
        
lista = [i for  i in range(1,101)]
for i in range(len(output)): 
    lista.remove(output[i])
print(lista)    
print(output)
print(sum(lista))
