#James Welsh
#CS8
#Final project
#I don't own any of the audio in this don't sue me plz


#TO DO LIST
#update commands
#add secondary answers

#IMPORT

import json
import pygame
import time
from musicplayer import MusicPlayer
from custom import User
import random
from datetime import datetime


#start pygame

pygame.init()


#Variables

calc = "calculator"
gr = True
currenttime = "what time is it"
going = True
custom = "customize"
kill = "kill"
endmusic2 = "stop music"
end = "stop"
endmusic = False
read = "read"
book1 = "harry potter book 1"
joke = "tell me a joke"
music = "play music"
book5 = "harry potter book 7"
book2 = "the candymakers book 1"
book3 = "the candymakers book 2"
book4 = "greetings from witness protection"
music1 = "play deathbed"
music2 = "play blinding lights"
music3 = "play girls like you"
music4 = "play mood"
music5 = "play upside down"
music6 = "play eyes blue like the atlantic"
music7 = "play riptide"
finishlyric = "play finish the lyric"
gameinfo = "tell me about games"
baseball = "baseball"
commands = "show commands"
secondmusic = False
thirdmusic = False
fourthmusic = False
fifthmusic = False
fact = "tell me a fun fact"
jeopardy = "play jeopardy"
sports = "sports"
pop = "pop culture"
history = "history"
science = "science"
test = "test"
round2 = False
round3 = False
y = "y"
yes = "yes"
round1lyric1a = "give you up"
round1lyric2a = "you"
round1lyric3a = "clubhouse"
round1lyric4a = "judge me"
round1lyric5a = "be great"
round2lyric1a = "can't no more"
round2lyric2a = "on a summer evening"
round2lyric3a = "nasty"
round2lyric4a = "turned up"
round2lyric5a = "flex tape"
round3lyric1a = "eat them all the time"
round3lyric2a = "I know"
end = "stop"
global v



#Making classes

user = User(input("What is your name?\n"))
player = MusicPlayer("audio.json", .2)

#Function

def myIn(myStr):
    return input(myStr).lower().strip()

def lyricfun(lyric_File):
    with open(lyric_File, "r") as f:
            lyricbook = json.load(f)
    print("Round 1 starting now!")
    lyricnum = random.randint(0, 4)
    responce = myIn(lyricbook["first round"][lyricnum]["q"] + "\n")
    if responce in lyricbook["first round"][lyricnum]["a"]:
        print("Correct!")
        round2 = True
    else:
        print("Sorry incorrect. Better luck next time!")
        ask = myIn("Would you like to play again?")
        if ask in ["y", "yes"]:
            lyricfun(lyric_File)
        else:
            print("Thanks for playing!")
            return()    
    while round2:
        print("Congrats on making it to round 2")
        time.sleep(1)
        print("Round 2 starting now!")
        lyricnum = random.randint(0, 4)
        responce = myIn(lyricbook["second round"][lyricnum]["q"] + "\n")
        if responce in lyricbook["second round"][lyricnum]["a"]:
            print("Correct!")
            round3 = True
            round2 = False
        else:
            print("Sorry incorrect. Better luck next time!")
            ask = myIn("Would you like to play again?")
            if ask in ["y", "yes"]:
                lyricfun(lyric_File)
            else:
                print("Thanks for playing!")
                return()            
    while round3:
        print("Congrats")
        time.sleep(1)
        print("If you thought anything above was difficult, you are in for a very difficult round")
        time.sleep(2)
        print("Round 3 starting now")
        lyricnum = random.randint(0, 4)
        responce = myIn(lyricbook["third round"][lyricnum]["q"] + "\n")
        if responce in lyricbook["third round"][lyricnum]["a"]:
            print("You win, congratulations.")
            ask = myIn("Would you like to play again?")
            if ask in ["y", "yes"]:
                lyricfun(lyric_File)
            else:
                print("Thanks for playing!")
                return()
        else:
            print("Sorry incorrect. Better luck next time!")
            ask = myIn("Would you like to play again?")
            if ask in ["y", "yes"]:
                lyricfun(lyric_File)
            else:
                print("Thanks for playing!")
                return()     
        
def jeopardyfun(questionsFile):
    global player
    global user
    playingMusic = False
    if myIn("Would you like Jeopardy music while you play?\n") in ["y", "yes"]:
        player.pause()
        player.loadTrack(1, "internal")
        playingMusic = True
        player.play()
    lives = 3
    points = 0
    questions = None
    with open(questionsFile, "r") as f:
        questions = json.load(f)
    if questions == None:
        print("Error")
    if lives == 0:
        ask = myIn("Sorry, you ran out of lives. Would you like to play again?")
        if ask == ["y", "yes"]:
            points = 0
            lives = 3
        else:
            print("Thanks for playing!")
            if playingMusic == True:
                player.pause()
            return()
    while lives > 0:
        selectedCategory = myIn(f"What category would you like?\nThese are you choices: sports, history, science, and pop culture. You can respond 'stop' to exit the game\nYou have {points} currently with {lives} lives left\n")
        if selectedCategory == "stop":
            print("Bye! Thanks for playing!")
            if playingMusic == True:
                player.pause()
            return()
        if selectedCategory in "sports":
            selectedPoints = myIn("What point question would you like?\n")
            if selectedPoints in "100":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Sports"]["100"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Sports"]["100"][questionNumber]["a"]:
                    print("Correct! 100 points")
                    points += 100
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "200":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Sports"]["200"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Sports"]["200"][questionNumber]["a"]:
                    print("Correct! 200 points")
                    points += 200
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "300":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Sports"]["300"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Sports"]["300"][questionNumber]["a"]:
                    print("Correct! 300 points")
                    points += 300
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "400":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Sports"]["400"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Sports"]["400"][questionNumber]["a"]:
                    print("Correct! 400 points")
                    points += 400
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "500":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Sports"]["500"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Sports"]["500"][questionNumber]["a"]:
                    print("Correct! 500 points")
                    points += 500
                else:
                    lives-=1
                    print("Sorry, incorrect")
        if selectedCategory in "history":
            selectedPoints = myIn("What point question would you like?\n")
            if selectedPoints in "100":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["History"]["100"][questionNumber]["q"] + "\n")
                if questionResponce in questions["History"]["100"][questionNumber]["a"]:
                    print("Correct! 100 points")
                    points += 100
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "200":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["History"]["200"][questionNumber]["q"] + "\n")
                if questionResponce in questions["History"]["200"][questionNumber]["a"]:
                    print("Correct! 200 points")
                    points += 200
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "300":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["History"]["300"][questionNumber]["q"] + "\n")
                if questionResponce in questions["History"]["300"][questionNumber]["a"]:
                    print("Correct! 300 points")
                    points += 300
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "400":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["History"]["400"][questionNumber]["q"] + "\n")
                if questionResponce in questions["History"]["400"][questionNumber]["a"]:
                    print("Correct! 400 points")
                    points += 400
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "500":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["History"]["500"][questionNumber]["q"] + "\n")
                if questionResponce in questions["History"]["500"][questionNumber]["a"]:
                    print("Correct! 500 points")
                    points += 500
                else:
                    lives-=1
                    print("Sorry, incorrect")
        if selectedCategory in "science":
            selectedPoints = myIn("What point question would you like?\n")
            if selectedPoints in "100":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Science"]["100"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Science"]["100"][questionNumber]["a"]:
                    print("Correct! 100 points")
                    points += 100
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "200":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Science"]["200"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Science"]["200"][questionNumber]["a"]:
                    print("Correct! 200 points")
                    points += 200
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "300":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Science"]["300"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Science"]["300"][questionNumber]["a"]:
                    print("Correct! 300 points")
                    points += 300
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "400":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Science"]["400"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Science"]["400"][questionNumber]["a"]:
                    print("Correct! 400 points")
                    points += 400
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "500":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Science"]["500"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Science"]["500"][questionNumber]["a"]:
                    print("Correct! 500 points")
                    points += 500
                else:
                    lives-=1
                    print("Sorry, incorrect")
        if selectedCategory in "pop cuture":
            selectedPoints = myIn("What point question would you like?\n")
            if selectedPoints in "100":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Pop culture"]["100"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Pop culture"]["100"][questionNumber]["a"]:
                    print("Correct! 100 points")
                    points += 100
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "200":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Pop culture"]["200"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Pop culture"]["200"][questionNumber]["a"]:
                    print("Correct! 200 points")
                    points += 200
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "300":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Pop culture"]["300"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Pop culture"]["300"][questionNumber]["a"]:
                    print("Correct! 300 points")
                    points += 300
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "400":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Pop culture"]["400"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Pop culture"]["400"][questionNumber]["a"]:
                    print("Correct! 400 points")
                    points += 400
                else:
                    lives-=1
                    print("Sorry, incorrect")
            if selectedPoints in "500":
                questionNumber = random.randint(1, 5)
                questionResponce = myIn(questions["Sports"]["500"][questionNumber]["q"] + "\n")
                if questionResponce in questions["Sports"]["500"][questionNumber]["a"]:
                    print("Correct! 500 points")
                    points += 500
                else:
                    lives-=1
                    print("Sorry, incorrect")          
        
#    

def addition(num1:int, num2:int):
  sum1 = num1 + num2
  return [num1, num2, sum1]

def multiplication(num1: int, num2:int):
  product = num1*num2
  return product

# Made by Sarvesh 
def subtraction(num1:int, num2:int):
  sub = num1 - num2
  return sub


# Made by Jacob
def division(num1:int, num2:int):
  quotient = (num1 / num2)
  return quotient

# Made by Eloise Modulo
def mod(num1:int, num2:int):
  mod1 = num1 % num2
  return mod1

# Made by Meranda
def exponent(num1 : int, num2 : int):
  index = num1 ** num2
  return index

# Made by Victoria
def fdivision(num1: int , num2: int):
  sum= num1 // num2
  return sum

#loop
        

while gr:
    request = myIn(f"{user.name}, what can I do for you? \n")
    if request in ["calculate", "calculator"]:
        input1 = int(input("first number (the number that will be subtracted or divided from): "))
        input2 = int(input("second number (the number that is subrated or divided by): "))
        input3 = int(input("Choices:\n1. Add\n2.Subtract\n3. Multiply\n4. Divide\n5. Mod\n6. Power\n7. Floor Divide\nYour Choice: "))
        if input3 in [1, 2, 3, 4, 5, 6, 7]:
            # choose the correct option
            if input3 == 1:
                print(addition(input1, input2))
            elif input3 == 2:
                print(subtraction(input1, input2))
            elif input3 == 3:
                print(multiplication(input1, input2))
            elif input3 == 4:
                print(division(input1, input2))
            elif input3 == 5:
                print(mod(input1, input2))
            elif input3 == 6:
                print(exponent(input1, input2))
            else:
                print(fdivision(input1, input2))
        else:
            print("That was not a valid choice")

        input4 = myIn("Would you like to go again? \n")
        if input4.lower() not in ["y", "yes", "true", "t"]:
            doLoop = False
    elif request in ["what time is it?", "what is the time", "what time is it", "what's the time", "what time is it?", "what's the time?"]:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("The Current time is ", current_time)
    elif request in ["play music", "music"]:
        player.displayTracks()
        player.pause()
        musicrequest = input("What song would you like to play?\nPlease only use numbers not words.\n")
        musicrq = int(musicrequest)
        player.loadTrack(musicrq)
        player.play()
    elif request in ["help", "commands", "what commands do you have", "what commands do you have?", "show commands"]:
        print("I have commands like reading (read)")
        time.sleep(1)
        print("Games (to learn about games type 'tell me about games' or to play one say either 'play jeopardy' or 'play finish the lyric')")
        time.sleep(2)
        print("I can tell you jokes (tell me a joke)")
        time.sleep(1)
        print("I can play music (play music)")
        time.sleep(1)
        print("And I can tell you fun fact (tell me a fun fact)")   
    elif request in ["baseball"]:
        print("LETS GO TWINS, ITS ALL ABOUT THE TWINS BABY!!!!")
    elif request in ["play finish the lyric", "play ftl"]:
        print("Welcome to finish the lyric")
        time.sleep(1)
        print("I am you host")
        time.sleep(1)
        print("I will give you part of a lyric and you will finish it. Good luck!")
        lyric_File = "lyric_game.json"
        lyricfun(lyric_File)
    elif request in ["fun fact", "tell me a fun fact"]:
        factnum = random.randint(1, 5)
        if factnum == 1:
            print("A shrimps heart is in it's head!")
        if factnum == 2:
            print("Most people cannot lick their elbow!")
        if factnum == 3:
            print("It is impossible for pigs to look up at the sky!")
        if factnum == 4:
            print("A crocodile cannot stick it's tongue out!")
        if factnum == 5:
            print("Some lipstick has fish scales in it!")
    elif request in ["read"]:
        player.displayTracks("books")
        booksrequest = input("Which book would you like read?\nPlease only use numbers not words.\n")
        bookrq = int(booksrequest)
        player.loadTrack(bookrq, "books")
        player.play()
    elif request in ["play jeopardy", "jeopardy", "jepordy", "play jepordy"]:
        questionsFile = "Jeopardy.json"
        print(f"Welcome to jeopardy, I am your host. You know the rules. \nBest of luck {user.name}")
        jeopardyfun(questionsFile)
    elif request.lower()== joke:
        jokenum = random.randint(1,6)
        if jokenum == 1:
            print("What do you call a disguised pasta?")
            time.sleep(1)
            print("An impasta!")   
        if jokenum == 2:
            print("What do birds give out on halloween?")
            time.sleep(1)
            print("Tweets!")
        if jokenum == 3:
            print("Why do people bring 2 pairs of socks when they go golfing?")
            time.sleep(1)
            print("Incase they get a hole-in-one!")   
        if jokenum == 4:
            print("What did the janitor say when he jumped out of the closet?")
            time.sleep(1)
            print("Supplies!") 
        if jokenum == 5:
            print("How does the the moon cut their hair?")
            time.sleep(1)
            print("They Eclips it!")    
        if jokenum == 6:
            print("Why wouldn't the oyster give up her pearl?")
            time.sleep(1)
            print("She is shellfish!")        
    elif request in ["tell me about games", "games"]:
        ask = myIn("I have two games: Jeopardy and finish the lyric. Which one would you like to learn about>?\n")
        if ask in ["jeopardy", "jepardy"]:
            print("A spin on the classic game")
            time.sleep(1)
            print("You have 3 lives to get as many points as possible with 4 categories.")
            time.sleep(1)
            playagain = myIn("Do you want to play?\n") 
            if playagain in ["y", "yes"]:
                questionsFile = "Jeopardy.json"
                jeopardyfun(questionsFile)
            else:
                print("Ok. Play soon!")
        else:
            print("In this game, you are given part of a lyric")
            time.sleep(1)
            ask = myIn("Your job is to finish it, would you like to play?")     
            if ask in ["yes", "y"]:
                lyric_File = "lyric_game.json"
                lyricfun(lyric_File)         
    elif request in ["stop music", "stop book", "pause music", "pause book", "pause"]:
        player.pause()
        print("Paused")     
    elif request in ["stop", "kill"]:
        print("Bye. See you next time!")
        gr = False
    elif request in ["resume", "resume music", "resume book"]:
        player.resume()
    elif request in ["increase volume", "higher volume"]:
        double_Check = myIn("Are you sure? You will have to reselect the song and start from the begining?\n")
        if double_Check in ["yes", "y"]:
            player.pause()
            player.changeVolume(.8)
            player.displayTracks()
            musicrq = int(myIn("What song were you playing?\n"))
            player.loadTrack(musicrq)
            player.play()
    elif request in ["decrease volume", "lower volume"]:
        double_Check = myIn("Are you sure? You will have to reselect the song and start from the begining?\n")
        if double_Check in ["yes", "y"]:
            player.pause()
            player.changeVolume(.05)
            player.displayTracks()
            musicrq = int(myIn("What song were you playing?\n"))
            player.loadTrack(musicrq)
            player.play()
    else:
        print("Sorry, I don't know that one. \nI have different activities like games, to hear more about games ask me 'tell me about games' \nor to see all commands type 'show commands'")
       