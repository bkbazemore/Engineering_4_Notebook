import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)


word = input("player 1, go for it, pick a word: ")
print("\n"*50) #clears the screen
letters = list(word)
guess_arr = []
wrong_letter = 1
#build
hangman = ["---|\n",
           "   o\n",
           "   |\n",
           "  /","|","\\", "\n",
           "   | \n",
           "  /"," ","\\","\n"]
for i in letters:
    guess_arr.append("_")

#gametimeeEee
while True:
    current_hangman = ""
    for i in range(0,wrong_letter):
        current_hangman += hangman[i]
    print(current_hangman)
    current_letters = ""
    for i in guess_arr:
        current_letters += i + ""
    print(current_letters)

    guess = input("player 2, give us your best guess ;): ")
    if guess not in letters:
        print("that aint it...")
        GPIO.output(24,GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(24,GPIO.LOW)
        wrong_letter += 1
        if hangman[wrong_letter] == "\n" or hangman[wrong_letter] == " ":
            wrong_letter += 1
    else:
        print("You got it dude!!")
        for i in letters:
            if guess in letters:
                letter_placement = letters.index(guess)
                guess_arr[letter_placement] = guess
                letters[letter_placement] = " "
                GPIO.output(23,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(23,GPIO.LOW)
            else:
                break
    if guess_arr == list(word):
        print("The word was " + word)
        print("You did it my dude")
        GPIO.output(23,GPIO.HIGH)
        break
    if wrong_letter == len(hangman):
        current_hangman = ""
        for i in range(0,wrong_letter):
            current_hangman += hangman [i]
        print(current_hangman)
        print("the word was " + word)
        print("you really didn't...")
        GPIO.output(24,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(24,GPIO.LOW)
        break
        

    

