person = {
    'first_name': 'Ehsan',
    'last_name': 'Hosseini',
    'age': 250,
    'country': 'iran',
    'is_marred': True,
    'skills': ['JavaScript', 'Django', 'Odoo', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'postal_code': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f'first index ---> {skills[0]}')
    print(f'middle index ---> {skills[middle_index]}')
    print(f'last index ----> {skills[-1]}')

    if 'Python' in skills:
        print('The person has Python skills')
    else:
        print('The person does not have Python skills')


def marital_state(state):
    if state:
        return 'married'
    else:
        return 'single'


print(
    f"{person['first_name']}  {person['last_name']} Lives in {person['country']} he is {marital_state(person['is_marred'])}"
    f" he has these skills: {person['skills']}")
