# add your code here
for i in range(1, 101):
    divisible_by_three = i % 3 == 0
    divisible_by_five = i % 5 == 0
    if(divisible_by_three & divisible_by_five):
        print('FizzBuzz')
    elif(divisible_by_three):
        print('Fizz')
    elif(divisible_by_five):
        print('Buzz')
    else:
        print(i)
