#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:31:19 2022

@author: wiktorklusek

Short Number guessing game in python
"""

import random
number = random.randint(10, 30)

name = input('Enter your name: ')
print(f'Hello, {name}!')



def guessing_game():
    answer = random.randint(0, 100)
    
    while True:
        user_guess = int(input('What is your guess? '))
        
        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        
        elif user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
            
        else:
            print(f'Your guess of {user_guess} is too high!')
            
guessing_game()

