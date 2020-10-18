# Project Name
> Simple-Banking-System

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Code Examples](#code-examples)
* [Features](#features)
* [Status](#status)

## General info
Everything goes digital these days, and so does money. Today, most people have credit cards, which save us time, energy and nerves. From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways.
This project imitates a simple banking system using sql and Luhn's algorithm

## Technologies
* python - version 3.8
* sqlite3 - version 3.33.0

## Code Examples
```
1. Create and account
2. Log into account
0. Exit
1

Your card has been created
Your card number:
4000009409699280
Your card PIN:
2530

1. Create and account
2. Log into account
0. Exit
1

Your card has been created
Your card number:
4000001876936998
Your card PIN:
9320

1. Create and account
2. Log into account
0. Exit
2

Enter your card number: 4000009409699280
Enter your PIN: 2530

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
2
Enter income:
10000
Income was added!

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
1

Balance: 10000

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
3

Transfer
Enter card number:
4000001876936997
Probably you made a mistake in the card number. Please try again!

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
3

Transfer
Enter card number:
4000003305061034
Such a card does not exist.

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
3

Transfer
Enter card number:
4000009409699280
You can't transfer money to the same account!

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
3

Transfer
Enter card number:
4000001876936998
Enter how much money you want to transfer:
15000
Not enough money!

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
3

Transfer
Enter card number:
4000001876936998
Enter how much money you want to transfer:
5000
Success!

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
5

You have successfully logged out!

1. Create and account
2. Log into account
0. Exit
2

Enter your card number: 4000001876936998
Enter your PIN: 9320

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
1

Balance: 5000

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
5

You have successfully logged out!

1. Create and account
2. Log into account
0. Exit
0

Bye!

Process finished with exit code 0
```
```
1. Create and account
2. Log into account
0. Exit
1

Your card has been created
Your card number:
4000007976430857
Your card PIN:
6049

1. Create and account
2. Log into account
0. Exit
2

Enter your card number: 4000007976430857
Enter your PIN: 6049

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5.Log out
0.Exit
4
The account has been closed!

1. Create and account
2. Log into account
0. Exit
2

Enter your card number: 4000007976430857
Enter your PIN: 6049

Wrong card number or PIN!

1. Create and account
2. Log into account
0. Exit
0

Bye!

Process finished with exit code 0
```

## Features
List of features
* Luhn's algorithm
* create new account with random generated card number and card pin
* login into account using card number and card pin
* see current balance
* add income
* do money transfer to any card number existing in the database
* close account

## Status
Project is: _finished_
