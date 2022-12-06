def solution(quizzes):
    results = []
    for quiz in quizzes:
        equation = quiz.split(" ")
        x = int(equation[0])
        y = int(equation[2])
        z = int(equation[4])
        symbol = equation[1]

        answer = False
        if symbol == "+":
            answer = x + y == z
        elif symbol == "-":
            answer = x - y == z

        if answer:
            results.append("O")
        else:
            results.append("X")
    return results