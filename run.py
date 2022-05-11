import sys
import time

# Global Variables


global alien_gun
alien_gun = "no"
global name
name = "input()"


def introdaction():
    """
    Display the story line, title and introduce the user into the game.
    """
    print("All the strugle and the years past, it all been a success. ")
    print("All for achieving the dream of my life.")
    time.sleep(1)
    print("\nMoom, Dad, I will be an astronaute! I will explore the " +
          "universe and I will see the galaxy!")
    time.sleep(1)
    print("\nIt's my time, I need to go, I have a long way ahead " +
          "all the training, and knowledge. Good bye Mom, Dad!")
    time.sleep(1)
    print("Vruum, on my way to the space, as Neil Armstrong said: " +
          "\n\"That's one small step for man, one giant leap for mankind.\"")
    time.sleep(1)
    print("Woow... looks exactly as how I've been dreaming about it! ")
    time.sleep(2)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@        @@       @@@@@@@@@@@        @@  @@@  @@       @@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@  @@@@@  @@@  @@@@@@@@@@@@@@  @@@@@  @@@  @@  @@@@@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@  @@@@@  @@@  @@@@@@@@@@@@@@  @@@@@       @@     @@@@@"
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@  @@@@@  @@@  @@@@@@@@@@@@@@  @@@@@  @@@  @@  @@@@@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@  @@@@@       @@@@@@@@@@@@@@  @@@@@  @@@  @@       @@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@    @@@@@    @@         @@@         @@    @@@@  @@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@  @  @@@  @  @@  @@@@@  @@@  @@@@@  @@  @  @@@  @@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@  @@  @  @@  @@  @@@@@  @@@  @@@@@  @@  @@  @@  @@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@  @@@  @@@@  @@  @@@@@  @@@  @@@@@  @@  @@@  @  @@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@  @@@@@@@@@  @@         @@@         @@  @@@@    @@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@")
    time.sleep(0.1)
    print("@@        @    @@@@@  @    @@@@@@@@@      @@@        @        @  " +
          "@@@   @")
    time.sleep(0.1)
    print("@@  @@@@  @  @  @@@@  @  @  @@@@@@@@  @@@@  @  @@@@  @  @@@@  @  " +
          "@@  @@@")
    time.sleep(0.1)
    print("@@  @@@@  @  @@  @@@  @  @@  @@@@@@@  @@@@  @  @@@@  @  @@@@@@@  " +
          "  @@@@@")
    time.sleep(0.1)
    print("@@        @  @@@  @@  @  @@@  @@@@@@     @@@@        @  @@@@@@@  " +
          "  @@@@@")
    time.sleep(0.1)
    print("@@  @@@@  @  @@@@  @  @  @@@@  @@@@@  @@@@  @  @@@@  @  @@@@@@@  " +
          "@  @@@@")
    time.sleep(0.1)
    print("@@  @@@@  @  @@@@@    @  @@@@@  @@@@  @@@@  @  @@@@  @  @@@@  @  " +
          "@@  @@@")
    time.sleep(0.1)
    print("@@  @@@@  @  @@@@@@   @         @@@@      @@@  @@@@  @        @  " +
          "@@@   @")
    time.sleep(0.1)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@\n\n")
    time.sleep(0.1)
    time.sleep(1)
    print("Starting to acomodate, the training looks easy, everything seems " +
          "amazing, but you cannot wait for the first lunch, for the first " +
          "trip for .... the moon!")
    time.sleep(2)
    start_game()


def start_game():
    """
    The role of this function is to start the game, asking the user to begainn,
    to continue the game, or not.
    If the input has been inserted incorect the user will be asked to introduce
    a corect input.
    """
    while True:
        to_the_moon = input("\nThe Cheif has requested you to join a jurney " +
                            "to the moon! Are you ready for " +
                            "the lifetime jurney?! (yes/no): ").lower()
        if to_the_moon == "no":
            print("\n This was one and the only offer...")
            time.sleep(2)
            print("But, It's your choice... Good luck!")
            time.sleep(3)
            print("\nGame over!")
            play_again()
            break
        elif to_the_moon == "yes":
            get_username()
            break
        else:
            print("\nOoops... you can type just 'yes' or 'no', try again.")
            continue


def get_username():
    """
    If user has choose 'yes', this function will request the username.
    If no input, the user will be asked again to input his username.
    """
    print("\nGreat! You made a life decision!")
    time.sleep(1)
    print("We are proud to have you here today! Your name will be " +
          "in all the newspapers!")
    while True:
        name = input("\nWhat is your name, young astronaute? " +
                     "(type name):").lower()
        if name == "":
            print("This doesn't look like your name, try again.")
            continue
        else:
            print(f'What a great name! Welcome to your life trip, {name} !')
            break
    print("\nEverything is ready, prepare for lunch!")
    time.sleep(1)
    print("3")
    time.sleep(0.2)
    print("2")
    time.sleep(0.2)
    print("1")
    time.sleep(0.2)
    print("Go!")
    time.sleep(0.2)
    print(f'The lunch has been successfully, {name},' +
          'soon you will land on the moon!')
    time.sleep(3)
    print("Prepare to land!")
    while True:
        landing = input("Prepare to land, be carefoul to fallow the " +
                        "landing procedures as you have been trained." +
                        "Have you fallow the landing procedures?" +
                        " (yes/no):").lower()
        if landing == "no":
            print("\nDanger! Danger! Danger!")
            time.sleep(1)
            print("You have crashed!")
            time.sleep(3)
            print("Game over!\n")
            play_again()
            break
        elif landing == "yes":
            print("You have successfully fallowed the landing procedures!")
            landing_string = "\nLanding ..."
            for character in landing_string:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(2)
            print("You have successfully landed on the moon!")
            print(f'Well done, {name}, you arrived on the moon' +
                  'be ready to take your first steps on the moon!')
            time.sleep(3)
            print('The crew has set the life support resources, ' +
                  f'{name}, you can step on the moon now!' +
                  'Keep in mind that you have 100% oxigen in your tank, this' +
                  ' will last aproximative one hour.')
            time.sleep(2)
            print("Don't forget to return to the base once you running low.")
            choice_two()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


# take the gun, or not
def choice_two():
    """
    The game will request from the user to choose if he will pick
    the gun wich will help later. Or not.
    """
    print("\nYour research is going well, unexpected you have seen " +
          "something you are not sure what it is, " +
          "looks like it's covered in dust.")
    time.sleep(1)
    print("Hmm.. let's see what it is....")
    time.sleep(1)
    it_is_a_gun = "IT'S A GUN! It's something that you never seen before."
    for character in it_is_a_gun:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)
    print("\nYou think it's an alien gun, what will you do?")
    while True:
        global alien_gun
        alien_gun = input("Do you take the gun? (yes/no): ").lower()
        if alien_gun == "yes":
            print("\nYou have pick the gun. Who knows when you will need it.")
            break
        elif alien_gun == "no":
            print("\nWhat you don't own, you don't take." +
                  "let's hope you won't regret that later.")
            time.sleep(2)
            print("The alien it's just behind you.")
            time.sleep(0.5)
            print("HE COUGHT YOU!!!!")
            time.sleep(0.5)
            print("GAME OVER!\n")
            play_again()
            break
        else:
            print("That's not quite right, please type 'yes' or 'no'.")
            continue
    time.sleep(2)
    print("What is that? Is that an ...")
    alien = "ALIEN!!!"
    for character in alien:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)
    print("He has saw you!!!")
    while True:
        choice_three = input("What will you do? (stay/hide/run)").lower()
        if choice_three == "stay":
            print("\nYou don't know how to use the gun yet.")
            time.sleep(2)
            print("The alien is running towords you, he is atacking you!")
            time.sleep(3)
            print("GAME OVER!\n")
            play_again()
            break
        elif choice_three == "run":
            print("The alien it's just behind you.")
            time.sleep(2)
            print("HE COUGHT YOU!!!!")
            time.sleep(2)
            print("GAME OVER!\n")
            play_again()
            break
        elif choice_three == "hide":
            print("I think the alien has lost you...")
            time.sleep(2)
            print("Looks like he lost you. Stay down.")
            crew_assist()
            break
        else:
            print("Wrong input. Please choose 'stay', 'hide' or 'run'")
            continue


def crew_assist():
    """
    The game continues where the user will be expose to new challenges
    and he will be requested to choose diferent what he will do next
    """
    oxigen_tank = "The oxigen tank is down to 50%."
    for character in oxigen_tank:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    while True:
        choose_your_next_move = input("What you will do? " +
                                      "(return/continue)").lower()
        if choose_your_next_move == "return":
            print("You are now returning to the spaceship!")
            time.sleep(2)
            print("You heard a cracking. What is happening?")
            time.sleep(1)
            print("You your oxigen is running out!")
            time.sleep(1)
            print("Something has broken your suit. " +
                  "You start loosing your constience")
            time.sleep(3)
            print("GAME OVER!\n")
            play_again()
            break
        elif choose_your_next_move == "continue":
            print("You have alerted the crew, someone will " +
                  "bring you supplies.")
            do_research()
            break
        else:
            print("Wrong input. Please choose 'return' or 'continuee'.")
            continue


def do_research():
    """
    While continue to collect the probes from the moon the user will
    continue meting challanges and will be exposed to the moons
    unknown dangers.
    """
    print("While continue researching, you noticed that you are running low " +
          "on the oxigen tanks. 25% it's what you see on the watch.")
    time.sleep(2)
    radio_string = "RADIO: Crew member: Chhh chhh ... he hit me!\n"
    for character in radio_string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)
    time.sleep(2)
    print("Your team member has been killed by an alien...")
    while True:
        choice_four = input("What do you do next?" +
                            "(return/continue)").lower()
        if choice_four == "return":
            print("You have just 25% oxigen left, you have to move fast!")
            returning_to_the_spaceship()
            break
        elif choice_four == "continue":
            print("You are brave! Continuuing researching is" +
                  " imporatnt for you!")
            time.sleep(2)
            research = "RESERCHING ..."
            for character in research:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.2)
            time.sleep(2)
            print("You have just 2% oxigen left, you start seeing unclear..")
            time.sleep(3)
            print("GAME OVER!\n")
            play_again()
            break
        else:
            print("That's not quite right! Please choose " +
                  "'return' or 'continue'.")
            continue


def returning_to_the_spaceship():
    """
    The user will be supposed to the last challenges of the game and he will
    return home on earth.
    """
    print("You are on your way back to the spaceship," +
          " the supplies are enough for you to return to safety.")
    time.sleep(3)
    print("What is that?")
    time.sleep(1)
    print("It's the alien! He didn't seen you this " +
          "time, now it's your chance!")
    time.sleep(0.5)
    print(f'Do not be scared, {name}!')
    print("Choose one of the below option.")
    print("\n1. Hide yourself wishing that he won't see you.")
    print("\n2. Kill the alien, and take his body with you to the spaceship")
    if alien_gun == "yes":
        alien_text = "(1 or 2)"
    else:
        alien_text = "Please choose the option 1 or 2."
    while True:
        try:
            your_chance = int(input('What do you do next?' +
                                    'ill the alien with the gun ' +
                                    'or hide until he will' +
                                    f'leave? {alien_text}:'))
            if your_chance == 1:
                print("That's a good choice, choosing safety is fine.")
                time.sleep(2)
                print("The alien sees you!")
                time.sleep(2)
                print("He is running toword you pointing his gun at you!")
                time.sleep(3)
                print("\nGAME OVER!")
                play_again()
                break
            elif your_chance == 2:
                print('The alien hasan\'t seen you! Now is your ' +
                      f'chance {name} shut!')
                time.sleep(3)
                print("You hit him! He's dead!")
                time.sleep(1)
                print("You can now take his body to earth," +
                      "that's a great discovery!")
                time.sleep(2)
                print("You might return to the spaceship now!")
                time.sleep(4)
                print("You have prepared the ship, you are ready to lunch!")
                back_to_earth()
                break
            else:
                print(f"Wrong number. Please type {alien_text}.")
                continue
        except ValueError:
            print(f"Wrong Input. Please type in a number {alien_text}.")
            continue


def back_to_earth():
    """
    This function will take the user back to earth,
    he will be exposed to one of his last challenges before ending the game.
    """
    print("Looks like the spaceship has been damaged when you shut the alien!")
    while True:
        spaceship_repair = input("What will you do? Do you consider " +
                                 "repairing the spaceship? " +
                                 "Or your experience is telling you that " +
                                 "you can fly like that? (repair/fly)").lower()
        if spaceship_repair == "fly":
            print("Your instincts are strong, you can do it!")
            time.sleep(3)
            danger = "DANGER! DANGER!\n"
            for character in danger:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.2)
            time.sleep(2)
            print("The ship has serios damage!")
            mayday = "Mayday! Mayday! Mayday"
            for character in mayday:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.2)
            print("GAME OVER!\n")
            play_again()
            break
        elif spaceship_repair == "repair":
            print("That's a good coice!")
            repair = "REPAIRING ..."
            for character in repair:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.2)
            time.sleep(2)
            print("The repairs are ready! You can now return home!")
            home_sweet_home()
            break
        else:
            print("Wrong input! Please choose 'repair' or 'fly'!")
            continue


def home_sweet_home():
    """
    The storyline will continue and congratulate the astronaute for the
    successfully mision.
    """
    print(f'Well done {name}, you have successfully return home!')
    time.sleep(2)
    print(f'Welcome back, {name} !')
    time.sleep(1)
    print("The alien that you have brought back from the moon has been taken" +
          "by the sciencists from Area 51! You are a hero!")
    time.sleep(2)
    print("You have won the game! You are ready to be a real astronaute!")
    print("Winner winner chicken dinner!")
    while True:
        next_move = input(f'\nWhat will you do next, {name}?' +
                          ' (leave/PlayAgain)').lower()
        if next_move == "leave":
            print(f'Thank you for playing my game! Good bye, {name} !')
            break
        elif next_move == "PlayAgain":
            print("That's a good choice, more training before the real thing!")
            play_again()
            break
        else:
            print("Please input a correct choice! (leave/PlayAgain")
            continue


# restart game
def play_again():
    """
    This function will be called everytime when the user will die in the
    challenges if not a good bye message will be displayed. If yes,
    a play_game function is called again.
    """
    while True:
        rplay_again = input("You can't die now! Try again? (yes/no):").lower()
        if rplay_again == "yes":
            introdaction()
            break
        elif rplay_again == "no":
            print("\n That's not what we expected... Thank you for playing!")
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


introdaction()
