import random
salary = []
for i in range(12):
    salary.append(random.randint(7500, 15000))
    print('Income per month', salary[i], 'UAH')
avarage = sum(salary) / len(salary)
print('Avarage income', avarage, 'UAH')