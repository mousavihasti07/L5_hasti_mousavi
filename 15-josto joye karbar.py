users = [
(1, "ali", "active"),
(2, "sara", "inactive"),
(3, "reza", "active"),
(4, "mina", "inactive"),
(5, "nima", "active")
]

user_name= input('your name?:').strip().lower()

for ID,name,status in users:
    if user_name in name:
        print(f'ID: {ID} , status: {status}')
        break
if not user_name in name:
     print('not found.')
        

