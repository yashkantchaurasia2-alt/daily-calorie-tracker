#task1
print("Welcome to calorie tracker..")
print("Compare your daily meals..")
#task2
Meal=[]
Calories=[]
num_Meal=int(input("How many meals did u eat today? "))
#task3
for i in range(num_Meal):
    Meal_name=input(f"Enter {i+1}th meal name: ")
    cal=float(input(f"Enter calories for {i+1}th meal: "))
    Meal.append(Meal_name)
    Calories.append(cal)

total_calories=sum(Calories)
avg_calories=total_calories/num_Meal
print("Your average calories are: ")
print(avg_calories)
daily_limit=float(input("Enter your daily calorie limit: "))
#task 4
if(avg_calories>daily_limit):
    print("Excess of calories are  taken..")
else:
    print("you are good in calories..")
print()
#task 5   
#print the table header 
print(f"{'Meal name':<15}{'Calories'}")
print("-" * 25)                         #prints a separator line
                                        #loop through the lists and print each meal and its calories
for i in range(len(Meal)):
    print(f"{Meal[i]:<15}{Calories[i]}")
print()
print("Your total caories are: ")
print(total_calories)

