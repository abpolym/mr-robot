import time
from random import randint

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# Therapist, Ollie_Parker, Boyfriend_Therapist
passwords = ['Dylan_2791', '123456seven', 'No match found']
keywords = ['Dylan; June 3rd, Stonehendge', '1984; 8D; Sa???', '2C;Yankees;Flipper']
listcounts = [42808, 9875894, 9875894]
possibilities = [8768028, 9875894, 9875894]
prompt = bcolors.OKBLUE + 'root@elliot:' + bcolors.ENDC + ' '
pos = randint(0,len(passwords)-1)
start_time = time.time()
print prompt + 'ping (222.12.154.102)'
print prompt + 'ping (222.12.154.102) 56(84) bytes of data'
print prompt + '64 bytes ev.e-bnk.org (222.12.154.102): icmp_req=1 ttl=11'
time.sleep(1.25)
print prompt + '1 packets transmitted, 1 received, 0% packet loss, time 0.'
print prompt + 'elpscrk -list pswList.list-add ' + keywords[pos]
print prompt + 'elpscrk  -ip 222.12.154.102 -usr mich05654 -psw pswList.list'
print prompt + 'List Count: '+str(listcounts[pos])+' Type: alphanum'
for i in range(0, possibilities[pos], 13):
	print prompt + 'Scanning word ' + str(i) + ' of ' + str(possibilities[pos]) + '\r',
print '                                                                \r',
print prompt + 'Scanning complete'
print prompt + 'Time elapsed: ' + str(time.time() - start_time)
print prompt + 'Password: ' + passwords[pos]
# Quick git sign test
# Quick blinking commit test
