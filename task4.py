input_string = input()
splitting_string = input_string.split(" ")
output_string = "-".join(word for word in splitting_string)
print(output_string)