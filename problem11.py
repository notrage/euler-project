def problem_11():
    with open("problem11.txt", "r") as file:
        data = [list(map(int, a.split(" "))) for a in file.read().split("\n")] 
    print(data)
    
    input: list = [j for j in [i.split(" ") for i in file.read().split("\n")]]
    l: list = []
    for i in range(20):
        for j in range(20):
            if i <= 16: l.append(int(input[i][j])*int(input[i+1][j])*int(input[i+2][j])*int(input[i+3][j]))
            if j <= 16: l.append(int(input[i][j])*int(input[i][j+1])*int(input[i][j+2])*int(input[i][j+3]))
            if i <= 16 and j <= 16: l.append(int(input[i][j])*int(input[i+1][j+1])*int(input[i+2][j+2])*int(input[i+3][j+3]))
            if i >=3 and j >= 3: l.append(int(input[i][j])*int(input[i-1][j-1])*int(input[i-2][j-2])*int(input[i-3][j-3]))
    return max(l)
                