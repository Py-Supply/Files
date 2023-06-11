'''
# write
f = open('example_file.txt', 'w')
f.write('This is an example string\nThis is a new line')
f.close()

# append
f_append = open('example_append_file.txt', 'a')
f_append.write('this is an example string\n')
f_append.close()


# read
f_read = open('example_append_file.txt', 'r')
print(f_read.read())
'''

fruit = ['oranges', 'apples', 'bananas', 'blueberrys']

userinput = 0
while userinput != 5:
    print('Menu:')
    print('1. Oranges')
    print('2. Apples')
    print('3. Bananas')
    print('4. Blueberrys')
    print('5. Exit')
    print('6. Previous selections')
    print('7. Clear previous selections')
    userinput = int(input())
    if userinput >= 0 and userinput <= 4:
        print('You chose: ' + fruit[userinput - 1])
        f = open('fruit_selection.txt', 'a')
        f.write(fruit[userinput - 1] + '\n')
        f.close()
    if userinput == 6:
        f = open('fruit_selection.txt', 'r')
        print(f.read())
        f.close()
    if userinput == 7:
        f = open('fruit_selection.txt', 'w')
        f.write('')
        f.close()
        