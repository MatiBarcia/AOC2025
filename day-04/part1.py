import sys

file_name = sys.argv[1]

if __name__ == "__main__":
    with open(file_name, "r") as input:
        lines = input.readlines()
        num_lines = len(lines)
        counter = 0
        
        for i in range(num_lines):
            if i == 0: # first line
                for j in range(len(lines[i])):
                    aux_line = ''
                    if lines[i][j] == '@':
                        if j == 0:
                            aux_line = lines[i][j+1] + lines[i+1][j] + lines[i+1][j+1]
                        elif j == len(lines[i].strip('\n'))-1:
                            aux_line = lines[i][j-1] + lines[i+1][j-1] + lines[i+1][j]
                        else:
                            aux_line = lines[i][j-1] + lines[i][j+1] + lines[i+1][j-1] + lines[i+1][j] + lines[i+1][j+1]
                        
                        if aux_line.count('@') < 4:
                            counter += 1
            elif i == num_lines-1: # last line
                for j in range(len(lines[i])):
                    aux_line = ''
                    if lines[i][j] == '@':
                        if j == 0:
                            aux_line = lines[i][j+1] + lines[i-1][j] + lines[i-1][j+1]
                        elif j == len(lines[i].strip('\n'))-1:
                            aux_line = lines[i][j-1] + lines[i-1][j-1] + lines[i-1][j]
                        else:
                            aux_line = lines[i][j-1] + lines[i][j+1] + lines[i-1][j-1] + lines[i-1][j] + lines[i-1][j+1]
                        
                        if aux_line.count('@') < 4:
                            counter += 1
            else: # every other line
                for j in range(len(lines[i])):
                    aux_line = ''
                    if lines[i][j] == '@':
                        if j == 0:
                            aux_line = lines[i][j+1] + lines[i-1][j] + lines[i-1][j+1] + lines[i+1][j] + lines[i+1][j+1]
                        elif j == len(lines[i].strip('\n'))-1:
                            aux_line = lines[i][j-1] + lines[i-1][j-1] + lines[i-1][j] + lines[i+1][j-1] + lines[i+1][j]
                        else:
                            aux_line = lines[i][j-1] + lines[i][j+1] + lines[i-1][j-1] + lines[i-1][j] + lines[i-1][j+1] + lines[i+1][j-1] + lines[i+1][j] + lines[i+1][j+1]
                        
                        if aux_line.count('@') < 4:
                            counter += 1

        print(f"The answer is: {counter}")