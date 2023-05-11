# Open the input file for reading

line_len = 80

my_input_file_path = "a14_exercise_threshold_decorator/a14_exercise_text"


def line_breaker(input_file_path):
    output_file_path = input_file_path + "_formatted"
    with open(input_file_path, 'r') as input_file:
        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Loop through each line in the input file
            for line in input_file:
                words = line.split()
                output_line = ""
                for word in words:
                    if len(output_line) + len(word) > line_len:
                        output_file.write(output_line + "\n")
                        output_line = ""

                    output_line += word + " "
                output_file.write(output_line + "\n")


line_breaker(my_input_file_path)

# Prüfen wenn leere Zeile ist diese in outputfile übernehmen.
