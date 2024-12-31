def likes(names):
    if len(names) > 2 :
        for name in names :
            if name == names[len(names) - 1] :
                print("and", end=" ")
                print(name, end=" ")
                break
            print(name, end="")
            print(",", end=" ")
        print("likes this")
    elif len(names) == 2 :
        print(names[0], "and", names[1], "likes this")
    elif len(names) == 1 :
        print(names[0], "likes this")

    else :
        print("no one likes this")
    pass


list = ["Peter", "John", "Dick"]
list2 = ["Nathan"]
likes(['Peter'])