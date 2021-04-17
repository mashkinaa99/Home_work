phone_number = input('Enter your phone number (no more than 10 characters): ')
if len(phone_number) <= 10 and phone_number.isdigit():
    print('Thank you')
elif len(phone_number) > 10:
    print('Error. Phone number must not be longer than 10 characters')
else:
    print('Error. Do not use letters when entering data.')
