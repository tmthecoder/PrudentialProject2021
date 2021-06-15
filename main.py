import pandas as pd


def write_analyze_column(dataset, column):
    response_mappings = {}
    for x in dataset[column]:
        if x in response_mappings.keys():
            response_mappings[x] += 1
        else:
            response_mappings[x] = 0
    file_name = column.replace(" ", "_").replace("?", "").replace(".", "")
    f = open("datasets/%s.txt" % file_name, "w")
    for response in response_mappings:
        f.write("%s: %s \n" % (response, response_mappings[response]))
    f.write("Total Responses: %s" % dataset[column].count())


mental_health_tech1 = pd.read_csv("datasets/mental-health-in-tech-2016.csv")
write_analyze_column(mental_health_tech1, "Do you currently have a mental health disorder?")
