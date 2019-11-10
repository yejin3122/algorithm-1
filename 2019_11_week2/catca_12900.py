def solution(n):
    answer1, answer2 = 0, 1
    for i in range(n):
        answer1, answer2 = answer2, answer1 + answer2
    return answer2 % 1000000007
