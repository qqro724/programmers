#파이썬숫자만추출
#출처 https://codechacha.com/ko/python-extract-integers-from-string/

import re 

def solution(my_string):
    # 정규표현식으로 숫자만 남긴 문자열을 만듭니다.
    numbers_str = re.sub(r'[^0-9]', '', my_string)
    # 각 숫자 문자들을 정수로 변환하여 리스트로 만듭니다.
    numbers_list = list(map(int, numbers_str))
    # 리스트를 오름차순으로 정렬합니다.
    numbers_list.sort()
    
    return numbers_list