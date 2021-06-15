# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd

mentalhealthtech1 = pd.read_csv("datasets/mental-health-in-tech-2016.csv")

responseMappings = {}

for x in mentalhealthtech1["Do you currently have a mental health disorder?"]:
    if x in responseMappings.keys():
        responseMappings[x] += 1
    else:
        responseMappings[x] = 0
print("Response Counts: " + responseMappings)
print("Total Responses: " + mentalhealthtech1["Do you currently have a mental health disorder?"].count())
