import requests

status = 'available'

res = requests.get(f'https://reqres.in/api/users?page=2?status{status}', headers={'accept':'application/json'})
print('Запрос Get')
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.post(f'https://reqres.in/api/users?status{status}', headers={'accept':'application/json'})
print('Запрос Post')
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.put(f'https://reqres.in/api/users/2?status{status}', headers={'accept':'application/json'})
print('Запрос Put')
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.delete(f'https://reqres.in/api/users/2?status{status}', headers={'accept':'application/json'})
print('Запрос Delete')
print(res.status_code)
print(res.text)

