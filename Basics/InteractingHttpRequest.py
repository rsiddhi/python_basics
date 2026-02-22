import requests
import webbrowser

r = requests.get('https://facebook.com')

print(r.status_code)
print(r.headers)
print(r.headers['Content-Type'])

# get request
payload = {'username': 'admin', 'password': 'password'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)

#post request
payload = {'username': 'admin', 'password': 'password'}
r = requests.post('https://httpbin.org/post', params=payload)
print(r.text)

# handle websites re-directions
r = requests.get('https://www.github.com')
print(r.status_code) #200

r = requests.get('https://www.github.com', allow_redirects=False)
print(r.status_code) #301
