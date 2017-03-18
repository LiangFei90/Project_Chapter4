# -*- encoding:utf-8 -*-
#findfat1.py

import tkinter
import tkinter.messagebox,tkinter.simpledialog
import os
import threading

rubbishExt=['.tmp','.TMP','.bak','.BAK','.old','.OLD','.wbk','.WBK','.xlk','.XLK','._mp','._MP',
            '.log','.LOG','.gid','.GID','.chk','.CHK','.syd','.SYD','.$$$','.@@@','.~*']
class Window():
        def __init__(self):
                self.root=tkinter.Tk()
                menu=tkinter.Menu(self.root)

                #创建‘系统’子菜单
                submenu=tkinter.Menu(menu,tearoff=0)
                submenu.add_command(label="关于...",command=self.MenuAbout)
                submenu.add_separator()
                submenu.add_command(label="退出",command=self.MenuExit)
                menu.add_cascade(label="系统",menu=submenu)

                #创建"清理" 子菜单
                submenu=tkinter.Menu(menu,tearoff=0)
                submenu.add_command(label="扫描垃圾文件",command=self.MenuScanRubbish)
                submenu.add_command(label="删除垃圾文件",command=self.MenuDelRubbish)
                menu.add_cascade(label="清理",menu=submenu)

                #创建"查找"子菜单
                submenu=tkinter.Menu(menu,tearoff=0)
                submenu.add_command(label="搜索大文件",command=self.MenuScanBigFile)
                submenu.add_separator()                                 #一条线
                submenu.add_command(label="按名称搜索文件",command=self.MenuSearchFile)
                menu.add_cascade(label="查找",menu=submenu)

                self.root.config(menu=menu)

                #创建标签，用于显示状态信息
                self.progress=tkinter.Label(self.root,anchor=tkinter.W,text='状态',bitmap='hourglass',
                            compound='left')
                self.progress.place(x=10,y=370,width=480,height=15)

                #创建文本框，显示文件列表
                self.flist=tkinter.Text(self.root)
                self.flist.place(x=10,y=10,width=480,height=350)

                #为文本框添加垂直滚动条
                self.vscroll=tkinter.Scrollbar(self.flist)
                self.vscroll.pack(side='right',fill='y')
                self.flist['yscrollcommand']=self.vscroll.set   ##scrollbar控件与text控件的绑定
                self.vscroll['command']=self.flist.yview         ##scrollbar控件与text控件的绑定

        def MainLoop(self):
                self.root.title("Findfat")
                self.root.minsize(500,400)
                self.root.maxsize(500,400)
                self.root.mainloop()
        
         #“关于”菜单
        def MenuAbout(self):
                tkinter.messagebox.showinfo("Findfat","欢迎使用")

        #“退出”菜单
        def MenuExit(self):
                self.root.quit()

        #"扫描垃圾文件"菜单
        def  MenuScanRubbish(self):
                result=tkinter.messagebox.askquestion("Findfat","GO ON SCAN?")
                if result=='no':
                        return
                tkinter.messagebox.showinfo("Findfat","Ready to SCAN")
                #self.ScanRubbish()
                self.drives=self.GetDrives()
                t=threading.Thread(target=self.ScanRubbish,args=(self.drives))
                t.start()
                
        #"删除垃圾文件"菜单
        def  MenuDelRubbish(self):
                result=tkinter.messagebox.askquestion("Findfat","GO ON DEL?")
                if result=='no':
                        return
                tkinter.messagebox.showinfo("Findfat","Ready to DEL")
                
        #"搜索大文件"菜单
        def MenuScanBigFile(self):
              s=tkinter.simpledialog.askstring('Findfat','请设置大文件的大小(M)')
              t=threading.Thread(target=self.ScanBigFile,args=(s,))
              t.start()
                                        
         #"按名称搜索文件"菜单
        def MenuSearchFile(self):
                result=tkinter.messagebox.askquestion("Findfat","GO ON SEARCH?")
                if result=='no':
                        return
                tkinter.messagebox.showinfo("Findfat","Ready to Searh")
        #遍历盘符
        def GetDrives(self):
                drives=[]
                for i in range(65,91):
                        vol=chr(i)+':/'
                        if os.path.isdir(vol):
                                drives.append(vol)
                return  tuple(drives)
                        
        
        #扫描大文件
        def ScanBigFile(self,filesize):
                total=0
                for drive in self.GetDrives():
                        for root,dirs,files in os.walk(drive):
                                for fil in files:
                                        try:
                                                fname=os.path.abspath(os.path.join(root,fil))
                                                fsize=os.path.getsize(fname)/1024/1024
                                                self.progress['text']=fname
                                                if fsize>=float(filesize):
                                                        total+=1
                                                        self.flist.insert(tkinter.END,'%s, [%.2f M ] \n' %(fname,fsize))
                                        except Exception as e:
                                                print(e)
                                                pass
                self.progress['text']="找到%s 个超过%s M 的文件"%(total,filesize)
        #扫描垃圾
        def ScanRubbish(self,scanpath):
                global rubbishExt
                total=0
                filesize=0
                for drive in scanpath:
                        for root,dirs,files in os.walk(drive):
                                try:
                                        for fil in files:
                                                filesplit=os.path.splitext(fil)                         #分离文件名与扩展名
                                                if filesplit[1]=='':
                                                        continue
                                                try:
                                                        if filesplit[1] in rubbishExt:
                                                                fname=os.path.join(os.path.abspath(root),fil)
                                                                                                                        #os.path.adspath返回path规范化的绝对路径
                                                                filesize+=os.path.getsize(fname)
                                                               # if total %20==0:
                                                                #        self.flist.delete(0.0,tkinter.END)
                                                                self.flist.insert(tkinter.END,fname+'\n')
                                                                l=len(fname)
                                                                if l>60:
                                                                        self.progress['text']=fname[:15]+'...'+fname[l-15:l]
                                                                else:
                                                                        self.progress['text']=fname
                                                                total+=1
                                                        else:
                                                                continue
                                                except ValueError :
                                                          pass
                                except Exception as e:
                                        print(e)
                                        pass
                self.progress['text']="找到 %s 个垃圾文件，共占用%.2f M磁盘空间"%(total,filesize/1024/1024)
if __name__=='__main__':
        window=Window()
        window.MainLoop()



