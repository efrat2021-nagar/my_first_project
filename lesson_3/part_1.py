# if prices in ILS add 10% TAX
#     if prices in $ add 20% TAX
#     the results in 2 lists
prices =['25$' , '50$' , '48ILS' , '34$']
prices_ILS = prices[0]
prices_dolars = prices[0]
for price in prices:
    if 'ILS' in price:
        price = price.replace('ILS','')
        price_as_int = int(price)
        price_with_tax = price_as_int*1.18
        print (f'{price_with_tax} ILS added to ILS list')

    elif '$' in price:
        price=price.replace('$','')
        price_as_int = int(price)
        price_with_tax = price_as_int*1.2
        print(f'{price_with_tax} dollars added to dollars list')

    else:
        print ('price include value that can not be calculated')

    print('Test End')
