import os
import subprocess

service_name = 'remove-admin'

path = f'/etc/systemd/system/{service_name}.service'

directory = os.getcwd()

code = f"""
[Unit]
Description=RemoveAdminBot

[Service]
WorkingDirectory = {directory}
ExecStart=/usr/bin/python3  {directory}/main.py
 
[Install]
WantedBy=multi-user.target
"""

with open(path, 'w') as file:
    file.write(code)

print('The service is installed. Launching...')
subprocess.run(f'systemctl enable {service_name}',shell=True)
subprocess.run(f'systemctl start {service_name}',shell=True)
print('Service is running')