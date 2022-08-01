a=open("nvow.txt","w")
b=open("vow.txt","w")
c=open("sh.txt","r")

data=c.read()
n=data.split()


for i in n:
    
    if(i[0]=="A" or i[0]=="E" or i[0]=="I" or i[0]=="O" or i[0]=="U" or i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u"):
    
        b.write(i)
        b.write(" ")
   
    else:
        a.write(i)
        a.write(" ")

c.close()
a.close()
b.close()