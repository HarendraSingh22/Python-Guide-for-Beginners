# This Python file uses the following encoding: utf-8
import os, sys, random


def gjettelek(hoyest):
    tilfeldig_tall = random.randint(1, hoyest)
    gjettet = False

    while (not(gjettet)):
        try:
            input_gjettet = int(input("Guess a number: "))

            if (input_gjettet == tilfeldig_tall):
                print("You got it right!")
                gjettet = True

            elif (input_gjettet > tilfeldig_tall):
                print("The number is lower!")

            else:
                print("The number is higher!")


        except ValueError:
            print("You didn't write a number!")


def get_values():
    try:
        hoyest = int(input("Write your upper limit: "))
        gjettelek(hoyest)

    except ValueError:
        print("You didn't write in a number, try again!")
        get_values()


get_values()
