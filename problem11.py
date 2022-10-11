def problem_11():
    file = open("problem11.txt", "r")
    input_list: list = [i.split(" ") for i in file.read().split("\n")]
    """
    input_list = file.read().split("\n")
    for i in range(len(input_list)):
        input_list[i] = input_list[i].split(" ")
    """