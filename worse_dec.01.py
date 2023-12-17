data = ['44']
#data = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}

'''with open('data/input.txt','r',encoding='utf-8')as f:
    
    for i in f.readlines():
        data.append(i.strip())'''

def turn_string_numbers_to_integer(num):
    print(num)
    if  'int' in str(type(num)):
        
        return num
    else:
        return numbers[num]
    
    
    
    

def search_numbers_in_data(data):
    output = []
    for i in range(len(data)):
        numbers_in_word = []
        index_of_numbers_in_word = []
        
        tmp = data[i]
        for x in tmp:
            try:
                x= int(x)
            except ValueError:
                pass
            if 'int' in str(type(x)):
                print(x)
                numbers_in_word.append(x)
                index_of_numbers_in_word.append(tmp.index(str(x)))
                #tmp = tmp.replace(str(x),'',1)
        tmp = data[i]
        
        
        
        for j in numbers.keys():
            tmp = data[i]
            while j in tmp:
                numbers_in_word.append(j)
                index_of_numbers_in_word.append(tmp.index(j))
                tmp =tmp.replace(j,'',1)
            else:
                tmp = data[i]




        frst_num = numbers_in_word[index_of_numbers_in_word.index(min(index_of_numbers_in_word))]
        last_num = numbers_in_word[index_of_numbers_in_word.index(max(index_of_numbers_in_word))]
        print(frst_num, last_num)
        
        
        if max(index_of_numbers_in_word)== min(index_of_numbers_in_word):
            output.append(str(turn_string_numbers_to_integer(frst_num)))
            
        else:
            output_0 = str(turn_string_numbers_to_integer(frst_num)) + str(turn_string_numbers_to_integer(last_num))
            output.append(int(output_0))
    return output
print((search_numbers_in_data(data=data)))