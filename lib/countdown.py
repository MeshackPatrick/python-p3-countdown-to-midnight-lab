# your code goes here!
import time
def count_down(num):
    while num > 0:
        print(f"{num} SECONDS(S)!")
        num -= 1
    print("HAPPY NEW YEAR !")

def count_down_with_sleep(num):
    while num > 0:
        print(f"{num} SECONDS(S)!")
        time.sleep(1)
        num -= 1
    print("HAPPY NEW YEAR !")
