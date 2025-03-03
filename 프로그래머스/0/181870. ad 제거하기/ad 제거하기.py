###틀린문제
# def solution(strArr):
#     answer = []
#     strArr.replace('ad','')
#     return strArr


def solution(strArr):
    answer = []
    for s in strArr:
        # s에서 "ad"를 제거한 결과가 s와 같으면, s에 "ad"가 없는 것이므로 answer에 추가합니다.
        if s.replace("ad", "") == s:
            answer.append(s)
    return answer
