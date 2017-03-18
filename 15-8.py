import subprocess

'''f=open('protest9.py')
print(f.readlines(1))'''

processes=[]
psum=5
for i in range(psum):
    processes.append(subprocess.Popen(['protest9.py'],
                                    stdout=subprocess.PIPE,
                                    stdin=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True,
                                    shell=True))
                                  
'''pro=subprocess.Popen(['protest9.py'],
                    stdout=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True,
                    shell=True)'''
#print(processes[0])
processes[0].communicate('0 bouqunt of flowers')
#print(processes[0].communicate()[0]+'00000')

for before,after in zip(processes[:psum],processes[1:]):
    after.communicate(before.communicate()[0])

print(processes[:psum])
print(processes[1:])
print(zip(processes[:psum],processes[1:]))
print(before.communicate()[0])
print(after.communicate(before.communicate()[0]))
'''
print('\n Sum of Process:%d' %psum)

print(processes[0].pid)
print('')
for item in processes:
    print(item.communicate()[0])
    '''
