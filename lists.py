def lists_example():
    friends_list = ["AK", "MM", "VM", "JM", "FS"]
    print("Names of all friends are: = ", friends_list)
    print("First friend = ", friends_list[0])
    print("reverse list = ", friends_list[::-1])
    print("last item = ", friends_list[-1])
    print("partial list items = ", friends_list[1:4])

def lists_of_lists():
    friends_list = ["AK", "MM", "VM", "JM", "FS"]
    relations_list = ["cousin", "brother", "mom", "dad"]
    people_lists = friends_list + relations_list
    print("people_lists combined list: ", people_lists)

    people_lists = [friends_list, relations_list]
    print("This is now lists of list", people_lists)
    print("people_lists[1][2] = ", people_lists[1][2])
    print("people_lists[0][3] = ", people_lists[0][3])


def main():
    lists_example()
    lists_of_lists()

if __name__ == "__main__":
    main()
