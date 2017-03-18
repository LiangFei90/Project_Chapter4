import os,os.path
def traverse(pathname):
    for item in os.listdir(pathname):
        fullitem=os.path.join(pathname,item)
        #print(fullitem)
        if os.path.isdir(fullitem):
            traverse(fullitem) 
        else :
            print(fullitem)
traverse("C:\JAVA")
            
