name = input('What is your name? ')
email = input('What is your email? ')
phone = input('What is your phone number? ')
job = input('What is your job title? ')

business_card = {
    'name' : name,
    'email' : email,
    'phone' : phone,
    'job' : job
                }
#print(business_card)
print(f'--- Business Card ---\nName: {business_card['name']}\nEmail: {business_card['email']}'
      f'\nPhone: {business_card['phone']}\nJob: {business_card['job']}')