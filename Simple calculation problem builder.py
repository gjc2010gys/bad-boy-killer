import random

def panduan():
    global right
    global channe
    if answer == guest:
        print("You are rigth！")
        right = right + 1
        print("You got the ", right, " question correctly.")
    else:
        print("You are wrong！The answer is", plus2)
    return right

def panduan2():
    global right
    global channe
    if plus2 == guest:
        print("You are rigth！")
        right = right + 1
        print("You got the ", right, " question correctly.")
    else:
        print("You are wrong！The answer is", plus2)
    return right

def MakeAnswer():
    global mode,plus1,plus2
    mode = random.randint(1, 4)
    plus1 = random.randint(smallest, bigest)
    plus2 = random.randint(smallest, bigest)
    return mode,plus1,plus2

def CheckWrong(InputSay):
    Wrong = True
    global temp
    while Wrong:
        try:
            temp = int(input(InputSay))
        except ValueError:
            print('Input Wrong!You only can input int number!')
        else:
            Wrong =  False
    return temp


CheckWrong("Please enter the minimum value of the answer.")
smallest = temp
CheckWrong("Please enter the maximum value of the answer.")
bigest = temp
right = 0

while True:
    MakeAnswer()
    if mode == 1:

        answer = plus1 + plus2
        print(plus1, "+", plus2, end=" ")
        guest = eval(input("="))

        panduan()

    elif mode == 2:

        answer = plus1 * plus2  # 积=乘数*乘数
        print(plus1, "*", plus2, end=" ")
        guest = eval(input("="))

        panduan()

    elif mode == 3:

        beichushu = plus1 * plus2  # 被除数=商*除数
        print(beichushu, "÷", plus1, end=" ")
        guest = eval(input("="))

        panduan2()

    else:

        beijianshu = plus1 + plus2  # 被减数=差+减数
        print(beijianshu, "-", plus1, end=" ")
        guest = eval(input("="))

        panduan2()