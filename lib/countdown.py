import time

def countdown(num):
    while num >= 1:
        print(f"{num} SECONDS()!")
        num -= 1
    print("HAPPY NEW YEAR!")

countdown(5)

def countdown_with_sleep(num2):
    while num2 >= 1:
        print(f"{num2} SECONDS()!")
        num2 -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")

countdown_with_sleep(8)

