def enumerate_list(my_list):
    colors = []
    counter = 0
    for index, elem in enumerate(my_list):
        if elem != "":
            colors.append(f"{counter}. {elem}")
            counter += 1
    return colors

def enumerate_backwards(my_list):
    colors = []
    counter = 0
    for index, elem in enumerate(my_list):
        if elem != "":
            elem = elem[::-1]
            colors.append(f"{counter}. {elem}")
            counter += 1
    return colors
