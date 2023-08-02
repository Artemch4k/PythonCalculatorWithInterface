from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry('400x400')

def request(symbol):
    enter.insert(END, symbol)

def clear_everything():
    enter.delete(0,END)

def equals():
    texT = enter.get()
    result = 0
    if '+' in texT:
        splitted = texT.split('+')
        first = float(splitted[0])
        second = float(splitted[1])
        result = first+second
    if '*' in texT:
        splitted = texT.split('*')
        first = float(splitted[0])
        second = float(splitted[1])
        result = first*second
    if '-' in texT:
        splitted = texT.split('-')
        first = float(splitted[0])
        second = float(splitted[1])
        result = first - second
    if '/' in texT:
        splitted = texT.split('/')
        first = float(splitted[0])
        second = float(splitted[1])
        if second == 0.0:
            result = 'Error!'
        else:
            result = first / second
    clear_everything()
    enter.insert(0, result)


enter = Entry(window, width=10,font= ('', 60))
enter.place(x=0, y=0)

button1 = Button(window, bg='black', fg='white',text='1',command=lambda: request('1'))
button1.place(x=0, y=95, width=55,height=50)

button2 = Button(window, bg='black', fg='white',text='2',command=lambda: request('2'))
button2.place(x=50,y=95,width=55,height=50)

button3 = Button(window, bg='black', fg='white',text='3',command=lambda: request('3'))
button3.place(x=100,y=95,width=55,height=50)

button4 = Button(window, bg='black',fg='white', text='4',command=lambda: request('4'))
button4.place(x=0,y=144,width=50,height=50)

button5 = Button(window, bg='black',fg='white', text='5',command=lambda: request('5'))
button5.place(x=50,y=144,width=50,height=50)

button6 = Button(window, bg='black',fg='white', text='6',command=lambda: request('6'))
button6.place(x=100,y=144,width=55,height=50)

button7 = Button(window, bg='black',fg='white', text='7',command=lambda: request('7'))
button7.place(x=0,y=193,width=50,height=50)

button8 = Button(window, bg='black',fg='white', text='8',command=lambda: request('8'))
button8.place(x=50,y=193,width=50,height=50)

button9 = Button(window, bg='black',fg='white', text='9',command=lambda: request('9'))
button9.place(x=100,y=193,width=55,height=50)

button0 = Button(window, bg='black',fg='white', text='0',command=lambda: request('0'))
button0.place(x=0,y=242,width=50,height=50)

button_plus = Button(window, bg='black',fg='white', text='+',command=lambda: request('+'))
button_plus.place(x=154, y=95,width=250,height=50)

button_plus = Button(window, bg='black',fg='white', text='-',command=lambda: request('-'))
button_plus.place(x=154, y=144,width=250,height=50)

button_plus = Button(window, bg='black',fg='white', text='*',command=lambda: request('*'))
button_plus.place(x=154, y=193,width=250,height=50)

button_plus = Button(window, bg='black',fg='white', text='/',command=lambda: request('/'))
button_plus.place(x=154, y=242,width=250,height=50)

button_clear = Button(window, bg='black',fg='white', text='CE',command=lambda: clear_everything())
button_clear.place(x=50, y=242,width=50,height=50)

button_equals = Button(window, bg='black',fg='white', text='=',command=lambda: equals())
button_equals.place(x=100, y=242,width=54,height=50)

button_by = Button(window, bg='black',fg='white', text='Made by Artemch4k')
button_by.place(x=0, y=291,width=400,height=110)


window.mainloop()

# END OF THE PROGRAM