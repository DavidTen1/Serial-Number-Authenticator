import os
import subprocess
import hashlib

serialNumberCommand = 'wmic bios get serialnumber'

#1st row shows "Serial Number", 2nd row shows the actual value
serialNumberOutput = str(subprocess.check_output(serialNumberCommand, shell=True)).split('\\n')

# 2nd row has serial num, some space and few \r signs, by splitting, only the value gets extracted
print('serial num', str(serialNumberOutput[1]).split(' ')[0])
