devices = [
    {"hostname": "PE1", "mgmt_ip": "192.168.68.220", "role": "PE", "os_version": "17.13.1"},
    {"hostname": "DC-CORE1", "mgmt_ip": "10.10.10.11", "role": "core", "os_version": "17.12.1"},
    {"hostname": "DIST-1", "mgmt_ip": "10.20.20.11", "role": "dist", "os_version": "17.12.1"},
    # ...
]

for d in devices:
    if d["os_version"] != "17.13.1":
        print(d["hostname"], d["mgmt_ip"], "needs upgrade")