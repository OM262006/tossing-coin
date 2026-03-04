import random

score = 0

while True: 
    user = input("enter t to toss the coin and e to exit:").lower()
    coin = random.choice(['Heads', 'Tails']).lower()
    if user == "t":
        print("coin is tossing...")
        if coin == "heads":
            print("its heads congratulations")
            score += 1
            print("number of times u tossed",score)
            break
        else: 
            print("its tails better luch next time")
            score += 1
            print("number of times u tossed",score)
    elif user == "e":
        print("thank you for playing")
        break
