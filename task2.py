input_keys = input()
keys_list = input_keys.split(" ")
input_values = input()
values_list = input_values.split(" ")
fin_dict = {}
iteration_number = 0
for keys in keys_list:
    if iteration_number < len(values_list):
        fin_dict[keys] = values_list[iteration_number]
    else:
        fin_dict[keys] = None
    iteration_number += 1
print(fin_dict)
