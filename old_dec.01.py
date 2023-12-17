words = {'zero':0,'one':1,'eight':8,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'nine':9}

def string_to_list(string):
    list = [i for i in string]
    return list

def number_to_str(string):
    for i in string_to_list(string):
        if ''.join(i) in words.keys():
            string=string.replace(''.join(i),str(words[''.join(i)]),1)
        for j in string_to_list(string):
            if ''.join([i,j]) in words.keys():
                string=string.replace(''.join([i,j]),str(words[''.join([i,j])]),1)
            for x in string_to_list(string):
                if ''.join([i,j,x]) in words.keys():
                    string=string.replace(''.join([i,j,x]),str(words[''.join([i,j,x])]),1)
                for z in string_to_list(string):
                    if ''.join([i,j,x,z]) in words.keys():
                        string=string.replace(''.join([i,j,x,z]),str(words[''.join([i,j,x,z])]),1)
                    for y in string_to_list(string):
                        if ''.join([i,j,x,z,y]) in words.keys():
                            string=string.replace(''.join([i,j,x,z,y]),str(words[''.join([i,j,x,z,y])]),1)
    return string


def counter1(string):
    output =[]
    numbers = []
    for i in words.keys():
        if i in string:
            numbers.append([words[i],string.index(i)])
    for i in string:
            try:
                
                numbers.append([int(i),string.index(i)])
            except:
                pass
    '''if len(numbers) == 1:
        return [str(numbers[0][0])]'''
    minimum = numbers[0]
    maximum = numbers[0]
    
    for i in range(len(numbers)):
        
        if minimum[1] > numbers[i][1]:
            minimum = numbers[i]
        if maximum[1] < numbers[i][1]:
            maximum = numbers[i]

    output.append(minimum[0]) 
    output.append(maximum[0])
    
    output1 = [str(i) for i in output]
    
    return output1

def counter(x):
    tmp = counter1(x)
    print(tmp)
    #tmp = tmp[0],tmp[-1]
    tmp = ''.join(tmp)
    
    return tmp


f = open("data/input.txt", "r")
file = f.readlines()
f.close()
f = file[:]
f = map(lambda x : x.strip(),f)

f = map(counter,f)

tmp = [int(i) for i in f]
print(tmp.index(77))
print(sum(tmp))
