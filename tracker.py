# Course            : Programming for Problem Solving using Python
# Assignment Title  : Building a Calorie Tracking Console App
# Name              : Kaushal
# Roll no.          : 2501730085
# Section           : B
# School            : School of engineering technology(SOET)
# Submission date   : 9 nov 2025

#______________________________________________________________________________________________________


# --- Welcome message and introduction ---
print("-------------------------------------------------------------------------------")
print("                Welcome to the Daily Calorie Tracker CLI")
print("-------------------------------------------------------------------------------")
print()


print("This tool helps you log your meals, track your total calories, compare them against your daily limit and save your data.\nIn this way we can take care of our nurition.")
print()
print("Lets start!")


# --- Input & Data Collection ---
meals = []
calories = []

num_meals = int(input("How many meals do you want to enter? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter meal {i+1} name: ")
    cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(cal)

# --- Calorie Calculations ---
total_calories = sum(calories)
average_calories = total_calories / len(calories)
limit = float(input("\nEnter your daily calorie limit: "))

# --- Exceed Limit Warning System ---
if total_calories > limit:
    status = " Warning: You have exceeded your daily calorie limit!"
else:
    status = " Good job! You are within your daily calorie limit."

# ---Formatted Output ---
print("\nYour Daily Calorie Summary:")
print("-"*28)
print("Meal Name\tCalories")
print("--------------------------------------------")
for m, c in zip(meals, calories):
    print(f"{m:<15}\t{c:<15}")
print("--------------------------------------------")
print(f"{'Total:':<15}\t{total_calories:<15.2f}")
print(f"{'Average:':<15}\t{average_calories:.2f}")
print(status)

# --- Task 6: Save Session Log to File ---
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

from datetime import datetime
if save == "yes":
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"
    
    with open(filename, "w") as file:
        file.write("Daily Calorie Tracker Log\n")
        file.write(f"Date & Time: {now}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("--------------------------------------------\n")
        for m, c in zip(meals, calories):
            file.write(f"{m:<15}\t{c:<15}\n")
        file.write("--------------------------------------------\n")
        file.write(f"{'Total:':<15}\t{total_calories:<15.2f}\n")
        file.write(f"{'Average:':<15}\t{average_calories:.2f}\n")
        file.write(status + "\n")
    
    print(f"\nReport saved successfully as '{filename}'!")
else:
    print("\nReport not saved.")















