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
write_analyze_column(mental_health_tech1, "Do you have a family history of mental illness?")
write_analyze_column(mental_health_tech1, "Have you had a mental health disorder in the past?")
write_analyze_column(mental_health_tech1, "If you have revealed a mental health issue to a client or business contact, "
                                          "do you believe this has impacted you negatively?")
write_analyze_column(mental_health_tech1, "Did your previous employers ever formally discuss mental health (as part of "
                                          "a wellness campaign or other official communication)?")
write_analyze_column(mental_health_tech1, "Would you have been willing to discuss a mental health issue with your "
                                          "previous co-workers?")
write_analyze_column(mental_health_tech1, "Do you feel that your employer takes mental health "
                                          "as seriously as physical health?")
write_analyze_column(mental_health_tech1, "Did you hear of or observe negative consequences for co-workers with "
                                          "mental health issues in your previous workplaces?")
write_analyze_column(mental_health_tech1, "Have you observed or experienced an unsupportive or badly handled response "
                                          "to a mental health issue in your current or previous workplace?")
write_analyze_column(mental_health_tech1, "If you have a mental health issue, do you feel that it interferes"
                                          " with your work when being treated effectively?")
write_analyze_column(mental_health_tech1, "If you have a mental health issue, do you feel that it "
                                          "interferes with your work when NOT being treated effectively?")
write_analyze_column(mental_health_tech1, "Are you self-employed?")
# write_analyze_column(mental_health_tech1, "Do you have medical coverage (private insurance or state-provided) which"
#                                           " includes treatment of  mental health issues?")
write_analyze_column(mental_health_tech1, "Have your previous employers provided mental health benefits?")
write_analyze_column(mental_health_tech1, "Did your previous employers provide resources to learn more about mental"
                                          " health issues and how to seek help?")
