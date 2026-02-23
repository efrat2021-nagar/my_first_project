def age_calculator(age):
    if age >= 18:
        print ('Age is greater than 18')
    else:
        print ('Age is less than 18')
    return age

    # stating the code

user_1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'efrat@com',
    'age': 21,

}
user_2 = {
    'first_name': 'Efrat',
    'last_name': 'Nagar',
    'email': 'eft@com',
    'age': 16,

}


age_1 = age_calculator(user_1['age'])
age_2 = age_calculator(user_2['age'])


# if user_1['age'] >18:
#     print ('age is greater then 18')
# else:
#     print ('age is less than 18')
#
# if user_2['age'] >18:
#     print ('age is greater then 18')
# else:
#     print ('age is less than 18')