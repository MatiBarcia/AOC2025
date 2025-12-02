import sys

file_name = sys.argv[1]

if __name__ == "__main__":
    with open(file_name, "r") as input:
        line = input.readline()
        id_ranges = line.split(",")

        result = 0

        for i in range(len(id_ranges)):
            min, max = id_ranges[i].split("-")
            for id in range(int(min),int(max)+1):
                length = len(str(id))
                mid = length // 2

                if str(id)[:mid] == str(id)[mid:]:
                    result += id
        
        print(f"Adding up all the invalid IDs produces: {result}")