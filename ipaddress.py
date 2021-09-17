import requests, socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
local_ip_address = s.getsockname()[0]

external_ip_address = requests.get('https://httpbin.org/ip')
external_ip_address = '{0}'.format(external_ip_address.json()['origin'])

print(f'\nYour Private IPv4 Address is {local_ip_address}')

print(f'\nYour Public IPv4 Address is {external_ip_address}')

input("\nPress ENTER to continue:")