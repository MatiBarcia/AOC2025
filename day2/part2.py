import sys

file_name = sys.argv[1]

def split_in_n_parts(text, n):
    part_size = len(text) // n
    parts = []

    for i in range(n):
        start = i * part_size
        
        if i == n - 1:
            part = text[start:]
        else:
            end = start + part_size
            part = text[start:end]
        
        parts.append(part)
    
    return parts

if __name__ == "__main__":
    with open(file_name, "r") as input:
        line = input.readline()
        id_ranges = line.split(",")

        result = 0

        for i in range(len(id_ranges)):
            min, max = id_ranges[i].split("-")

            for id in range(int(min),int(max)+1):
                length = len(str(id))

                for i in range(2,length+1):
                    parts = split_in_n_parts(str(id),i)

                    if len(set(parts)) == 1:
                        result += id
                        break
        
        print(f"Adding up all the invalid IDs produces: {result}")