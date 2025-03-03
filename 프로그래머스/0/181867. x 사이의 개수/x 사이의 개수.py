###틀린문제



def solution(myString):
    parts = myString.split('x')         # "x"를 기준으로 문자열을 나눕니다.
    answer = [len(part) for part in parts]  # 각 부분의 길이를 계산합니다.
    return answer
