# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:14:10 2022

@author: User
"""

# Constants for the Turing machine
BLANK_SYMBOL = 'B'  # Symbol for the blank cell on the tape
HALT_STATE = 'H'  # State in which the Turing machine halts

class TuringMachine:
    def __init__(self, transition_function, initial_state, blank_symbol, halt_state):
        self.transition_function = transition_function
        self.current_state = initial_state
        self.blank_symbol = blank_symbol
        self.halt_state = halt_state
        self.tape = [blank_symbol]
        self.cursor = 0
    
    def step(self):
        current_symbol = self.tape[self.cursor]
        (new_state, new_symbol, direction) = self.transition_function[(self.current_state, current_symbol)]
        self.tape[self.cursor] = new_symbol
        self.current_state = new_state
        if direction == 'L':
            self.cursor -= 1
        elif direction == 'R':
            self.cursor += 1
    
    def run(self):
        while self.current_state != self.halt_state:
            self.step()
    
    def __str__(self):
        return ''.join(self.tape)

# Define the transition function for the Turing machine
transition_function = {
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', BLANK_SYMBOL): ('q2', BLANK_SYMBOL, 'L'),
    ('q2', '0'): ('q2', '0', 'L'),
    ('q2', '1'): ('q2', '1', 'L'),
    ('q2', BLANK_SYMBOL): ('q3', '1', 'R'),
    ('q3', '0'): ('q3', '1', 'R'),
    ('q3', '1'): ('q3', '0', 'R'),
    ('q3', BLANK_SYMBOL): ('H', BLANK_SYMBOL, 'R'),
}

# Create a Turing machine and run it
tm = TuringMachine(transition_function, 'q1', BLANK_SYMBOL, 'H')
tm.tape = list('101B10001')
tm.run()
print(tm)  # Output: '110001'
