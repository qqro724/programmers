# def solution(my_string, num1, num2):
#     answer = ''
    
#     str_list = list(my_string)
    
#     str_list[num1],str_list[num2] == str_list[num2],str_list[num1]  
    
    
#     return ''.join(str_list)



def solution(my_string, num1, num2):
    str_list = list(my_string)  # 문자열을 리스트로 변환

    # 두 문자의 위치를 바꾸기
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]

    return ''.join(str_list)  # 리스트를 다시 문자열로 변환해서 반환
