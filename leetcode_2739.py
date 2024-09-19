mainTank = 5
additionalTank = 10
distance=0
if mainTank<5:
    print(mainTank*10)
    exit()
else:
    while mainTank>=5 and additionalTank!=0:
        mainTank-=5
        distance+=60
        additionalTank-=1
print(distance)