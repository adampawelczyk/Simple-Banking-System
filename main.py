import random
import sqlite3


class BankingSystem:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS card
               (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);""")
        self.conn.commit()
        self.card_number = None
        self.card_pin = None
        self.balance = None

    @staticmethod
    def luhn_alg(card_number):
        number = [int(i) for i in card_number]
        for index, _ in enumerate(number):
            if index % 2 == 0:
                number[index] *= 2
            if number[index] > 9:
                number[index] -= 9
        check_sum = str((10 - sum(number) % 10) % 10)
        card_number += check_sum
        return card_number

    def generate_card_number(self):
        card_number = self.luhn_alg('400000' + str.zfill(str(random.randint(000000000, 999999999)), 9))
        self.cur.execute("""SELECT number FROM card""")
        card_numbers = [row[0] for row in self.cur.fetchall()]
        if card_number in card_numbers:
            self.generate_card_number()
        else:
            return card_number

    def log_in(self):
        self.card_number = input("\nEnter your card number: ")
        self.card_pin = input("Enter your PIN: ")
        self.cur.execute("""SELECT number, pin FROM card WHERE number = ? AND pin = ?;""",
                         (self.card_number, self.card_pin))
        if self.cur.fetchone():
            print("\nYou have successfully logged in!")
            while True:
                print("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5.Log out\n0.Exit")
                choice = input()
                if choice == '1':
                    self.cur.execute("""SELECT balance FROM card WHERE number = ?;""", (self.card_number, ))
                    self.balance = (self.cur.fetchone())[0]
                    print(f"\nBalance: {self.balance}")
                elif choice == '2':
                    self.cur.execute("""SELECT balance FROM card WHERE number = ?;""", (self.card_number, ))
                    self.balance = (self.cur.fetchone())[0]
                    print("Enter income:")
                    income = int(input())
                    self.cur.execute("""UPDATE card SET balance = ? WHERE number = ?;""",
                                     (self.balance + income, self.card_number))
                    self.conn.commit()
                    print("Income was added!")
                elif choice == '3':
                    print("\nTransfer\nEnter card number:")
                    transfer_card_number = input()
                    if transfer_card_number == self.card_number:
                        print("You can't transfer money to the same account!")
                    else:
                        if self.luhn_alg(transfer_card_number[:15]) == transfer_card_number:
                            self.cur.execute("""SELECT number FROM card""")
                            card_numbers = [row[0] for row in self.cur.fetchall()]
                            if transfer_card_number in card_numbers:
                                print("Enter how much money you want to transfer:")
                                self.cur.execute("""SELECT balance FROM card WHERE number = ?;""", (self.card_number, ))
                                self.balance = (self.cur.fetchone())[0]
                                transfer = int(input())
                                if transfer > self.balance:
                                    print("Not enough money!")
                                else:
                                    self.cur.execute("""UPDATE card SET balance = ? WHERE number = ?;""",
                                                     (self.balance - transfer, self.card_number))
                                    self.cur.execute("""SELECT balance FROM card WHERE number = ?;""",
                                                     (transfer_card_number, ))
                                    transfer_balance = (self.cur.fetchone())[0]
                                    self.cur.execute("""UPDATE card SET balance = ? WHERE number = ?;""",
                                                     (transfer_balance + transfer, transfer_card_number))
                                    self.conn.commit()
                                    print("Success!")
                            else:
                                print("Such a card does not exist.")
                        else:
                            print("Probably you made a mistake in the card number. Please try again!")
                elif choice == '4':
                    self.cur.execute("""DELETE FROM card WHERE number = ?;""", (self.card_number,))
                    self.conn.commit()
                    print("The account has been closed!\n")
                    return
                elif choice == '5':
                    print("\nYou have successfully logged out!\n")
                    return
                elif choice == '0':
                    self.cur.close()
                    self.conn.close()
                    print("\nBye!")
                    exit()
                else:
                    print("Unknown option!")
        else:
            print("\nWrong card number or PIN!\n")
            return

    def create_account(self):
        self.card_number = self.generate_card_number()
        self.card_pin = str.zfill(str(random.randint(0000, 9999)), 4)
        self.cur.execute("""INSERT INTO card(number, pin) VALUES (?, ?);""", (self.card_number, self.card_pin))
        self.conn.commit()
        print(f'\nYour card has been created\nYour card number:\n{self.card_number}\nYour card PIN:\n{self.card_pin}\n')

    def menu(self):
        while True:
            print("1. Create and account\n2. Log into account\n0. Exit")
            choice = input()
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.log_in()
            elif choice == '0':
                self.cur.close()
                self.conn.close()
                print("\nBye!")
                exit()
            else:
                print("Unknown option!\n")


BankingSystem().menu()
