def main():
    #get two numbers
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    # divide num1 by num2
    #result is stored in variable named called output
    #1,2,3,4,5, etc but except 0.
    if num2 != 0: 
        output = num1 / num2

    #display the result
        print(f'{num1} divided by {num2} is {output}') 
    # in case of num2 == 0
    else:
        print('Cannot divide by zero')

if __name__ == '__main__':
    main()