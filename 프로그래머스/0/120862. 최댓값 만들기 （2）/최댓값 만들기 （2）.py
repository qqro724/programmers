# def solution(numbers):
#     answer = 0
    
#     numbers=[]
    
#     numbers_1 = sorted(numbers)
    
#     for i in numbers:
#         numbers[0]*numbers[1]
        
    
#     return answer


# def solution(numbers):
#     numbers.sort()  # numbers를 오름차순 정렬

#     # 경우 1: 가장 큰 두 개의 숫자 곱하기
#     max1 = numbers[-1] * numbers[-2]

#     # 경우 2: 가장 작은 두 개의 숫자 곱하기 (음수일 때 더 클 수도 있음)
#     max2 = numbers[0] * numbers[1]

#     return max(max1, max2)  # 두 개 중 더 큰 값을 반환



def solution(numbers):
    numbers.sort()
    
    max1=numbers[-1]*numbers[-2]
    
    #음수일때 더 클수가 있음?
    max2=numbers[0]*numbers[1]
    
    return max(max1,max2)