import sys

file_name = sys.argv[1]

if __name__ == "__main__":
    with open(file_name, "r") as input:
        result = 0
        for line in input:
            line_length = len(line)
            
            first_index = 0
            max_first_number = line[0]

            for i in range(line_length-2): # not taking the last one
                if int(max_first_number) < int(line[i]):
                    max_first_number = line[i]
                    first_index = i

            max_second_number = line[first_index+1]
        
            for i in range(first_index+1,line_length-1):
                if int(max_second_number) < int(line[i]):
                    max_second_number = line[i]

            max_number = max_first_number + max_second_number

            result += int(max_number)
        
        print(f"The answer is: {result}")