line1=[1,2,3,4]
line2=[5,6,7,8]
line3=[9,0,1,4]
lines = [line1, line2, line3]

def clear_list(list):
    list.clear()
    

list(map(clear_list,lines))
print (line1)
print (line2)
print (line3)




