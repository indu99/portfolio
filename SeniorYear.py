start = '''
It's the beginning of senior year! The choices that you make in your last year of high school will significantly impact your future whether you know it or not.
Your friend invited you to a party tonight. Will you go or will you stay home and work on your college application?'''

print(start)

print("Type 'party' to go to the party or 'study' to study for you upcoming tests.")
user_input = input()
if user_input == "party":
    print("You go to the party and you are having a good time, however, it is getting late and you have 9 missed calls from your mom. Do you go home or stay? ")
    print("Type 'home' to go home and study or type 'stay' to stay at the party.")
    user_input2 = input()
    if user_input2 == "home":
        print("Good Job! You know how to have fun responsibly.")
        print("Your good habits stick, and you end up going to a highly reputable college and getting a great education!")
    elif user_input2 == "stay":
        print("You decide to stay for another hour.")
        print("You are about to leave but your all time crush walks up to you and asks you to stay and hang out. Do you stay or leave?")
        print("Type 'stay' to hang out with your crush or 'leave' to go home and get some rest before your test tommorow.")
        user_input3 = input ()
        if user_input3 == "stay":
            print ("You stay and hang out with your crush...")
            print ("But ten minutes later, your mom shows up at the door along with the police.")
            print ("Everyone blames you for the party getting busted and you become a social outcast with no friends. :(")
        elif user_input3 == "leave":
            print ("You decide that you are an independent woman or man and your crush isn't worth failing your test tommorow.")
            print ("Your ability to refuse temptation helps you get into a good college where your receive a great education!")
elif user_input == "study":
    print("You choose to study. Good for you! Will you take notes or will you study for 30 minutes and watch Netflix for 2 hours? ...")
    print("Type 'notes' to take notes or 'netflix' to study for a little and watch netflix.")
    user_input1 = input()
    if user_input1 == "notes":
        print("You study well and you ace your test!")
        print("Your good habits stick, and you end up going to a highly repuatble college and getting a great education!")
    elif user_input1 == "netflix":
        print("You watch netflix for the majority of the night and get an okay grade on your test.")
        print("You continue your lazy habits for the rest of the year.")
        print("You end up going to a decent college and still receive a great education! However, you must fix your lazy habits!")


print ("<<Remember, life is about having a balance; know when to have fun but also know when to work hard>>")
