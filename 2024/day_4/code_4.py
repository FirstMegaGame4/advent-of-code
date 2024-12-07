### Common

def collect_input() -> list[str]:
    return [string.replace("\n", "") for string in open("./input_4.txt")]

def flatten(array: list[list]) -> list:
    result = []
    for sub in array:
        for item in sub:
            result.append(item)
    return result

### Part 1

def rotate(content: list[str], factor_45_degrees: int) -> list[str]:
    factor_45_degrees = factor_45_degrees % 8
    if factor_45_degrees % 2 == 0:
        rotated = ["" for _ in range(len(content))]
        for j in range(len(content)):
            for i in range(len(content)):
                match factor_45_degrees:
                    case 0: rotated[i] = rotated[i] + content[i][j]
                    case 2: rotated[i] = content[-j - 1][-i - 1] + rotated[i]
                    case 4: rotated[i] = content[-i - 1][j] + rotated[i]
                    case 6: rotated[-i - 1] = content[j][-i - 1] + rotated[-i - 1]
        return rotated
    else:
        rotated = ["" for _ in range(len(content * 2) - 1)]
        for i in range(len(content)):
            j = 0
            for k in range(len(content) - i):
                if k != len(content) - i - 1: # Prevent the diagonal to appear twice
                    match factor_45_degrees:
                        case 1: rotated[i + j] += content[i][-k - 1]
                        case 3: rotated[i + j] += content[i][k]
                        case 5: rotated[i + j] = content[i][-k - 1] + rotated[i + j]
                        case 7: rotated[i + j] = content[i][k] + rotated[i + j]
                    j += 1
            l = 0
            for m in reversed(range(i + 1)):
                match factor_45_degrees:
                    case 1: rotated[len(content) - 1 + l] += content[i][m]
                    case 3: rotated[len(content) - 1 + l] += content[i][-m - 1]
                    case 5: rotated[len(content) - 1 + l] = content[i][m] + rotated[len(content) - 1 + l]
                    case 7: rotated[len(content) - 1 + l] = content[i][-m - 1] + rotated[len(content) - 1 + l]
                l += 1
        return rotated if factor_45_degrees != 3 and factor_45_degrees != 5 else list(reversed(rotated))

def count_xmas_iterations() -> int:
    total = 0
    collected_input = collect_input()
    for string in flatten([rotate(collected_input, i) for i in range(8)]):
        for i in range(len(string) - 3):
            if string[i:i+4] == "XMAS":
                total += 1
    return total

### Part 2

def check_x_mas(content: list[str], x: int, y: int) -> bool:
    if 0 < x < len(content) - 1 and 0 < y < len(content) - 1 and content[x][y] == "A":
        fitting_diagonals = 0
        if content[x - 1][y - 1] + content[x][y] + content[x + 1][y + 1] == "MAS":
            fitting_diagonals += 1
        elif content[x + 1][y + 1] + content[x][y] + content[x - 1][y - 1] == "MAS":
            fitting_diagonals += 1
        if content[x - 1][y + 1] + content[x][y] + content[x + 1][y - 1] == "MAS":
            fitting_diagonals += 1
        elif content[x + 1][y - 1] + content[x][y] + content[x - 1][y + 1] == "MAS":
            fitting_diagonals += 1
        if fitting_diagonals == 2:
            return True
    return False

def count_x_mas_iterations() -> int:
    total = 0
    collected_input = collect_input()
    for i in range(len(collected_input)):
        for j in range(len(collected_input)):
            if check_x_mas(collected_input, i, j):
                total += 1
    return total

if __name__ == '__main__':
    ### Part 1
    print(count_xmas_iterations())
    ### Part 2
    print(count_x_mas_iterations())
