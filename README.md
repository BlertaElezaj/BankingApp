# Banking App GUI

## Overview
The **Banking App GUI** is a simple banking application built using Kivy, a Python framework for developing multitouch applications. This app allows users to perform basic banking actions like depositing and withdrawing money from accounts.

## Features
- View multiple accounts with their balance.
- Select actions (Deposit or Withdraw) using a dropdown menu (Spinner).
- Input the amount to be deposited or withdrawn.
- Display the updated balance after performing the action.
- Show success or error messages in popups after each action.

## Installation
To run this application, you need to have Python and Kivy installed. You can install Kivy using `pip`:

### 1. Install Python
Make sure Python (3.6 or higher) is installed on your system. You can download it from the official website: https://www.python.org/

### 2. Install Kivy
Install Kivy using pip by running the following command:

pip install kivy

Run the app using the following command:
python banking_app.py

Account Details
The app displays a list of accounts with the owner's name and balance. Currently, three accounts are predefined:

User1: $500.00
User2: $1000.00
User3: $1500.00
Select Action
A dropdown menu (Spinner) allows the user to choose between two actions:

Deposit: Add money to the account balance.
Withdraw: Subtract money from the account balance.
Input Amount
The user can enter the amount for deposit or withdrawal using a TextInput widget.

Perform Action
A button is provided to perform the selected action on the chosen account. Upon clicking the button, the app will update the balance and show a popup with the result of the action.

Success popups appear when the action is completed successfully.
Error popups appear in case of invalid input (e.g., insufficient balance, non-numeric amount).
Code Structure
BankingAppGUI: The main class that builds the graphical interface of the app.
BaseEnum: Enum that defines possible actions (DEPOSIT and WITHDRAW).
Popup: Displays success or error messages.
Requirements
Python 3.6 or higher
Kivy library
