#!/usr/bin/env python
#
# The following functions are useful in this snippet:
#
#     * random.choice(seq) - https://docs.python.org/3/library/random.html#random.choice
#     * time.sleep(sec) - https://docs.python.org/3/library/time.html#time.sleep
#
# Dictionary keys can be accessed by:
#
#     * dict.keys()
#
# The print function takes an optional "flush" argument. To immediately see the
# output of a "print" if you haven't used a newline as the "end" character, set
# "flush" to "True", e.g.
#
#     print("hello", end=" ", flush=True)
#
# Background: this is a performance tweak, called buffered I/O.
#


import argparse
import pickle
import random
import time

def generate_text(model, prompt, length=50, fake_ai_delay=0.2):
    """
    Given a model and a "prompt" (here, it is just an N-gram that we can lookup
    in the model dictionary), choose a random next word and iterate until a
    text of a given length is generated.
    """
    print(" ".join(prompt), end=" ")
    # Given the length, for the current "prompt", pick a random choice from a
    # list of follow up words.
    #
    # If a "prompt" is not found in the dictionary, return or raise an exception.
    #
    # Bonus: add a "fake ai delay" (via time.sleep, https://docs.python.org/3/library/time.html)
    # to the tokens do not appear immediately but are added after a short
    # delay. The print function has a "flush" argument, that may be required to
    # see the effect.
    for i in range(length):
        if prompt in model:
            word = random.choice(model[prompt])
            print(word, end=" ", flush=True)
            time.sleep(fake_ai_delay)
            prompt = (*prompt[1:], word)
        else:
            raise ValueError("no such prompt: {}".format(prompt))


print(r"""

 __  __    __    ____  _  _  _____  _  _  ___  _   _    __   ____
(  \/  )  /__\  (  _ \( )/ )(  _  )( \/ )/ __)( )_( )  /__\ (_  _)
 )    (  /(__)\  )   / )  (  )(_)(  \  /( (__  ) _ (  /(__)\  )(
(_/\/\_)(__)(__)(_)\_)(_)\_)(_____)  \/  \___)(_) (_)(__)(__)(__) 3.5

""")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Choose a random starting "prompt", that is: use random.choice from the keys
# of the model.
initial_prompt = random.choice(list(model.keys()))

# Generate some text. Pass the model (dictionary), the initial prompt as a
# tuple. Optionally, pass the length of the text to generate and a fake ai
# delay.
generate_text(model, initial_prompt, length=100, fake_ai_delay=0.2)
print()
