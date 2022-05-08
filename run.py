import sys
import time

#Global Variables

global alien_gun
alien_gun = "no"

def introdaction():
    """
    Display the story line, title and introduce the user into the game.
    """
    print("All the strugle and the years past, it all been a success.")
    print("All for achieving the dream of my life.")
    time.sleep(3)
    print("Moom, Dad, I will be an astronaute! I will explore the\n" +
    "universe and I will see the galaxy!")
    time.sleep(2)
    print("It's my time, I need to go, I have a long way ahead\n" +
    "all the training, and knowledge. Good bye Mom, Dad!")
    time.sleep(1)
    print("Vruum, on my way to the space, as Neil Armstrong said\n" + 
    "\"That's one small step for man, one giant leap for mankind.\"")
    time.sleep(1)
    print("Woow... looks exactly as how I've been dreaming about it")
    time.sleep(2)
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(" @@@@@@@@        @@       @@@@@@@@@@@        @@  @@@  @@       @@@@@@@@@@")
    print(" @@@@@@@@@@@  @@@@@  @@@  @@@@@@@@@@@@@@  @@@@@  @@@  @@  @@@@@@@@@@@@@@@")
    print(" @@@@@@@@@@@  @@@@@  @@@  @@@@@@@@@@@@@@  @@@@@       @@     @@@@@@@@@@@@")
    print(" @@@@@@@@@@@  @@@@@  @@@  @@@@@@@@@@@@@@  @@@@@  @@@  @@  @@@@@@@@@@@@@@@")
    print(" @@@@@@@@@@@  @@@@@       @@@@@@@@@@@@@@  @@@@@  @@@  @@       @@@@@@@@@@")
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(" @@@@@@@@@@@@    @@@@@    @@         @@@         @@    @@@@  @@@@@@@@@@@@")
    print(" @@@@@@@@@@@@  @  @@@  @  @@  @@@@@  @@@  @@@@@  @@  @  @@@  @@@@@@@@@@@@")
    print(" @@@@@@@@@@@@  @@  @  @@  @@  @@@@@  @@@  @@@@@  @@  @@  @@  @@@@@@@@@@@@")
    print(" @@@@@@@@@@@@  @@@  @@@@  @@  @@@@@  @@@  @@@@@  @@  @@@  @  @@@@@@@@@@@@")
    print(" @@@@@@@@@@@@  @@@@@@@@@  @@         @@@         @@  @@@@    @@@@@@@@@@@@")
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(" @@        @    @@@@@  @    @@@@@@@@@      @@@        @        @  @@@   @")
    print(" @@  @@@@  @  @  @@@@  @  @  @@@@@@@@  @@@@  @  @@@@  @  @@@@  @  @@  @@@")
    print(" @@  @@@@  @  @@  @@@  @  @@  @@@@@@@  @@@@  @  @@@@  @  @@@@@@@  @  @@@@")
    print(" @@        @  @@@  @@  @  @@@  @@@@@@     @@@@        @  @@@@@@@    @@@@@")
    print(" @@  @@@@  @  @@@@  @  @  @@@@  @@@@@  @@@@  @  @@@@  @  @@@@@@@  @  @@@@")
    print(" @@  @@@@  @  @@@@@    @  @@@@@  @@@@  @@@@  @  @@@@  @  @@@@  @  @@  @@@")
    print(" @@  @@@@  @  @@@@@@   @         @@@@      @@@  @@@@  @        @  @@@   @")
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")
    time.sleep(2)
    print("Starting to acomodate, the training looks easy, everything seems\n" +
    "amazing, but you cannot wait for the first lunch, for the first trip\n" + 
    "for .... the moon!")
    time.sleep(3)
    start_game()

def start_game():
    """
    The role of this function is to start the game, asking the user to begainn,
    to continue the game, or not.
    If the input has been inserted incorect the user will be asked to introduce
    a corect input.
    """
    while True:
        to_the_moon = input("The Cheif has requested you to join a jurney " +
                            "to the moon! Are you ready for " + 
                            "the lifetime jurney?! (yes/no):\n" )
        if to_the_moon == "no":
            print("\n This was one and only offer...")
            time.sleep(2)
            print("But, It's your choice... Good luck!")
            time.sleep(3)
            print("Game over!\n")
            play_again()
            break
        elif to_the_moon == "yes":
            get_username()
            break
        else:
            print("Ooops... you can type just 'yes' or 'no', try again.")
            continue


def get_username():
    """
    If user has choose 'yes', this function will request the username.
    If no input, the user will be asked again to input his username.
    """
    print("\nGreat! You made a life decision!")
    time.sleep(2)
    print("We are proud to have you here today! Your name will be " + 
          "in all the newspapers!")
    while True:
        name = input("What is your name, young astronaute? (type name):\n")
        if name == "":
            print("This doesn't look like your name, try again.")
            continue
        else:
            print(f"What a great name!" + 
            "Welcome to your life trip, " + {name} + "!")
            break
    print("Everything is ready, prepare for lunch!")
    time.sleep(1)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("Go!")
    time.sleep(0.5)
    print("The lunch has been successfully, " + {name} + "," + 
          "soon you will land on the moon!")
    time.sleep(3)
    print("Prepare to land!")
    while True:
        landing = input("Prepare to land, be carefoul to fallow the " +
                            "landing procedures as you have been trained." + 
                            "Have you fallow the landing procedures? (yes/no):\n" )
        if landing == "no":
            print("\n Danger! Danger! Danger!")
            time.sleep(2)
            print("You have crashed!")
            time.sleep(3)
            print("Game over!\n")
            play_again()
            break
        else landing == "yes":
        print("You have successfully fallowed the landing procedures!")
        continue

    landing_string = "Landing ...\n"
    for character in landing_string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(2)
    print("You have successfully landed on the moon!")
    print("Well done," + {name} + ", you arrived on the moon " 
    "be ready to take your first steps on the moon!")
    

    