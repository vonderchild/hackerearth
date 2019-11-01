"""

Rahul is a very busy persion he dont wan't to waste his time . He keeps account of duration of each and every work. Now he don't even get time to calculate duration of works, So your job is to count the durations for each work and give it to rahul.

Input:

First line will be given by N number of works
Next N line will be given SH,SM,EH and EM  each separated by space(SH=starting hr, SM=starting min, EH=ending hr, EM=ending min)

Output:

N lines with duration HH MM(hours and minutes separated by space)

SAMPLE INPUT
2
1 44 2 14
2 42 8 23

SAMPLE OUTPUT
0 30
5 41

"""

n = int(input())
for i in range(n):
    sh, sm, eh, em = (int(x) for x in input().split())
    m = em - sm
    h = eh - sh
    if m < 0:
        h -= 1
        m += 60

    print(h, m)
