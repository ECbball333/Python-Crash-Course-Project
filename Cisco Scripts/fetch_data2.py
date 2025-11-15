from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.68.61',
    'username': 'admin',
    'password': "",
}

commands = [
    'show version',
    'show ip int brief',
    'show ip route',
    'show ip protocols',
    'ping 8.8.8.8'
]

with ConnectHandler(**device) as conn:
    for cmd in commands:
        print(f"\n=== {cmd} ===")
        output = conn.send_command(cmd)
        print(output)