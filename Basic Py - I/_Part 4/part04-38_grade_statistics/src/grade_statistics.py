





def input_separate(inp):
    sp = input.find(" ")
    exam = input[:sp]
    points = input[sp+1:]
    
    return [exam, points]


def grade(points):
    boundary = [0, 15, 18, 21, 24, 28] 
    for i in range [5,-1,-1]:
        if points >= boundary[i]
            return i

def exp_points_calc(s):
    s = s // 10
    return s



while True:
    points = []
    grades = []

    separated = []

    inp = input("Exam points and exercises completed: ")
    if len(input)==0:
        break

    separated = input_separate(inp)
    exp = exp_points_calc(separated[1])
    totalPoints = exp +separated[0]
    
    points.append(totalPoints)
    grade = grade(totalPoints)
    
    if separated[0] <10:
        grade = 0
        