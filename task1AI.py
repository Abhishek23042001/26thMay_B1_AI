s= input('Enter a string: ')                    # For eg.: 'aabbccdddeee'

b= list({i:s.count(i) for i in s}.values())   #count of individual character i.e {'a':2,'b':2,'c':2,'d':3,'e':3}

z= {i:b.count(i) for i in b}                  #count of above dict's values i.e {2:3,3:2}

[print("It's MyString") if len(z)==1 or (len(z)==2 and (max(z.keys())-min(z.keys()))<=1 and z[max(z.keys())]<=1) else print('Not Mystring')]       #output: 'Not MyString'