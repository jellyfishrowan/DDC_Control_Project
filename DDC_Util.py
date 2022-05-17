# start with [$ sudo apt install ddcutil]
import ddcutil
import subprocess
ddc_Detect = subprocess.Popen(['ddcutil', 'detect'], stdout=PIPE)
ddc_Detect_Output = ddc_Detect.communicate()
subprocess.run(['ddcutil', 'setVCS?', '0x10', '80'], shell=True)