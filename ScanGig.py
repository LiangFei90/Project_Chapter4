import os
import threading

#def ScanBigFile(self,filesize):
##def GetDrives():
##    drives=[]
##    for i in range(65,91):
##            vol=chr(i)+':/'
##            if os.path.isdir(vol):
##                    drives.append(vol)
##    return  tuple(drives)
total=0
#for drive in GetDrives():
print ('hello')
print(os.path.getsize('C:\Windows\zh-CN\winhlp32.exe.mui'))
for root,dirs,files in os.walk("C:/"):
    for fil in files:
        try:
            fname=os.path.abspath(os.path.join(root,fil))
            fsize=os.path.getsize(fname)/1024/1024
            #self.progress['text']=fname if fsize>=1: total+=1
            if fsize>=10:
                print('%d >%s   [%.2f M] \n' %(total ,fname,fsize))
                               # self.flist.insert(tkinter.END,'%s, [%2f M ] \n' %(fname,fsize))
                total+=1       
        except Exception as e:
            print(e)
            pass
print ('共%d条文件'%total)
