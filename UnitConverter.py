print('Welcome to the incredible Unit Converter!','\n',
"For F-to-C, please type 'F'",'\n',
"For C-to-F, please type 'C'",'\n')
selection = input()
if selection == 'F' or selection == 'f':
    print('You have chosen Fahrenheit to Celsius conversion.','\n')
    temp = input('Please enter a temperature in Fahrenheit: ')
    print(str(temp) + ' degrees Fahrenheit is ' + str(round(((int(temp)-32)*(5/9)),2)) + ' degrees Celsius')
elif selection == 'C' or selection == 'c':
    print('You have chosen Celsius to Fahrenheit conversion.')
    temp = input('Please enter a temperature in Celsius: ')
    print(str(temp) + ' degrees Celsius is ' + str(round(((int(temp)*(9/5))+32),2))+ ' degrees Fahrenheit')
else:
    print('Invalid selection')
