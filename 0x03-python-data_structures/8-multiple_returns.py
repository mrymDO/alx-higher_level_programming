#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(len(sentence)):
        if len(sentence) == 0:
            return len(sentence), "None"
        else:
            return len(sentence), sentence[0]
