n = int(input())  # 첫째줄 입력
peoples = list(map(int, input().split()))  

peoples.sort()  
answer = 0 

for x in range(1, n+1):
    answer += sum(peoples[0:x])  
print(answer) 