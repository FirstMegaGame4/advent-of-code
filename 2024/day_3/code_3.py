### Common

def collect_input() -> str:
    string = ""
    for line in open("./input_3.txt"):
        string += line
    return string

### Part 1 (conditional_statements=False)
### Part 2 (conditional_statements=True)

def multiplications_sum(conditional_statements: bool) -> int:
    collected_input = collect_input()
    total = 0
    enabled = True
    for i in range(len(collected_input)):
        if i <= len(collected_input) - 4 and collected_input[i:i+4] == "mul(" and (not conditional_statements or enabled):
            first_number = ""
            find_first_number = True
            j = 1
            while find_first_number:
                if collected_input[i+3+j].isdigit():
                    first_number += collected_input[i+3+j]
                    j += 1
                elif collected_input[i+3+j] == "," and len(first_number) > 0:
                    second_number = ""
                    find_second_number = True
                    k = 1
                    while find_second_number:
                        if collected_input[i+3+j+k].isdigit():
                            second_number += collected_input[i+3+j+k]
                            k += 1
                        elif collected_input[i+3+j+k] == ")" and len(second_number) > 0:
                            total += int(first_number) * int(second_number)
                            find_first_number = False
                            find_second_number = False
                        else:
                            find_first_number = False
                            find_second_number = False
                else:
                    find_first_number = False
        elif conditional_statements:
            if i <= len(collected_input) - 4 and collected_input[i:i+4] == "do()":
                enabled = True
            elif i <= len(collected_input) - 7 and collected_input[i:i+7] == "don't()":
                enabled = False
    return total

if __name__ == '__main__':
    ### Part 1
    print(multiplications_sum(False))
    ### Part 2
    print(multiplications_sum(True))
