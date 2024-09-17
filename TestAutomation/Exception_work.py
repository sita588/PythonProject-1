try:
    input1=input("Please enter first num: ")
    input2=input("Please enter second num: ")
    c=int(input1)+int(input2)
    print(c)
except:
    print("you entered wrong input, please enter valid input")
finally:
    print("finally block executed")
