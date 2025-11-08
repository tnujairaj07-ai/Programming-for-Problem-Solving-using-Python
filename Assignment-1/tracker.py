# tracker.py
# Name: [Your Name Here]
# Date: 27-10-2025
# Project Title: Daily Calorie Tracking Console App

import datetime

print("Welcome to Daily Calorie Tracker CLI!")
print("This tool lets you log your meals, track total calories, compare against your daily target, and save session logs.\n")

# Task 2: Input Data Collection
meal_names = []
meal_calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    name = input(f"Enter name for meal {i+1} (e.g., Breakfast): ")
    calorie = float(input(f"Enter calorie amount for {name}: "))
    meal_names.append(name)
    meal_calories.append(calorie)

# Task 3: Calorie Calculations
total_calories = sum(meal_calories)
average_calories = total_calories / num_meals if num_meals else 0

limit = float(input("Enter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > limit:
    status_msg = f"Warning: You exceeded your daily calorie limit by {total_calories-limit:.2f} calories!"
    status = "Exceeded"
else:
    status_msg = "Great! You are within your daily calorie limit."
    status = "Within limit"

# Task 5: Neatly Formatted Output
print("\nCalorie Intake Summary")
print("Meal Name\tCalories")
print("-" * 24)
for name, cal in zip(meal_names, meal_calories):
    print(f"{name}\t\t{cal}")
print("-" * 24)
print(f"Total\t\t{total_calories:.2f}")
print(f"Average\t\t{average_calories:.2f}")
print(status_msg)

# Task 6: Bonus - Save Session Log to File
save = input("\nDo you want to save the session summary to a file? (yes/no): ").strip().lower()
if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorielog.txt"
    with open(filename, "w") as f:
        f.write(f"Calorie Tracker Session: {timestamp}\n")
        f.write("Meal Name\tCalories\n")
        for name, cal in zip(meal_names, meal_calories):
            f.write(f"{name}\t\t{cal}\n")
        f.write(f"Total\t\t{total_calories:.2f}\n")
        f.write(f"Average\t\t{average_calories:.2f}\n")
        f.write(f"Daily Limit: {limit}\n")
        f.write(f"Limit Status: {status}\n")
        f.write(f"{status_msg}\n")
    print(f"Session saved successfully to {filename}")

