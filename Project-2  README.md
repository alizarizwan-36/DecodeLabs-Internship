💰 Expense Tracker
A simple command-line Python script that continuously accepts expense entries from a user, accumulates them in real-time, and displays the total amount spent — built as part of the DecodeLabs Industrial Training Kit (Project 2).
📋 Overview
This project demonstrates core backend logic concepts through a practical example:
Accumulator Pattern — maintaining and updating running totals (total += expense)
State Management — initializing variables outside loops so values persist correctly
Defensive Coding — using try/except to handle invalid (non-numeric) input gracefully
Sentinel Values — using a special keyword to gracefully exit an infinite loop
🚀 How It Works
The program starts with total = 0.
It enters an infinite loop, repeatedly asking the user to enter an expense amount.
If the user choose to exit, the loop breaks.
If the user enters a number, it's converted to an integer and added to total.
If the user enters something that isn't a valid number, the program shows an error and asks again — without crashing.
AUTHOR
This project is created by ALIZA RIZWAN , as an intern in the DECODE LABS.
This project was created as part of the DecodeLabs Industrial Training Kit (Batch 2026) for educational purposes.
