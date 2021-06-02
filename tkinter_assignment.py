import tkinter as tk
app = tk.Tk()
txt = 'hello'
app.title('Registration Form')
app.geometry('400x300')
tk.Label(app,text='Full Name : ').place(x=40,y=40)
tk.Label(app,text='Email Id : ').place(x=40,y=70)
tk.Label(app,text='User Name : ').place(x=40,y=100)
tk.Label(app,text='Password : ').place(x=40,y=130)
tk.Label(app,text='Age : ').place(x=40,y=160)
tk.Label(app,text='Mobile No : ').place(x=40,y=190)

f_name = tk.Variable(app)
E_mail = tk.Variable(app)
u_name = tk.Variable(app)
pwd = tk.Variable(app)
age = tk.Variable(app)
mobile = tk.Variable(app)

tk.Entry(app,width = 30,bg='#ffffff',textvariable= f_name).place(x=150,y=40)
tk.Entry(app,width = 30,bg='#ffffff',textvariable= E_mail).place(x=150,y=70)
tk.Entry(app,width = 30,bg='#ffffff',textvariable= u_name).place(x=150,y=100)
tk.Entry(app,width = 30,bg='#ffffff',textvariable= pwd).place(x=150,y=130)
tk.Entry(app,width = 30,bg='#ffffff',textvariable= age).place(x=150,y=160)
tk.Entry(app,width = 30,bg='#ffffff',textvariable=mobile).place(x=150,y=190)
def register():
    f= open('data.csv','a')
    data = [f_name.get(),E_mail.get(),u_name.get(),pwd.get(),age.get(),mobile.get()]
    print(data)
    f.write(",".join(data)+'\n')
    f.close()
    f_name.set('')
    E_mail.set('')
    u_name.set('')
    pwd.set('')
    age.set('')
    mobile.set('')
    
tk.Button(app,text='Submit',command=register).place(x=170,y=240)

app.mainloop()
