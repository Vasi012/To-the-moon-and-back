import sys
import time
import pyfiglet
from colorama import init, Fore, Back, Style
init(autoreset=True)

# Global Variables

global alien_gun
alien_gun = "no"


def introduction():
    """
    Display the story line, title, and introduce the user into the game.
    """
    print("Welcome to the moon and back game, " +
          "this game is a fiction game, where you " +
          "will be exposed to different challenges, " +
          "all starting from the idea of traveling to "
          "the moon. \nThroughout the game you will need " +
          "to input answers in order to pass to the next " +
          "challenge, bear in mind that you have just one " +
          "chance to win! Enjoy and have fun!")
    time.sleep(4)
    print("\n\nAll the struggle and the past years, it all " +
          "been a success. ")
    print("\nAll for achieving the dream of my life.")
    time.sleep(2)
    print("\nMom, Dad, I will be an astronaut! I will explore the " +
          "universe and I will see the galaxy!")
    time.sleep(2)
    print("\nIt's my time, I need to go, I have a long way ahead " +
          "all the training, and knowledge. Good bye Mom, Dad!")
    time.sleep(3)
    print("\nVroom, on my way to the space, as Neil Armstrong said: " +
          "\n\"That's one small step for man, one giant leap for mankind.\"")
    time.sleep(1)
    print("Wow... looks exactly as I've been dreaming about it! ")
    time.sleep(4)
    print(Fore.CYAN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@@@@@@@@@@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@        @@       @@@@@@@@@@" +
          "@        @@  @@@  @@       @@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@  @@@@@  @@@  @@@@@@@" +
          "@@@@@@@  @@@@@  @@@  @@  @@@@@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@  @@@@@  @@@  @@@@@@@@"
          "@@@@@@  @@@@@       @@     @@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@  @@@@@  @@@  @@@@@@@@@@@" +
          "@@@  @@@@@  @@@  @@  @@@@@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@  @@@@@       @@@@@@@@@@@" +
          "@@@  @@@@@  @@@  @@       @@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@    @@@@@    @@         @@" +
          "@         @@    @@@@  @@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@  @  @@@  @  @@  @@@@@  @@@  @@@" +
          "@@  @@  @  @@@  @@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@  @@  @  @@  @@  @@@@@  @@@  @@" +
          "@@@  @@  @@  @@  @@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@  @@@  @@@@  @@  @@@@@  @" +
          "@@  @@@@@  @@  @@@  @  @@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@  @@@@@@@@@  @@         @@" +
          "@         @@  @@@@    @@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@        @    @@@@@  @    @@@@@@@@" +
          "@      @@@        @        @  @@@   @")
    time.sleep(0.1)
    print(Fore.BLUE + "@@  @@@@  @  @  @@@@  @  @  @@@@@@@@  @@" +
          "@@  @  @@@@  @  @@@@  @  @@  @@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@  @@@@  @  @@  @@@  @  @@  @@@@@@@  @@@" +
          "@  @  @@@@  @  @@@@@@@    @@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@        @  @@@  @@  @  @@@  @@@@@@     @" +
          "@@@        @  @@@@@@@    @@@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@  @@@@  @  @@@@  @  @  @@@@  @@@@@  @@@@  @  @" +
          "@@@  @  @@@@@@@  @  @@@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@  @@@@  @  @@@@@    @  @@@@@  @@@@  @@@@  @  @" +
          "@@@  @  @@@@  @  @@  @@@")
    time.sleep(0.1)
    print(Fore.BLUE + "@@  @@@@  @  @@@@@@   @         @@@@      @@@  @" +
          "@@@  @        @  @@@   @")
    time.sleep(0.1)
    print(Fore.CYAN + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" +
          "@@@@@@@@@@@@@@@@@@@@@@@\n\n")
    time.sleep(0.1)
    time.sleep(2)
    print("\n\nStarting to accommodate, the training looks easy, everything " +
          "seems amazing, but I cannot wait for the first launch, for " +
          "the first trip to .... the moon!")
    time.sleep(2)
    start_game()


def start_game():
    """
    The role of this function is to start the game, asking the user to begin,
    to continue the game, or not.
    If the input has been inserted incorrect the user will be asked to
    introduce the correct input.
    """
    while True:
        to_the_moon = input("\nThe Chief engineer requested you to join a " +
                            "mission to the moon! Are you ready for " +
                            "the lifetime journey?! (yes/no): ").lower()
        if to_the_moon == "no":
            print("\nThis was the one and only offer...")
            time.sleep(2)
            print("\nBut, It's your choice... Good luck!")
            time.sleep(3)
            game_over = pyfiglet.figlet_format("Game Over", font="block")
            print(Fore.RED + game_over)
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
    If user has chosen 'yes', this function will request the username.
    If no input, the user will be asked again to input his username.
    """
    print("\nGreat! You made a life decision!")
    time.sleep(2)
    print("We are proud to have you here today! Your name will be " +
          "all over the newspapers!")
    while True:
        name = input("\nWhat is your name, young astronaut? " +
                     "(type name): ")
        if name == "":
            print("This doesn't look like your name, try again.")
            continue
        else:
            print(f'What a great name! Welcome to your life trip, {name}!')
            break
    print("\nEverything is ready, prepare for launch!")
    time.sleep(1)
    print("3")
    time.sleep(0.2)
    print("2")
    time.sleep(0.2)
    print("1")
    time.sleep(0.2)
    print("Go!")
    time.sleep(0.2)
    print(f'The launch has been successfull, {name}, ' +
          'soon you will land on the moon!')
    time.sleep(3)
    print("\nPrepare to land!")
    while True:
        landing = input("\nPrepare to land, be careful to follow the " +
                        "landing procedures as you have been trained. " +
                        "\nHave you followed the landing procedures? " +
                        "(yes/no):").lower()
        if landing == "no":
            print(Fore.RED + "\nDanger! Danger! Danger!")
            time.sleep(1)
            print(Fore.RED + "\nDanger! Danger! Danger!")
            time.sleep(1)
            print("You have crashed!")
            time.sleep(2)
            game_over = pyfiglet.figlet_format("Game Over", font="block")
            print(Fore.RED + game_over)
            play_again()
            break
        elif landing == "yes":
            print("You have successfully followed the landing procedures!")
            landing_string = "\nLanding ..."
            for character in landing_string:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(2)
            print("\nYou have successfully landed on the moon! ")
            print(f'Well done, {name}, you arrived on the moon ' +
                  'be ready to take your first steps on the moon!')
            time.sleep(3)
            print('The crew has set the life support resources, ' +
                  f'{name}, you can step on the moon now! ' +
                  'Keep in mind that you have 100% oxygen in your tank, ' +
                  'this will last approximative one hour.')
            time.sleep(2)
            print("Don't forget to return to the base once you running " +
                  "low on oxygen.")
            choice_two()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


# take the gun, or not
def choice_two():
    """
    The game will request the user to choose if he will pick
    the gun which will help later. Or not.
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
            print("\nYou have picked the gun. Who " +
                  "knows when you will need it.")
            choice_of_three()
            break
        elif alien_gun == "no":
            print("\nWhat you don't own, you don't take. " +
                  "Let's hope you won't regret that later.")
            time.sleep(2)
            print("The alien it's just behind you.")
            time.sleep(0.5)
            print("HE COUGHT YOU!!!!")
            time.sleep(0.5)
            game_over = pyfiglet.figlet_format("Game Over", font="block")
            print(Fore.RED + game_over)
            play_again()
            break
        else:
            print("That's not quite right, please type 'yes' or 'no'.")
            continue
    time.sleep(2)


def choice_of_three():
    """
    The user will be put in a situation where he has to choose what
    he will do next, he will receive 3 different variants
    where he can continue the game or lose.
    He can choose just one of the below variants.
    """
    print("What is that? Is that an ... ")
    alien = "ALIEN!!!"
    for character in alien:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)
    print("\nHe saw you!!!")
    while True:
        choice_three = input("What will you do? (stay/hide/run): ").lower()
        if choice_three == "stay":
            print("\nYou don't know how to use the gun yet.")
            time.sleep(2)
            print("The alien is running towards you, he is attacking you!")
            time.sleep(3)
            game_over = pyfiglet.figlet_format("Game Over", font="block")
            print(Fore.RED + game_over)
            play_again()
            break
        elif choice_three == "run":
            print("The alien it's just behind you.")
            time.sleep(2)
            print("HE COUGHT YOU!!!!")
            time.sleep(2)
            game_over = pyfiglet.figlet_format("Game Over", font="block")
            print(Fore.RED + game_over)
            play_again()
            break
        elif choice_three == "hide":
            print("I think the alien lost you...")
            time.sleep(2)
            print("Looks like he lost you. Stay down.")
            crew_assist()
            break
        else:
            print("Wrong input. Please choose 'stay', 'hide' or 'run'")
            continue


def crew_assist():
    """
    The game continues where the user will be exposeed to new challenges
    and he will be requested to choose different options.
    """
    oxigen_tank = "The oxygen tank is down to 50%."
    for character in oxigen_tank:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    while True:
        choose_your_next_move = input("What will you do? " +
                                      "(return/continue): ").lower()
        if choose_your_next_move == "return":
            print("You are now returning to the spaceship!")
            time.sleep(2)
            print("You heard a cracking. What is happening?")
            time.sleep(1)
            print("You your oxygen is running out!")
            time.sleep(1)
            print("Something has damaged your suit. " +
                  "You start loosing your conscience.")
            time.sleep(3)
            game_over = pyfiglet.figlet_format("Game Over", font="block")
            print(Fore.RED + game_over)
            play_again()
            break
        elif choose_your_next_move == "continue":
            print("You have alerted the crew, someone will " +
                  "bring you supplies.")
            do_research()
            break
        else:
            print("Wrong input. Please choose 'return' or 'continue'.")
            continue


def do_research():
    """
    While continue to collect the probes from the moon the user will
    continue meeting challenges and will be exposed to the moons
    unknown dangers.
    """
    print("While continue researching, you noticed that you are running low " +
          "on the oxygen tanks. 25% it's what you see on the watch.")
    time.sleep(2)
    radio_str = "RADIO: Crew member: Chhhhh chhhh ... he hit me!\n"
    for character in radio_str:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)
    time.sleep(2)
    print("Your team member has been killed by an alien...")
    while True:
        choice_four = input("What do you do next? " +
                            "(return/continue): ").lower()
        if choice_four == "return":
            print("You have just 25% oxygen left, you have to move fast!")
            returning_to_the_spaceship()
            break
        elif choice_four == "continue":
            print("You are brave! Continuing researching is " +
                  "important for you!")
            time.sleep(2)
            research = "RESERCHING ..."
            for character in research:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.2)
            time.sleep(2)
            print("You have just 2% oxygen left, you start seeing unclear..")
            time.sleep(3)
            game_over = pyfiglet.figlet_format("Game Over", font="block")
            print(Fore.RED + game_over)
            play_again()
            break
        else:
            print("That's not quite right! Please choose " +
                  "'return' or 'continue'.")
            continue


def returning_to_the_spaceship():
    """
    The user will be exposed to the last challenges of the game and he will
    return home on earth.
    """
    print("You are on your way back to the spaceship, " +
          "the supplies are enough for you to return to safety.")
    time.sleep(3)
    print("What is that?")
    time.sleep(1)
    print("It's the alien! He didn't seen you this " +
          "time, now it's your chance!")
    time.sleep(0.5)
    print("Do not be scared!")
    print("Choose one of the below option.")
    print("\n1. Hide yourself wishing that he won't see you.")
    print("\n2. Kill the alien, and take his body with " +
          "you to the spaceship.\n")
    if alien_gun == "yes":
        alien_text = "(1 or 2)"
    else:
        alien_text = "Please choose the option 1 or 2."
    while True:
        try:
            your_chance = int(input('What do you do next? ' +
                                    'Kill the alien with the gun ' +
                                    'or hide until he will ' +
                                    f'leave? {alien_text}: '))
            if your_chance == 1:
                print("That's a good choice, choosing safety is fine.")
                time.sleep(2)
                print("The alien sees you!")
                time.sleep(2)
                print("He is running toward you pointing his gun at you!")
                time.sleep(3)
                game_over = pyfiglet.figlet_format("Game Over", font="block")
                print(Fore.RED + game_over)
                play_again()
                break
            elif your_chance == 2:
                print("The alien hasan\'t seen you! Now is your " +
                      "chance shut!")
                time.sleep(3)
                print("You hit him! He is dead!")
                time.sleep(1)
                print("You can now take his body to earth, " +
                      "this is a great discovery!")
                time.sleep(2)
                print("You might return to the spaceship now!")
                time.sleep(4)
                print("You have prepared the ship, you are ready to launch!")
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
                                 "you can fly it like that? " +
                                 "(repair/fly): ").lower()
        if spaceship_repair == "fly":
            print("Your instincts are strong, you can do it!")
            time.sleep(3)
            danger = "DANGER! DANGER! DANGER!\n"
            for character in danger:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(2)
            print("The ship has serios damage!\n")
            mayday = "Mayday! Mayday! Mayday\n"
            for character in mayday:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.2)
            game_over = pyfiglet.figlet_format("Game Over", font="block")
            print(Fore.RED + game_over)
            play_again()
            break
        elif spaceship_repair == "repair":
            print(Style.BRIGHT + "That's a good choice!")
            repair = "REPAIRING ..."
            for character in repair:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.2)
            time.sleep(2)
            print("The repairs are completed! You can now return home!")
            home_sweet_home()
            break
        else:
            print("Wrong input! Please choose 'repair' or 'fly'!")
            continue


def home_sweet_home():
    """
    The storyline will continue and congratulate the astronaut for the
    successfully mission.
    """
    print("Well done, you have successfully returned home!")
    time.sleep(2)
    print(Back.GREEN + "Welcome back to earth!")
    time.sleep(1)
    print("\nThe alien you have brought back from the moon has been taken " +
          "by the scientists from Area 51! You are a hero!\n\n")
    time.sleep(3)
    win = pyfiglet.figlet_format("WINNER", font="smisome1")
    print(Fore.RED + win)
    time.sleep(1)
    print(Fore.GREEN + "\nYou are ready " +
          "to be a real astronaut!")
    print(Fore.GREEN + "Winner winner, chicken dinner!")
    while True:
        next_move = input("\nWhat will you do next?" +
                          "(leave/playagain): ").lower()
        if next_move == "leave":
            print("Thank you for playing my game! Good bye!")
            break
        elif next_move == "playagain":
            print("\nThat's a good choice, more training before " +
                  "the real thing!")
            play_again()
            break
        else:
            print("\nPlease input a correct choice! (Leave/PlayAgain)")
            continue


# restart game
def play_again():
    """
    This function will be called every time when the user will die in the
    challenges if not a goodbye message will be displayed. If yes,
    a play game function is called again.
    """
    while True:
        rplay_again = input("Are you ready to try again? (yes/no): ").lower()
        if rplay_again == "yes":
            introduction()
            break
        elif rplay_again == "no":
            print("\n That's not what we expected... Thank you for playing!")
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


introduction()
