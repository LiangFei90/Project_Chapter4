import tkinter
import tkinter.messagebox
import os

rubbishExt=['.tmp','.TMP','.bak','.BAK','.old','.OLD','.wbk','.WBK','.xlk','.XLK','._mp','._MP',
            '.log','.LOG','.gid','.GID','.chk','.CHK','.syd','.SYD','.$$$','.@@@','.~*']
#global rubbishExt
total=0
filesize=0

drives=[]

for i in range(65,91):
    vol=chr(i)+':/'
    print (vol)
    if os.path.isdir(vol):
        print(vol)
        dirves.append(vol)
tuple(drives)

for drive in drives:
    print ('1')
    for root,dirs,files in os.walk(drive):
          #  try:
        for fil in files:
            filesplit=os.path.splitext(fil)                         #分离文件名与扩展名
            if filesplit[1]=='':
                continue
            #print(os.path.join(os.path.abspath(root),fil))
            #print(filesplit[1])
            # print(rubbishExt.index(filesplit[1]))
            # try:
            #print(rubbishExt.index('.txt'))
            try:
                if filesplit[1] in rubbishExt:
                    fname=os.path.join(os.path.abspath(root),fil)
                                                                            #os.path.adspath返回path规范化的绝对路径
                    filesize+=os.path.getsize(fname)
                    #if total %20==0:
                    #        self.flist.delete(0.0,tkinter.END)
                    #self.flist.insert(tkinter.END,fname+'\n')
                    l=len(fname)
                    if l>60:
                        outname=fname[:30]+'...'+fname[l-30:l]
                    else:
                        outname=fname
                    print(outname)
                    total+=1
                else :
                    continue
            except Exception as e:
                print(e)
                pass
    ##                        except ValueError :
    ##                                  pass
    ##                       except Exception as e:
    ##                print(e)
    ##                pass
print("共有 %s 条记录,共占用%2.fM磁盘空间" %(total ,filesize/1024/1024))
