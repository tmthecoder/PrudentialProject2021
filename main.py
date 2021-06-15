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
print("Response Counts: %s" % responseMappings)
print("Total Responses: %s" % mentalhealthtech1["Do you currently have a mental health disorder?"].count())

f = open("datasets/Do_you_currently_have_a_mental_health_disorder.txt", "w")
f.write("Response Counts: %s" % responseMappings)
f.write("Total Responses: %s" % mentalhealthtech1["Do you currently have a mental health disorder?"].count())


