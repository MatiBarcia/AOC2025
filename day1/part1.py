import sys

STARTING_POINT=50 # number between 1 and 99

file_name = sys.argv[1]

if __name__ == '__main__':
    actual_number = STARTING_POINT

    with open(file_name, "r") as input:
        password = 0
        for line in input:
            line = line.strip()
            if line[0] == 'R': # add
                next_rotation = int(line[1:])
                actual_number += next_rotation
                
                while actual_number > 99:
                    actual_number -= 100
                if actual_number == 0:
                    password += 1

            elif line[0] == 'L': # sub
                next_rotation = int(line[1:])
                actual_number -= next_rotation
                
                while actual_number < 0:
                    actual_number += 100
                if actual_number == 0:
                    password += 1

            else: # error
                print("There's an error with the input.")
                
        print(f"The password is: {password}")
    