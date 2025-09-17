# Open the file named 'sample.txt' for reading
file = open('sample.txt', 'r')

# Go through each line in the file, keeping track of the line number
line_number = 1
for line in file:
    # Print the line number and the line content
    print(str(line_number) + ': ' + line.strip())
    line_number += 1

# Close the file when done
file.close()