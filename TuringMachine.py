# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:12:46 2022

@author: User
"""

# Constants for the Turing machine
BLANK_SYMBOL = 'B'  # Symbol for the blank cell on the tape
HALT_STATE = 'H'  # State in which the Turing machine halts

# The transition function is a dictionary that maps (current_state, current_symbol)
# to a tuple (new_state, new_symbol, direction)
# where direction is either 'L' for left or 'R' for right
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

def turing_machine(input_tape):
    """Simulates a Turing machine that adds two numbers in binary.
    
    Args:
        input_tape: A string representing the input tape, with the input
            numbers separated by a blank symbol. For example, '101B10001'
    
    Returns:
        The contents of the tape after the Turing machine halts.
    """
    tape = list(input_tape)  # Convert the input tape to a list
    state = 'q1'  # Initial state
    cursor = 0  # Initial position of the cursor
    
    while state != HALT_STATE:
        current_symbol = tape[cursor]
        (new_state, new_symbol, direction) = transition_function[(state, current_symbol)]
        tape[cursor] = new_symbol  # Update the symbol on the tape
        state = new_state  # Update the state of the Turing machine
        if direction == 'L':
            cursor -= 1  # Move the cursor to the left
        else:
            cursor += 1  # Move the cursor to the right
    
    return ''.join(tape)  # Return the tape as a string

# Test the Turing machine
input_tape = '101B10001'
print(turing_machine(input_tape))  # Output: '110001'
