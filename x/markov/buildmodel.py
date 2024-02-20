#!/usr/bin/env/python

"""
Takes a stream of text, normalizes it to tokens and then builds a language
model, that is note the successor token for each every two token sequence.

Write this dictionary to a file (as pickle).
"""

import collections
import string
import pickle


def sanitize(tok):
    """ Only keeps ascii chars from a token. """
    return "".join([c for c in tok if c in string.ascii_lowercase])


def tokenize(s):
    """ Turn a string intro a list of tokens. """
    # TODO: think of a good way to "normalize" the input, that is to make it
    # less heterogeneous. Some ideas: only use lowercase, use the "sanitize"
    # function on each token, only accept sanitized tokens with length > 1.
    raw = [tok for tok in s.lower().split()]
    sanitized = [sanitize(tok) for tok in raw]
    sanitized = [tok for tok in sanitized if len(tok) > 1]
    return sanitized

# use n-grams: number of predecessor tokens (reasonable values between 1 to 5, maybe)
N = 2

# The model maps n-gram to a list of possible successor,
# e.g. for N=2 and inputs like "it is rainy", "it is sunny"
# we would get {("it", "is"): ["rainy", "sunny"]}
model = collections.defaultdict(list)

with open("corpus.txt") as f:
    data = f.read()
    tokens = tokenize(data)

# TODO: build the model (which is a dictionary): iterate over the corpus (list
# of tokens) and collect for all two-token inputs the successor token.  For the
# dictionary keys, we need an immutable value - we cannot use a list, but we
# can use tuple for example, e.g. ("a", "b") would be a valid dictionary key.
for i in range(N, len(tokens) - N):
    key = tuple(tokens[i - k] for k in range(N, 0, -1))
    value = tokens[i]
    model[key].append(value)

# print(model)

# Write the model (dictionary) to a file, so we can read it later in another program.
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

