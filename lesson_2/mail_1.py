mails = ["abc@aa.com" , "sss.com" , "sss@reee.com"]
for mail in mails:
    if '@' in mail:
        print(f'{mail} is a valid mail')
else:
    print (f'{mail} is not a valid mail')


