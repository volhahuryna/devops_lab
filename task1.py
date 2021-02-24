number = int(input())
names = {}
for i in range(number):
    input_string = input()
    name = input_string.split(" ")[0]
    marks_string = input_string.split(" ")[1:]
    marks_float = list()
    for mark in marks_string:
        marks_float.append(float(mark))
    names[name] = marks_float
selected_name = input()
average_mark = sum(names[selected_name])/len(names[selected_name])
print("{:.2f}".format(average_mark))
