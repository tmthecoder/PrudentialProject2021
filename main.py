# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd


def write_analyze_column(dataset, column):
    response_mappings = {}
    for x in dataset[column]:
        if x in response_mappings.keys():
            response_mappings[x] += 1
        else:
            response_mappings[x] = 0

    f = open("datasets/%s.txt" % column, "w")
    for response in response_mappings:
        f.write("%s: %s \n" % (response, response_mappings[response]))
    f.write("Total Responses: %s" % dataset[column].count())


mental_health_tech1 = pd.read_csv("datasets/mental-health-in-tech-2016.csv")
write_analyze_column(mental_health_tech1, "Do you currently have a mental health disorder?")
