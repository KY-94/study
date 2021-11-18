#max와 min을 사용하지않고 최대 최소 구하기
list_a = [52,273,103,32,57]

#최소값 구하기
out = 10000000
for i in list_a:
    if i<out:
        out=i
print(out)


#최대값 구하기
output = -10000000
for j in list_a:
    if j>output:
        output=j
print(output)

#최소값 구하기
for k in list_a:
        if k>list_a[0]:
                k=list_a[0]
        if k>list_a[1]:
                k=list_a[1]
        if k>list_a[2]:
                k=list_a[2]
        if k>list_a[3]:
                k=list_a[3]
        if k>list_a[4]:
                k=list_a[4]
print(k)

#최대값 구하기
for m in list_a:
        if m<list_a[0]:
                m=list_a[0]
        if m<list_a[1]:
                m=list_a[1]
        if m<list_a[2]:
                m=list_a[2]
        if m<list_a[3]:
                m=list_a[3]
        if m<list_a[4]:
                m=list_a[4]
print()