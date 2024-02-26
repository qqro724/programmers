# def solution(num_list):
#     product = 1
#     sum_of_elements = 0
    
#     for num in num_list:
#         product *= num
#         sum_of_elements += num
    
#     if product < sum_of_elements ** 2:
#         return 1
#     else:
#         return 0
    
def solution(num_list):
#모든 원소들을 곱하기 위한 초기값
    product = 1
#모든 원소들을 더하기 위한 초기값
    sum_of_elements = 0

#모든 곱
    for num in num_list:
        product *= num
        sum_of_elements += num
#모든 원소들의 합의 제곱
    if product < sum_of_elements ** 2:
        return 1
    else:
        return 0