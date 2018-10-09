def nested_list(num, *argv):
    highest = 0
    highest_list = []
    second_highest = 0
    second_highest_list = []
    for arg in argv:
        name = arg[0]
        score = float(arg[1])
        if score > highest:
            second_highest = highest
            second_highest_list = highest_list.copy()
            highest = score
            highest_list.append(name)
        elif score is highest:
            highest_list.append(name)
        elif score is second_highest:
            second_highest_list.append(name)
    for name in second_highest_list:
        print(name)


nested_list(5, ["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39])