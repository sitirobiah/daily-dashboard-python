first_name = "mohamed"
last_name = "ali"
name = first_name + " " + last_name



#With while loop
def get_mood():
    while True:
        mood = input("How are you feeling today? ")
        if mood == "happy":
            print("You have high energy today!")   
            return mood
        elif mood == "sad":
            print("You have average energy today!")
            return mood
        else:
            print("Enter happy/sad only.")


def get_energy():
        energy = int(input("How is your energy level (0-100): "))
        if energy > 80:
            print("Great Energy !")   
        elif energy > 50:
            print("Good Energy !")
        elif energy > 20:
            print("Low Energy!")
        else:
            print("Time to rest")
        return energy

# combined if elif else statement
def show_wellbeing(mood, energy):
    if mood == "happy" or energy > 70:
        print("Your Wellbeing looks great today!")
    elif mood == "sad" and energy > 50:
        print("Wellbeing is about mood AND energy!")
    elif mood == "sad" and energy > 20:
        print("Take some time to rest and recharge.")
    else:
        print("Input FALSE")
    



def get_goals():
    goal_list = []
    print("Enter your goals for today :")
    while True:
        goal = input("Enter a goal: ")
        if goal == "done":
            break
        goal_list.append(goal) #menambahkan item ke dalam list goals
    print("Total goals:", len(goal)) #menghitung jumlah item dalam list goals
    return goal_list


def get_completions(goal_list):
    completed = 0
    print("Mark your goals as completed:")

    for goal in goal_list:
        status = input(goal + "_done?  (y/n): ")
        if status == "y":
            completed += 1
    return completed

def show_result(goal, completed):
    print("Total goals", len(goal))
    print("Completed goals:", completed)
    print("Pending goals:", len(goal) - completed)

def show_final_message(goal, completed):
    if completed == len(goal):
        print("You nailed all your goals today")
    else:
        print("Keep pushing to complete your goals!")




print("==============================")
print("DAILY DASHBOARD")
print("==============================")
print()
print("Welcome back,", name)
print()
print("WELLBEING")
mood = get_mood()
energy = get_energy()

print()
show_wellbeing(mood, energy) 
print()

print("GOALS")
goal = get_goals()
completed = get_completions(goal)

print("RESULTS")
show_result(goal, completed)
show_final_message(goal, completed)