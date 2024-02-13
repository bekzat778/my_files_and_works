import random
o = random.randint(1,20)

def gu(l):
    global o
    if o == l:
        print("Good job, KBTU! You guessed my number in 3 guesses!")
        return 0
    elif o > l:
        print("Your guess is too low.")
        l = int(input())
        return gu(l)
    else:
        print("Your guess is too high.")
        l = int(input())
        return gu(l)



print('Hello! What is your name?')

k = input()
print(f"Well, {k}, I am thinking of a number between 1 and 20.")
p = int(input())
gu(p)

