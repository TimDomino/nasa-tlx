#!/usr/bin/python3

## install: pip3 install appjar
from appJar import gui

## Texts for the individual questionnaire items
texts = ["Mental Demand    -    How mentally demanding was the task?",
         "Physical Demand    -    How physically demanding was the task?",
         "Temporal Demand    -    How hurried or rushed was the pace of the task?",
         "Performance    -    How successful were you in accomplishing what you were asked to do?",
         "Effort    -    How hard did you have to work to accomplish your level of performance?",
         "Frustration    -    How insecure, discouraged, irritated, stressed and annoyed were you?"]

## Labels on the left and right sides of the scale
left_labels = ["Very Low", "Very Low", "Very Low", "Perfect", "Very Low", "Very Low"]
right_labels = ["Very High", "Very High", "Very High", "Failure", "Very High", "Very High"]

## Labels of the Conditions to be chosen from
conditions = ["Condition 1", "Condition 2"]

## Experiments to be chosen from
experiments = ["Experiment 1", "Experiment 2"]


## Called when the submit button is clicked
def on_submit():
    experiment = app.getOptionBox("Experiment")
    user_id = app.getSpinBox("User ID")
    condition = app.getOptionBox("Condition")

    write_string = ''
    write_string += str(experiment) + ','
    write_string += str(user_id) + ','
    write_string += str(condition)

    for i in range(len(texts)):
        write_string += ',' + str(app.getScale("q" + str(i)) * 5)

    file_handle = open("nasa-tlx-results.txt", "a")
    file_handle.write(write_string + '\n')
    file_handle.close()
    print("The results were written successfully.")
    app.stop()


## Main entry point
app = gui()
app.setTitle("NASA-TLX")
app.setSize(1000, 700)
app.setFont(10)

app.addLabelOptionBox("Experiment", experiments, 0, 0)
app.addLabelSpinBoxRange("User ID", 1, 200, 0, 1)
app.addLabelOptionBox("Condition", conditions, 0, 2)
app.addHorizontalSeparator(2, 0, 3)

for i, entry in enumerate(texts):
    app.setSticky("we")
    app.addLabel("q" + str(i) + "_text", entry, 4*i + 3, 1)

    app.setSticky("e")
    app.addLabel("q" + str(i) + "_label_left", left_labels[i], 4*i + 1 + 3, 0)
    app.setSticky("we")
    app.addScale("q" + str(i), 4*i + 1 + 3, 1)
    app.setSticky("w")
    app.addLabel("q" + str(i) + "_label_right", right_labels[i], 4*i + 1 + 3, 2)

    app.setScaleRange("q" + str(i), 0, 20, 10)
    app.setScaleIncrement("q" + str(i), 1)

    app.setSticky("we")
    app.addLabel("ticks_q" + str(i), "||", 4*i + 2 + 3, 1)
    app.addHorizontalSeparator(4*i + 3 + 3, 0, 3)

app.setSticky("we")
app.addButton("Submit", on_submit, 4*len(texts) + 1 + 3, 1)

app.go()
