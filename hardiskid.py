# import os
# data = os.popen('vol '+'c:', 'r').read()
# data = data.split()
# print(data[len(data)-1:])
import subprocess
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
print(current_machine_id)