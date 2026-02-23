from operator import index

full_name = "leo messi"
len_full_name = len(full_name)
print(len_full_name)
full_name = full_name.replace("leo messi", "leonid " )
index = full_name.index(" ")
first_name = full_name[0:index]
last_name = full_name[index:len_full_name:]
print (f'first_name is {first_name} last_name is {last_name}')
signal_char = full_name[4]
primt = (f'first_name is {first_name} last_name is {last_name} signal_char is {signal_char}')
print(full_name)

