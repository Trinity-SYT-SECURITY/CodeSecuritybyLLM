import os


def run_command(user_input):
    command = "ls -l " + user_input
    os.system(command)


run_command("-" * 10000000)
# A buffer overflow vulnerability in Python could occur if an attacker can control the size of input that is processed by the application.
