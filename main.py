import json
import random
from datetime import datetime

with open("tips.json", "r") as file:
    data = json.load(file)

name = input("Enter your name: ")

print("\nHello", name + "!")
print("Welcome to Smart Student Assistant")

print("\n1. Generate Study Tip")
print("2. Generate Motivation Quote")
print("3. Display Current Date & Time")

choice = input("Enter your choice: ")

if choice == "1":
    output = "Study Tip: " + random.choice(data["study_tips"])

elif choice == "2":
    output = "Motivation Quote: " + random.choice(data["quotes"])

elif choice == "3":
    now = datetime.now()
    output = "Current Date and Time: " + now.strftime("%d-%m-%Y %I:%M %p")

else:
    output = "Invalid Choice"

print("\n" + output)

with open("output.txt", "a") as file:
    file.write("Name: " + name + "\n")
    file.write(output + "\n")
    file.write("---------------------\n")

print("\nOutput saved in output.txt")
