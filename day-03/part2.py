import sys

file_name = sys.argv[1]

if __name__ == "__main__":
    with open(file_name, "r") as input:
        result = 0
        
        for line in input:
            line = line.strip('\n')
            line_length = len(line) # 15
            counter = 11
            highest_number = ""

            while line_length - counter > 0 and counter >= 0:
                max_index = 0
                for i in range(line_length - counter):
                    if int(line[max_index]) < int(line[i]):
                        max_index = i

                highest_number += line[max_index]
                line = line[max_index + 1:]
                line_length = len(line)
                counter -= 1
            
            if counter >= 0:
                highest_number += line

            result += int(highest_number)
        
        print(f"The answer is: {result}")