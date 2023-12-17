def printer(list):
    for i in list:
        print(i)

number = ['1', '2', '3', '4', '5', '6', '7', '8','9']

def számláló(i,j):
    if file[i][j] in number and file[i][j+1] in number and file[i][j+2]  in number:
        parts.append(int(''.join([file[i][j],file[i][j+1],file[i][j+2]])))
    if file[i][j] in number and file[i][j-1] in number and file[i][j-2]  in number:
        parts.append(int(''.join([file[i][j-2],file[i][j-1],file[i][j]])))
    if file[i][j] in number and file[i][j+1] in number and file[i][j-1]  in number:
        parts.append(int(''.join([file[i][j-1],file[i][j],file[i][j+1]])))
    if file[i][j] in number and file[i][j+1] in number and file[i][j-1] not in number:
        if j +2>len(file[i])-1:
            parts.append(int(''.join([file[i][j],file[i][j+1]])))
        elif file[i][j+2] not in number:
            parts.append(int(''.join([file[i][j],file[i][j+1]])))
    if file[i][j] in number and file[i][j-1] in number and file[i][j+1] not in number:
        if j-2<0:
            parts.append(int(''.join([file[i][j-1],file[i][j]])))
        elif file[i][j-2] not in number:
            parts.append(int(''.join([file[i][j-1],file[i][j]])))
        
        

f = open('data/input3.txt','r',encoding='utf-8')
file = f.readlines()
f.close()
file = list(map(lambda x:list(x.strip()), file))
parts = []
for i in range(len(file)):
    for j in range(len(file[i])):
        if file[i][j] in number:
            if 0<=j < len(file[i])-1 and 0<=i < len(file)-1:
                if (file[i][j+1] not in number and file[i][j+1] != '.'):
                    számláló(i,j)
                if (file[i-1][j] not in number and file[i-1][j]!= '.'):
                    számláló(i,j)
                if (file[i][j-1] not in number and file[i][j-1]!= '.'):
                    számláló(i,j)
    
                if (file[i][j+1] not in number and file[i][j+1]!= '.'):
                    számláló(i,j)
            
            
                if (file[i-1][j+1] not in number and file[i-1][j+1] != '.'):
                    számláló(i,j)
                if i < len(file)-1:
                    if (file[i+1][j+1] not in number and file[i+1][j+1] != '.'):
                        számláló(i,j)
                    if (file[i+1][j-1] not in number and file[i+1][j-1] != '.'):
                        számláló(i,j)
                    
                if (file[i-1][j-1] not in number and file[i-1][j-1] != '.'):
                    számláló(i,j)
print(parts)

for i in parts:
    if i == parts[parts.index(i)+1]:
        parts.remove(i)
        
print(parts)
print(sum(parts))