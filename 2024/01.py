def get_lists():
    list1 = []
    list2 = []
    with open('01-input', 'r') as file:
        for line in file:
            numbers_in_line = line.split()
            list1.append(int(numbers_in_line[0]))
            list2.append(int(numbers_in_line[1]))
    return list1, list2

def calc_distance(list1, list2):
    distance = 0
    list_length = len(list1)
    for i in range(list_length):
        distance += abs(list1[i] - list2[i])
    return distance

def calc_similarity(list1, list2):
    similarity = 0
    list_length = len(list1)
    for i in range(list_length):
        similarity += list1[i] * list2.count(list1[i])
    return similarity

def main():
    list1, list2 = get_lists()
    list1.sort()
    list2.sort()
    distance = calc_distance(list1, list2)
    print('distance:', distance)
    similarity = calc_similarity(list1, list2)
    print('similarity:', similarity)

if __name__ == '__main__':
    main()
