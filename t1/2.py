A = {}
B = {}
C = {}
D = {}
F = {}
for std in range(10):
    name = input('Enter the students name')
    score = int(input('Enter the students score'))
    if 80 <= score <= 100:
        A.update({name: score})
    elif 70 <= score <= 79:
        B.update({name: score})
    elif 60 <= score <= 69:
        C.update({name: score})
    elif 50 <= score <= 59:
        D.update({name: score})
    elif 0 <= score <= 49:
        F.update({name: score})


print(f'The scores of A -----> {A}')
print(f'The scores of B -----> {B}')
print(f'The scores of C -----> {C}')
print(f'The scores of D -----> {D}')
print(f'The scores of F -----> {F}')