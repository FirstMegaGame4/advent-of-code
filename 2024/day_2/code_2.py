### Common

def collect_input() -> list[list[int]]:
    reports = []
    for line in open("./input_2.txt"):
        reports.append(list(map(lambda x: int(x), line.split(" "))))
    return reports

def is_safe(report: list[int]) -> bool:
    if sorted(report) == report or sorted(report, reverse=True) == report:
        safe = True
        for i in range(len(report) - 1):
            difference = abs(report[i] - report[i + 1])
            if difference < 1 or difference > 3:
                safe = False
        return safe

### Part 1

def count_safe_reports() -> int:
    counter = 0
    for report in collect_input():
        if is_safe(report):
            counter += 1
    return counter

### Part 2

def count_safe_reports_with_problem_dampener() -> int:
    counter = 0
    for report in collect_input():
        safe = False
        for sub_report in [report[0:i] + report[i+1:len(report)] for i in range(len(report))]:
            if is_safe(sub_report):
                safe = True
        if safe:
            counter += 1
    return counter

if __name__ == '__main__':
    ### Part 1
    print(count_safe_reports())
    ### Part 2
    print(count_safe_reports_with_problem_dampener())
