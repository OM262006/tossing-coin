import random 
score = 0
while True:
    user = input("Enter T to toss the coin and E to exit: ").lower()
    if user == "t":
        print("Coin is tossing...")
        coin = random.choice(["heads", "tails"]).lower()
        
        if coin == "heads":
            print("You got heads. Congratulations!")
            score += 1
            print("Number of times you tossed:", score)
            print("Your total score:", score)
            break
        else:
            print("You got tails. Try once again.")
            score +=1
            print("Number of times you tossed:", score)
        print("Your total score:", score)    
  

    elif user == "e":
        print("Thank you for playing.")
        break
    else:
        print("Invalid input")
