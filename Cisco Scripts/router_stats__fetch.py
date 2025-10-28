from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    'host': "192.168.68.73",
    "username": "admin",
    "password": "Pass2885!",
}

commands = [
    'show version',
    'show ip int brief',
    'show ip route',
    'show ip protocols',
]

with ConnectHandler(**device) as conn:
    for cmd in commands:
        print(f"\n=== {cmd} ===")
        output = conn.send_command(cmd)
        print(output)