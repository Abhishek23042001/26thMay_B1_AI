import tkinter as tk
import csv
import operator
app = tk.Tk()
txt = 'hello'
app.title('Summary')
app.geometry('400x300')

f= open('data.csv','r')
data= list(csv.reader(f))
f.close()
cols = ['name','email','username','password','age','mobile']  #Columns Name
d = dict(zip(cols,zip(*data)))

no_of_users = len(d['name'])
avg_age = sum( list( map(lambda x: int(x),d['age']) ))/len(d['age'])
domains = list(map(lambda x:x.split('@')[1],d['email']))
domains_dict = {i:domains.count(i) for i in domains}
domains_list = sorted(domains_dict.items(), key=operator.itemgetter(1)) # Sorting based on dict values
domains_list.reverse()
domains_finaldict = dict(domains_list)

tk.Label(app,text='Summary',font= ("Arial", 15), fg='#f00').place(x=140,y=20)
tk.Label(app,text='Total Users : ',fg = '#0033cc').place(x=40,y=70)        # Display the Total no of users in a given data
tk.Label(app,text= no_of_users).place(x=120,y=70)
tk.Label(app,text='Average Age : ',fg = '#0033cc').place(x=40,y=100)
tk.Label(app,text= avg_age).place(x=120,y=100)                             # Display the average age of users in a given data
tk.Label(app,text="5 Commonly used Domain's : ",fg = '#0033cc').place(x=40,y=130)

a=120
b=160
for k,v in list(domains_finaldict.items())[0:5]: # Top 5 domain's
    tk.Label(app,text= k).place(x=a,y=b)
    tk.Label(app,text= v).place(x=a+80,y=b)
    b+=25
app.mainloop()