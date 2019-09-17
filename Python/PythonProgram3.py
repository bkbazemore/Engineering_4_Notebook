def sentencespliter():

    list = input("Enter your sentence: ")

    words = list.split(" ")
    
    for word in words:
        for letter in word:
            print(letter)
        print("-")
    letters= len(words)

    #[print(i) for i in list]

    #print("-"), 

sentencespliter()
