number = int(input("Input the number: "))
nums = [1] * number


def pretty_print(list):
    for item in list:
        print(str(item) + " ", end="")

    print("\n")


def change_value(list, index, value):
    if (len(list) > 1):
        listLength = len(list[index: len(list)])
        i = 0
        ind = index
        while (i < listLength):
            list[ind] = value
            ind += 1
            i += 1
    return list


def update_list(list):
    i = 1
    for item in list:
        pretty_print(list)
        list = change_value(list, i, i + 1)
        i += 1

    return list


def update_list_two(list):
    i = 1
    amount = len(list) + 1
    while (i < amount):
        for j in range(len(list)):

            if (list[j] == i):
                break

            list[j] = i

        pretty_print(list)

        i += 1


def main_update(list):
    list = update_list(list)
    update_list_two(list)


main_update(nums)