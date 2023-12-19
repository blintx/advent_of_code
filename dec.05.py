data = []
seeds = []
seed_to_soil =[]
soil_to_fertilizer= []
fertilizer_to_water= []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

with open('data/input5.txt','r',encoding='utf_8')as f :
    for i in f.readlines():
        data.append(i.strip())
        
dictionary = {}  
index = 0
count= 0
while index < len(data):
    if data[index] == '':
        data[index] = int(count)
        count += 1
        
    index += 1


dictionary = {}  
count = 0
for i in range(len(data)):
    # print(str(type(data[i])))

    if ('int' in str(type(data[i]))):
        print('x')
        # print(data[i+2:data.index(count+1)])
        # print(data[i+1])
        
        if 0<=count <7:
            dictionary.update({data[i+1]:data[i+2:data.index(count+1)]})
            
            
        else:
            dictionary.update({data[i+1]:data[i+2:]})
        count+=1
        print(count)
            
        
        




data_2 = []
print(dictionary)


dictionary.update({data[0].split(':')[0]:data[0].split(':')[1].replace(' ','',1).replace(' ',';').split(';')})