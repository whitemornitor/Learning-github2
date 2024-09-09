    # creating password for the user

print("Welcome to Timmy Academy :)")

player = input("Did you have an existing account? ").lower()

if player == "no":
    ask_user = input("Will you create one now? ")
    if ask_user != "yes":
        quit()
    
    # Prompt the user to create his/her account
    print("\nPlease fill the form below >>>\n")
    name1 = input("First Name? ").title()
    name2 = input("Last Name? ").title()
    user = input("Password? ")

# Store the user password
    password = " "

# variable to monitor how user log in
    password_count = 0
    password_limit = 3
    out_of_password = False 

    print(f"Congratulaion {name1}, you just created an account!")

#Ask user after creating password if he/she is willing to log in
    ask = input(f"Did you want to log in now {name1}? ").lower()

    if ask != "yes":
        quit()

 # Create while loop to continue prompting the user for certain limit if the user entered incorrect password
    while password != user and not(out_of_password):
        if password_count < password_limit:
            password = input("Please log in: ")
            if password != user:
                print(f"Error, try again {password_limit - (password_count + 1)} trial left")
            password_count += 1

        else:
            out_of_password = True
 
    if out_of_password:
        print("Invalid password")

    else:
        print("Log in successfully\n")
        print("Now you can play your game :)")
        print(f"Hello {name1}, Welcome to my program!\n")

        user = input(f"Should we procced for the quize {name1}? ").lower()

        if user != "yes":
            quit()

        else:
           print("Okay! Let go then :)\n")
        

        import random
        print("There are two(2) Games here, kindly choose your favourit one")
        print("A) Guessing game\nB) Quize game")
        answer = input("Make your choice: ").upper()

        # Check the condition of the user
        if answer == "A":
            # First game: Random choosen number
             
            top_range_number = input("\nEnter a number: ")
            if top_range_number.isdigit():                # Convert user string to integer
                top_range_number = int(top_range_number)

                # Check maybe the number is less than zero. If it is, tell the user to ener a number greater than zero next time and quit
                if top_range_number <= 0:
                    print("Please type number higher than 0 next time")
                    quit()

            else:
                print("Please type a number next time")
                quit()

            random_number = random.randrange(0, top_range_number)
            guesses = 0

            # Use while loop to ask the user to guess the random number generated
            while True:
                guesses += 1
                user_guesses = input("Make a guess: ")
                if user_guesses.isdigit():
                    user_guesses = int(user_guesses)

                else:
                    print("Please type a number next time")
                    continue

                if user_guesses == random_number:
                    print("You guess right!")
                    break

                elif user_guesses > random_number:
                    print("You were above the number!")

                else:
                    print("You were below the number!")
            print("You got it in", guesses, "guesses")

        # Second Game: Quize game
        elif answer == "B":
            print("Welcome to our Quize :)")
            score = 0
            que1 = input("What is the full meaning of CPU? ")
            if que1.lower() == "central processing unit":
                print("Wow Correct!\n")
                score +=1
            else:
                print("Incorrect!\n")


            que2 = input("What is the full meaning of LED? ")
            if que2.lower() == "light emitting diode":
                print("Wow Correct!\n")
                score +=1
            else:
                print("Incorrect!\n")

            que3 = input("What is the full meaning of GPU ")
            if que3.lower() == "graphic processing unit":
                print("Wow Correct!\n")
                score +=1
            else:
                print("Incorrect!\n")

            que4 = input("What does PSU stand for?  ")
            if que4.lower() == "power supply":
                print("Wow Correct!\n")
                score += 1
            else:
                print("Incorrect!\n")

            print("You scored " + str(score) + " correctly")
            print("You got " + str((score / 4) * 100) + "%")

        else:
            print("Not available yet")
            quit()


else: 
    print("You don't have account here, kindly create one")
    quit()

  