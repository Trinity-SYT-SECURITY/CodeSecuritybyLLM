import os
import sys


def run_user_input():
    user_input = input("Enter your command: ")
    eval(user_input)


run_user_input()
