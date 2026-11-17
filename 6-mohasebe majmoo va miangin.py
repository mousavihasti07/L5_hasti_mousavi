scores = [15, 18, 12, 20, 16, 14, 19]
total = 0
count = 0

for i in scores:
    total = total + i
    count = count + 1
    
print(f'the total is:{total}')
    
average= total/count
print(f'the average is:{average}')