from operator import index

names = ['efrat', 'vered', 'matan', 'kobi']
cities = ["lod","london","paris" ]
grades = [78,56,90,89]

for name in names:
    print (name)
    l=len(name)
    print(f'the len of name is {l}')

city_index_1 = cities [1]
length_of_list = len(cities)
lod_counter = cities.count('lod')
is_rome = "Rome" in cities
is_madrid = "Madrid" in cities

print(f'is madrid is {is_madrid}')
print(f'is rome is {is_rome}')