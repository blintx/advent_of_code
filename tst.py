string ='eighthree'

words = {'one':1,'eight':8,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'nine':9}


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










def counter(string):
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
    
    minimum = numbers[0]
    maximum = numbers[0]
    for i in range(len(numbers)):
        
        if minimum[1] > numbers[i][1]:
            minimum = numbers[i]
        if maximum[1] < numbers[i][1]:
            maximum = numbers[i]

    output.append(minimum[0]) 
    output.append(maximum[0]) 
    
    return output
print(counter(string))
    



print([4])