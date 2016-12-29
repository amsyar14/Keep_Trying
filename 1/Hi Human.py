print('Hello Human')                          # just a greet
print('My name is EZ, What yours human ?')     # asking for human name

human_name = input('Your Name : ')   # human type the name

#while human_name != str():                             # prevent Human from typing numbers
#    print('Name only have words Human, not numbers')   #
#    print('please type your name Human')               #
#    human_name = input('Your Name:')                               #

print('Nice to meet you ' + human_name)
print('How old are you ' + human_name + ' ?')   # asking for human age

human_age = int(input('your age : '))   # human type the age

while human_age > 117:
        print('I know I ask you to type your age, but you must not be that old right')
        human_age = int(input('please type your real age : '))
        continue

if human_age <= 12:
    print('you are still a child I see')   # check age
elif human_age <= 18:
    print('you are a teenager I see')
elif human_age > 18:
    print('you are adult I see')

#print()

#print('Do you want to play a game ' + human_age + ' ? yes or no ?')

#human_game = input()

#if human_game == yes:
#    import random
#    print('Nice, ok let start')
#    num1 = random.randint(0,99)

#    print('Try to think numeber')