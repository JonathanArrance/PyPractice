import requests

response = requests.get('http://127.0.0.1:9000/demo/test1')

print(response.text)
print(response.content)


print('Post test')

response2 = requests.post('http://127.0.0.1:9000/demo/test1', data={'demo', 'This is a post demo'})

print(response2.text)
print(response2.content)