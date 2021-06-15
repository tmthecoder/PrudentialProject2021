# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd

mentalhealthtech1 = pd.read_csv("datasets/mental-health-in-tech-2016.csv")
# create an empty map
kvSet = {}
# loop through the dataset entry
for x in mentalhealthtech1["Do you currently have a mental health disorder?"]:
    # check if the key exists and increment it or create it
    if x in kvSet.keys():
        kvSet[x] = kvSet[x]+1;
    else:
        kvSet[x] = 0

print(kvSet)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
