students = [
("Ali", 22, 18),
("Sara", 20, 15),
("Reza", 23, 9),
("Mina", 21, 20),
("Nima", 19, 12),
("Amir", 24, 7)
]

total_score= 0
rejected_list= []

for name,age,score in students:
    print(f'name:{name}, age:{age}, score:{score}')
    total_score= total_score + score
    if score < 10:
        rejected_list.append(name)
print(f'{rejected_list}, your scores are less than 10.')

high_score= 0
for name,age,score in students:        
    if score > high_score:
        high_score = score
        top_name = name
print(f'{top_name}, you have highest score.')

average = total_score / len(students)
print(f'average number is:{average}')

good_score= []
for name,age,score in students:
    if score > average:
        good_score.append(name)
print(good_score,'your scores are more than average.')
    


