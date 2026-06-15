Password Generator 

A simple Python-based password generator that creates secure random passwords based on user-defined length and calculates their entropy.

Features

* Generates strong random passwords
* Uses letters, digits, and special characters
* Calculates password entropy (security strength estimate)
* Input validation for safe password length
* Simple command-line interface


 How It Works

The program:
1. Asks the user for a password length
2. Validates that the length is **greater than 8 and less than 64**
3. Generates a random password using:

   * Uppercase letters
   * Lowercase letters
   * Numbers
   * Special characters

4. Calculates entropy using:

[
Entropy = \text{length} \times \log_2(\text{number of possible characters})
]

5. Displays the generated password and its strength



Example Output
Enter password length: 12

Generated Password: aB9@kL!2pQ#z
Password Length: 12
Entropy: 78.23 bits


Security Note

This project uses Python’s `random` module for generating passwords. While it is suitable for learning purposes, it is **not cryptographically secure**.

For enterprise level or real world , its good to use secret module.


Author or Intern
Aliza Rizwan 


