def read_file(file_path): #file_path is a parameter/variable
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f'File not found because: {nf}')
        
def calculator_menu():
    option = 0 
    optionsList = ['1', '2', '3', '4', '5', '6']
    menuChoices = read_file("Calculator/calculator_options.txt")
      
    while option not in optionsList:
        print(menuChoices)
        
        option = input("Enter an option from the menu choices above: ")
        
        if option not in optionsList:
            print(f'{option} is not a valid choice!!!')
    return option

mainProgram = True #Toggle to False to exit the while loop below
while mainProgram:
    #call the songs menu function and assign it to a variable
    mainMenu = calculator_menu()
    
    #match case is the same as switch in JavaScript
    match mainMenu:
        case "1": 
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            answer = num1 + num2
            print(f'The answer to {num1} + {num2} = {answer}')
        case "2":
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            answer = num1 - num2
            print(f'The answer to {num1} - {num2} = {answer}')
        case "3":
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            answer = num1 * num2
            print(f'The answer to {num1} * {num2} = {answer}')
        case "4":
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            answer = num1 / num2
            print(f'The answer to {num1} / {num2} = {answer}')
        case "5":
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            answer = num1 % num2
            print(f'The answer to {num1} % {num2} = {answer}')
        case _:
            mainProgram = False #set mainProgram variable to false to exit the menu
input("Press enter to exit.....")