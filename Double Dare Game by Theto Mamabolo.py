import sys
import time

print('Welcome to Double Dare!'.upper())
print()

player1_name = input('Player1, enter your name:\n ')
print()
player2_name = input('Player2, enter your name:\n ')
print()

mode = {1: 'Easy', 2 : 'Medium', 3 : 'Hard'}

print('1: Easy, 2: Medium, 3: Hard')
print()

easy = {
    "What color is the sky on a clear day?": "BLUE",
    "How many legs does a spider have?": "8",
    "What do you use to brush your teeth?": "TOOTHBRUSH",
    "What animal barks?": "DOG",
    "How many days are in a week?": "7",
    "What do bees make?": "HONEY",
    "What is the opposite of hot?": "COLD",
    "How many wheels does a bicycle have?": "2",
    "What shape has 3 sides?": "TRIANGLE",
    "What is the first letter of the alphabet?": "A",
    "What do you call a baby cat?": "KITTEN",
    "How many hours are in a day?": "24",
    "What fruit is yellow and curved?": "BANANA",
    "What sound does a cow make?": "MOO",
    "Which planet do we live on?": "EARTH",
    "What color are apples usually?": "RED",
    "What do you wear on your feet?": "SHOES",
    "What do chickens lay?": "EGGS",
    "What is 2 + 2?": "4",
    "Which animal is known as the king of the jungle?": "LION"
}

medium = {
    "What gas do plants breathe in that humans breathe out?": "CARBON DIOXIDE",
    "Who painted the Mona Lisa?": "LEONARDO DA VINCI",
    "What is the capital city of France?": "PARIS",
    "How many continents are there on Earth?": "7",
    "What is the largest mammal in the world?": "BLUE WHALE",
    "Which ocean is the largest?": "PACIFIC",
    "In what country were the pyramids built?": "EGYPT",
    "Who discovered gravity when an apple fell on his head?": "ISAAC NEWTON",
    "What is H2O commonly known as?": "WATER",
    "How many sides does a hexagon have?": "6",
    "Which organ pumps blood through your body?": "HEART",
    "What is the currency of Japan?": "YEN",
    "What do you call animals that eat only plants?": "HERBIVORES",
    "What planet is known as the Red Planet?": "MARS",
    "What is the boiling point of water in Celsius?": "100",
    "Which part of the plant conducts photosynthesis?": "LEAVES",
    "What is the capital of South Africa?": "PRETORIA",
    "Who wrote 'Romeo and Juliet'?": "WILLIAM SHAKESPEARE",
    "What is the largest planet in our solar system?": "JUPITER",
    "How many bones are in the adult human body?": "206"
}

hard = {
    "What is the smallest prime number greater than 100?": "101",
    "What element has the atomic number 79?": "GOLD",
    "Who developed the theory of general relativity?": "ALBERT EINSTEIN",
    "Which Shakespeare play features the characters Rosencrantz and Guildenstern?": "HAMLET",
    "What is the square root of 1444?": "38",
    "Which war began in 1914?": "WORLD WAR I",
    "What’s the capital of Iceland?": "REYKJAVIK",
    "What language has the most native speakers in the world?": "MANDARIN",
    "Which philosopher wrote 'The Republic'?": "PLATO",
    "What is the hardest natural substance on Earth?": "DIAMOND",
    "What is the longest river in the world?": "NILE",
    "What instrument measures earthquakes?": "SEISMOGRAPH",
    "What is the term for animals active during twilight?": "CREPUSCULAR",
    "Who painted 'The Starry Night'?": "VINCENT VAN GOGH",
    "What is the currency of Switzerland?": "SWISS FRANC",
    "Which element is represented by the symbol 'Fe'?": "IRON",
    "What is the powerhouse of the cell?": "MITOCHONDRIA",
    "Who is the Greek god of the underworld?": "HADES",
    "What number is represented by the Roman numeral 'D'?": "500",
    "What mathematician is known for his last theorem?": "FERMAT"
}



while True:
    try:
        mode_selection = int(input('Enter the choice of difficulty by entering the number that corresponds with the difficulty:\n '))
        print()
        
        if mode_selection in mode:
            if mode_selection == 1:
                m = easy
            
            elif mode_selection == 2:
                m = medium

            elif mode_selection == 3:
                m = hard
            break

        else:
            print('The mode you selected does not exist. Try again.')
            print()
    
    except ValueError:
        print('Your selection should be an integer, ("1-3").')
        print()




def game():

    print('\nGame rules: ' \
    'Player 1 first enters his answer. If player 1\'s answer is incorrect, the same question is directed to player 2, vice versa. If player 1 or 2 gets the answer correct, the player gets to play again until they get it wrong or win.')
    print()

    player1_health = 100
    player1_points = 0
    player2_health = 100
    player2_points = 0
    
    for question in m.keys():
        print(question)
        ply1_input = input(f" {player1_name}'s answer: ").upper()
        print()

        if ply1_input in m[question].upper():
            player1_points += 5
            print('You obtain +5 points!')
            print()
            if player1_points == 100:
                break
            


        else:
            player1_health -= 10
            print('Incorrect answer!')
            print(f' Health left, {player1_name} : {player1_health}')
            print()
            if player1_health == 0:
                print(f'Health depleted. {player1_name} loses!')
            
            ply2_input = input(f'{player2_name} answer: ').upper()

            if  ply2_input == m[question].upper():
                player2_points += 5
                print('You obtain +5 points')
                if player2_points == 100:
                    break
            
            else:
                player2_health -= 10
                print('Incorrect answer!')
                print(f' Health left, {player2_name} : {player2_health}')
                print()
                if player2_health == 0:
                    print(f'Health depleted. {player2_name} loses!')
        
    print(f"{player1_name}'s final points: {player1_points}")
    print(f"{player2_name}'s final points: {player2_points}")

    if player1_points > player2_points:
        print('Checking results...')
        time.sleep(3)
        print(f'{player1_name} WINS!')

    else:
        print('Checking results...')
        time.sleep(3)
        print(f'{player1_name} WINS!')
    

    while True:
        try:
            _exit = input('Enter "YES" if you want to exit game or "NO" if you\'d like to stay:\n' ).upper()
            if _exit == 'Yes'.upper():
                sys.exit()

            elif _exit == 'NO'.upper():
                try:
                    _restart_game = input('You chose to stay. Would you like to restart the game? "YES" or "No":\n ').upper()

                    if _restart_game == 'YES'.upper():
                       return game()

                    elif _restart_game == 'NO'.upper():
                        pass

                    else:
                        print('Please enter "YES" or "NO".')

                except ValueError:
                    print('Your response should be a string, ("YES" or "NO").')
            
            else:
                print('Please enter "YES" or "NO".')

        except ValueError:
            print('Your response should be a string, ("YES" or "NO").')
    
        return
game()               





   



    


