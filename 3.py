def analyze_scores(*scores):
    if not scores:
        return 0, 0, 0
    x = sum(scores)
    y = len(scores)
    return x, y, x / y
def print_report(team_name, **info):
    print(team_name)
    for k, v in info.items():
        print(k, v)
print(analyze_scores(8, 10, 7, 9))
print(analyze_scores(5, 5))
print(analyze_scores())
print_report("Комета", coach="Иванов", city="Минск")
