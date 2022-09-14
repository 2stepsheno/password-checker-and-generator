import random
import string
symbols = '!$%^&*()_-=+'
capAlp = 'ABCDEFGHIGKLMNOPQRSTUVWSYZ'
smaAlp = 'abcdefghigklmnopqrstuvwxyz'
num = '1234567890'
characters = list(string.ascii_letters + string.digits + '!$%^&*()_-=+')
value = True
while value == True:
    print(f'--------------------\n1.Check Password\n2.Generate Password\n3.Quit')
    choice = int(input('Enter your choice: '))
    ##password generator:
    if choice == 2:
        def generator():
            length = int(input('Enter your length of the password'))
            if length > 8 and length < 24:
                random.shuffle(characters)
                password = []
                for i in range(length):
                    password.append(random.choice(characters))
                random.shuffle(password)
                print("".join(password))
            else:
                print('invalid length')
        generator()
    ##quit
    if choice == 3:
        quit()
    ##password checker:
    if choice == 1:
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        u, l, s, n = 0, 0, 0, 0
        score = u + l + s + n
        user_input = input('Enter your password: ')
        if len(user_input) < 8 or len(user_input) > 24:
            print('invalid length')
        else:
            for i in user_input:
                if (i in capAlp):
                    u += 5
                    flag1 = True
                if (i in smaAlp):
                    l += 5
                    flag2 = True
                if (i in symbols):
                    s += 5
                    flag3 = True
                if (i in num):
                    n += 5
                    flag4 = True
                if flag1 == True and flag2 == True and flag3 == True and flag4 == True:
                    score += 10

            if score < 10:
                print(f'{score}, weak password.')

            if score > 30:
                print(f'{score}, strong password.')

            if score > 10 and score < 30:
                print(f'{score}, fine password.')