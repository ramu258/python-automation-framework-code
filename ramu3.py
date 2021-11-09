num=int(input("enter a number:"))
total_sum=0
step=1
condition =True
while condition :
    while num:
        total_sum += num %10
        num //= 10
    print("Step-%d Sum: %d" % (step, total_sum))
    num = total_sum
    total_sum=0
    step += 1
    condition =num>9