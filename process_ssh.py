
import subprocess
ssh_host = "root@10.248.70.118" #test using US1I-ERPCPRP01
args = 'varnishadm -n default backend.list | grep DapsGateway'
process = subprocess.Popen(['ssh', ssh_host, args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()
process.wait()
print "##################### output"
print output
print "##################### error"
print error
