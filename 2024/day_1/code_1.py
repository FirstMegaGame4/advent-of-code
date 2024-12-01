### Common

def collect_input() -> tuple[list, list]:
    first_list = []
    last_list = []
    for line in open("./input_1.txt"):
        temp = line.split("   ")
        first_list.append(int(temp[0]))
        last_list.append(int(temp[1]))
    return first_list, last_list

### Part 1

def total_distance() -> int:
    first_list, last_list = collect_input()
    if len(first_list) == len(last_list):
        first_list_sorted = sorted(first_list)
        last_list_sorted = sorted(last_list)
        distances = []
        for i in range(len(first_list)):
            distances.append(abs(first_list_sorted[i] - last_list_sorted[i]))
        return sum(distances)
    else:
        raise Exception("your input_1.txt file is likely fucked up")

### Part 2

def similarity_score() -> int:
    score = 0
    first_list, last_list = collect_input()
    for num in first_list:
        score += num*len(list(filter(lambda x: x == num, last_list)))
    return score

if __name__ == '__main__':
    ### Part 1
    print(total_distance())
    ### Part 2
    print(similarity_score())
