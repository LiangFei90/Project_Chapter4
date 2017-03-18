# -*- encoding:utf-8 -*-
#findfat1.py

import tkinter
import tkinter.messagebox

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
                
        #"删除垃圾文件"菜单
        def  MenuDelRubbish(self):
                result=tkinter.messagebox.askquestion("Findfat","GO ON DEL?")
                if result=='no':
                        return
                tkinter.messagebox.showinfo("Findfat","Ready to DEL")
                
        #"搜索大文件"菜单
        def MenuScanBigFile(self):
                result=tkinter.messagebox.askquestion("Findfat","GO ON SCAN BIG FILES?")
                if result=='no':
                        return
                tkinter.messagebox.showinfo("Findfat","Ready to Scan Big Files")

         #"按名称搜索文件"菜单
        def MenuSearchFile(self):
                result=tkinter.messagebox.askquestion("Findfat","GO ON SEARCH?")
                if result=='no':
                        return
                tkinter.messagebox.showinfo("Findfat","Ready to Searh")
if __name__=='__main__':
        window=Window()
        window.MainLoop()



