if __name__ == '__main__':
    #UPDATED: 11-15-21 by Nick
    #Notes from Nick: I added the dictionary containing all the trivia questions and answers.
    #Here is how you use the dictionary, lets say the user selects "Science 200", to display the question
    #print(d["Science 200"][0]) : This will print out "This continent is where lions are native to"
    #
    #When the user answers, use an if statement to detect if the proper answer was typed in
    #
    #*******************
    #x = str(input())
    #if x == d["Science 200"][1] or d["Science 200"][2]
    #   print("Correct!")
    #   score += 200
    #else:
    #   print("Incorrect!")
    #   print("Please select a category by saying the category and price (Ex. Movies 200, Sports 1000, etc)")
    #   n += 1
    #*******************
    #
    #To summarize,  d["Category 200-1000"][0] = Question
    #               d["Category 200-1000"[1, 2, 3, etc.] = possible answers
    #There are multiple answers because some people might not capitalize certain words, and since this is case
    #sensitive there needed to be a way where every possible input would work. If you all decide this is not neccesary then
    #we can ignore it, I just added it to make sure.
    #If you have any questions feel free to ask me anything in the GroupMe!
    #
    #
    #



    d = {
        "Science 200": ["This continent is where lions are native to", "What is Africa", "what is africa"],
        "Science 400": ["This pigment gives leaves their green color", "What is Chlorophyll", "what is chlorophyll"],
        "Science 600": ["Devil's Tower is located in this state", "What is Wyoming", "what is wyoming"],
        "Science 800": ["This is the name of our species", "What is Homo Sapiens", "what is homo sapiens"],
        "Science 1000": ["This person is the chemist who invented dynamite and established the Nobel Prize ", "What is Alfred Nobel", "what is alfred nobel"],
        "Music 200": ["This was the best selling album of all time.", "What is Thriller", "what is thriller"],
        "Music 400": ["This instrument has the highest pitch in an string orchestra", "What is the Violin", "what is the violin", "what is Violin", "What is violin"],
        "Music 600": ["This person is considered to be the greatest guitar player of all time, he is known for burning his guitar at a festival", "What is Jimi Hendrix", "what is jimi hendrix"],
        "Music 800": ["This state is where the infamous Woodstock Festival was held in 1969", "What is New York", "what is new york"],
        "Music 1000": ["This musician is known by many aliases, from Aphex Twin, AFX, Polygon Window, Caustic Window, and many others", "What is Richard D. James", "What is Richard D James", "what is richard d. james", "what is richard d james"],
        "Sports 200": ["This sport is known as America's past time", "Baseball", "baseball"],
        "Sports 400": ["Michael Jordan won 6 NBA Championships with this team", "Chicago Bulls", "chicago bulls"],
        "Sports 600": ["This QB won the Heisman trophy in 2016 and went on to play for the Ravens in the NFL", "What is Lamar Jackson", "what is lamar jackson"],
        "Sports 800": ["This person is the only athlete to be named an All-Star in both Baseball and Football", "What is Bo Jackson", "what is bo jackson"],
        "Sports 1000": ["This country is where the sport of golf originates from", "Scotland", "scotland"],
        "Television 200": ["This show ran from 2005 to 2013 and starred Steve Carrel, John Krasinski, Rainn Wilson, and others", "What is The Office", "what is the office"],
        "Television 400": ["This show features a talking sponge that works at a fast food restaurant", "What is Spongebob", "what is spongebob", "What is Spongebob Squarepants", "what is spongebob squarepants"],
        "Television 600": ["This person is the voice actor of BoJack Horseman, and other characters in the show", "Will Arnett", "will arnett"],
        "Television 800": ["This popular television shows series finale cut to black mid-scene", "What is The Sopranos", "what is the sopranos"],
        "Television 1000": ["This person played Carl Grimes on AMC's The Walking Dead", "What is Chandler Riggs", "what is chandler riggs"],
        "Movies 200": ["This movie released in 2019 and use to be the highest grossing film of all time", "What is Avengers: End Game", "what is avengers: end game", "What is Avengers End Game", "what is avengers end game"],
        "Movies 400": ["Released in 2017, this movie is the highest grossing film in the U.S. that's set during World War I", "What is Wonder Woman", "what is wonder woman"],
        "Movies 600": ["Who was the lead actor in 2013's The Wolf of Wallstreet", "Leonardo DiCaprio", "Leonardo Dicaprio", "leonardo dicaprio"],
        "Movies 800": ["This movie made by Pixar stars Tom Hanks as a talking sheriff toy", "What is Toy Story", "what is toy story"],
        "Movies 1000": ["This movie, which was directed by Stanley Kubrik, explores the horrors of the Vietnam War", "What is Full Metal Jaket", "what is full metal jacket"],
        "Geography 200": ["This country is where Stonehenge is located", "What is Britian", "what is britian", "What is the UK", "what is the uk", "What is the United Kingdom", "what is the united kingdom"],
        "Geography 400": ["This region in the Middle East where modern day Iraq and Syria is located is known as", "What is the Fertile Crescent", "what is the fertile crescent"],
        "Geography 600": ["This is the tallest mountain on earth from above sea level", "What is Mt. Everest", "what is mt. everest", "What is Mount Everest", "what is mount everest", "What is Mt Everest", "what is mt everest"],
        "Geography 800": ["This is the deepest part of the ocean", "What is the Mariana Trench", "what is the mariana trench"],
        "Geography 1000": ["This Inca Citadel in Peru is named", "What is Machu Picchu", "what is machu picchu"],
    }
    categories = ['Science', 'Music', 'Sports', 'Television', 'Movies', 'History' ]
    r1 = ['200', '  200', '   200', '     200', '     200', '    200']
    r2 = ['400', '  400', '   400', '     400', '     400', '    400']
    r3 = ['600', '  600', '   600', '     600', '     600', '    600']
    r4 = ['800', '  800', '   800', '     800', '     800', '    800']
    r5 = ['1000', '1000', '  1000', '    1000', '    1000', '   1000']
    print(categories)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    score = 0
    print("Please select a category by saying the category and price (Ex. Movies 200, Sports 1000, etc")
    x = str(input())
    n = 0
    while n <= 30:
        print("Please select a category by saying the category and price (Ex. Movies 200, Sports 1000, etc)")
        x = input()
        if x == "movies 200" or "Movies 200":
            print(r1[4])
            z = input()
            if z == "Leonardo Dicaprio":
                print("Correct!")
                score += 200
                n += 1
            else:
                print("That answer is incorrect.")
                print("Please select a category by saying the category and price (Ex. Movies 200, Sports 1000, etc)")
                n += 1
        else:
            pass
            n += 1
        print("Your score is:", score)

    def final_jeopardy(score):
        print("Final Jeopardy Question!")
        wager = int(input("What is your wager?"))
        if wager > score:
            print("You cannot wager more than you have!")
            pass
        else:
            print("Released in 2017, this movie is the highest grossing film in the U.S. that's set during World War I")
            answer = "Wonder Woman"
            guess = input("What is your Guess?")
            if answer == guess:
                score = wager + score
                print("You are correct! Your final score is", score)
            else:
                score = score - wager
                print("Sorry that's incorrect. Your final score is", score)
        return(score)

    final_jeopardy(score)
