H, M = map(int, input().split())
Add_M = int(input())

H += (M + Add_M) // 60
new_M = (M + Add_M) % 60
new_H = H % 24

print(new_H, new_M)
