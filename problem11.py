def problem_11() -> int:
    with open("problem11.txt", "r") as file: data = [list(map(int, a.split(" "))) for a in file.read().split("\n")]    
    l: list = []
    for i in range(20):
        for j in range(20):
            if i <= 16: l.append(data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j])
            if j <= 16: l.append(data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3])
            if i <= 16 and j <= 16: l.append(data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3])
            if i <= 16 and j >= 3: l.append(data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3])
    return max(l)