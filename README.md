# Coffee-Maker-Machine

☕ Coffee Machine - Python Project

Overview
This is a simple terminal-based **Coffee Machine simulation** written in Python. It allows users to order drinks like **Espresso, Latte**, and **Cappuccino**, processes coin payments, checks for ingredient availability, and keeps track of earnings and resources.

---

Features
- Offers 3 types of drinks: Espresso, Latte, Cappuccino
- Checks if ingredients are sufficient
- Accepts payment in coins (quarters, dimes, nickels, pennies)
- Gives change if payment exceeds drink cost
- Tracks profit and remaining resources
- Option to print a resource report
- Option to exit the program

Requirements

- Python 3.x

No external libraries are required.

How to Run
1. **Clone or download** the repository.
2. Open a terminal and navigate to the directory containing the Python file.
3. Run the script:

```bash
python coffee_machine.py
```

Menu Options

You will be presented with the following options:

- `1. Espresso`
- `2. Latte`
- `3. Cappuccino`
- `4. Report` — Displays remaining resources and total money earned.
- `5. Exit` — Shuts down the machine.

Alternatively, you can type:  
- `espresso`, `latte`, `cappuccino`, `report`, or `exit`.

Example Interaction

```
Welcome to the Coffee Machine!

Please select an option:

1. Espresso
2. Latte
3. Cappuccino
4. Report
5. Exit

What would you like to order? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0
Here is $0.0 in change.
Here is your latte ☕. Enjoy!

License

This project is for educational purposes and is free to use or modify.
