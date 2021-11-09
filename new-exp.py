from tkinter import * 
from tkinter import messagebox
from tkinter import font
from tkinter.font import BOLD
from email_demo import *
from dbcommands import *
from fnc import *
from libgen import *



#ROOT WINDOW PROPERTIES
root = Tk()
root.geometry("1200x600")
root.title("Login Page")


#FUNCTIONS AND WIDGETS FOR BACKGROUND 

list1 = ['00']
list2 = ['7c']

def add_one(s):
	s1 = ""
	if(s == '9f'):
		return 'a0'
	elif(s == 'ff'):
		return '00'
	elif(s[-1] == 'f'):
		c0 = str(chr(ord(s[0]) + 1))
		c1 = '0'
		s1 = c0 + c1

	elif(s[-1] == '9'):
		c0 = s[0]
		c1 = 'a'
		return f'{c0}{c1}'
	else:
		c0 = s[0]
		c1 = str(chr(ord(s[1]) + 1))
		s1 = c0+c1

	return s1

for i in range (1 ,90):
	list1.append(str(add_one(list1[i-1])))
	list2.append(str(add_one(list2[i-1])))

#SETTING BG
for i in range(90):
 
	frame = LabelFrame(root , bg = '#'+list1[89-i] + 'ff' + list2[i] , bd = 0 ,width = 40 , height = 100)
	frame.grid( row = 0 ,column 	= i , sticky = 'news' , columnspan = 20 )
	root.columnconfigure(i , weight = 1)
	


#MAINFRAME (LOGIN WINDOW)
main = LabelFrame(root , width = 100 , height = 200 , bd = 0)
print("line60")


#FUNCTIONS FOR PRESSED BUTTONS

def submit(event):
	#print('submitted' , user_entry.get() , pass_entry.get())
    curr_user = user_entry.get().strip()
    curr_pass = pass_entry.get()
    print(curr_user,curr_pass)

    info = user_details(curr_user)
    print(info)

    if(info is None):
        print('NO USER RECORD IN DATABASE')
        choice = messagebox.askquestion('Username invalid' , 'Username not found\nClick on Create new account')
        if choice == 'yes':
            create_acc_fxn()


        user_entry.delete(0,END)
        pass_entry.delete(0,END)

    elif(info[0] == curr_user and info[1] == curr_pass):
        # 
        main.destroy()
        root.destroy()
        
        NewRoot = Tk()
        SF = createSearch(NewRoot)
        SF.place(relx = .1 , rely = .05 , relheight = 0.35 , relwidth = 0.8)
        NewRoot.geometry("1000x700+100+30")
        NewRoot.configure(bg="#fa3")
        NewRoot.title("Book Fetcher Project")


        RES = createResult(NewRoot)
        RES.place(relx = .1 , rely = 0.45 , relwidth = 0.8 , relheight = 0.45)
        # RES.pack()

       
       
        print('user verified')
        # root.title('USER VERIFIED')
    else:
        print('incorrect password')
        messagebox.showerror('ERROR!!!' , 'Wrong Username password combo' , parent = main )
        user_entry.delete(0,END)
        pass_entry.delete(0,END)

    

def forgotpass():
	
	def setNewPass(uid , mail , pass1 , pass2):
		if pass1 == pass2:
			set_pass(uid , mail,pass1)
			forgot_frame.destroy()
		else:
			messagebox.showinfo('Warning' , 'Both passwords fields dont match')


	def confirm():
		
		print('confirm')
		
		
		curr = ff_e1.get()
		ff_e1.delete(0,END)

		send = messagebox.askquestion("Confirm" , f'Are you sure your mail is {curr}')
		if send == 'yes':
			
			ans = user_check_mail(curr)
			print(ans)

			if ans:
				new_otp = otp_email(ans)

				update_otp(curr , new_otp)
				
				# items = [reg_mail_entry , reg_email ]
				# for item in items:
				# 	item.destroy()

				ff_l1.config(text='Enter OTP')
				ff_l1.place(relx = 0.05 , rely = 0.2 , relheight= 0.15 , relwidth=0.4)
				ff_e1.place(relx = 0.55 , relwidth=0.35 , rely = 0.2 , relheight=0.15 )
				ff_b1.config(text='Verify OTP' , command=lambda : checkWithDb(ans[2] , ff_e1.get()) )
				ff_cancel.place(relx = 0.6 , rely = 0.65 , relwidth=0.2 , relheight=0.2)
				
			else:
				messagebox.showerror('Error' , 'Cannot find required email')
				ff_e1.delete(0,END)

	print('here')
	forgot_frame = LabelFrame(root , bd = 0)


	def checkWithDb(email , otp):
		
		info = reset_details(email)
		data = user_check_mail(email)

		print(info)	
		if(info[1] == otp):
			
			ff_l1.config(text='Enter new password')
			ff_e1.delete(0,END)

			ff_l2 = Label(forgot_frame ,text='Re-enter Password',bg = '#ff68df' , relief = GROOVE)

			ff_l1.place(relx=0.05 , rely = 0.2 , relwidth=0.35 ,relheight=0.15)
			ff_e1.place(relx=0.5 , rely = 0.2 , relwidth=0.4 , relheight=0.15)
			
			ff_l2.place(relx = 0.05 , rely = 0.45 , relwidth=0.35 , relheight= 0.15)
			ff_e2.place(relx=0.5 , rely = 0.45 ,relwidth=0.4 , relheight=0.15)

			ff_b1.config(text='Change' , command=lambda:setNewPass(data[0],email,ff_e1.get() , ff_e2.get()))
			ff_b1.place(relx=0.1 ,rely = 0.7 , relwidth=0.3 , relheight=0.2 )
			ff_cancel.place(relx = 0.6 , rely = 0.7 , relwidth=0.2 , relheight=0.2)
			


		else:
			messagebox.showerror('Error' , 'INCORRECT OTP ENTERED')
			ff_e1.delete(0,END)



	def cancelFrame():
		forgot_frame.destroy()
	
	##BACKGROUND FOR FORGOT FRAME
	for i in range(100):
		grad = LabelFrame(forgot_frame , bg = '#ff'+ li1[i] + li2[99-i] , bd = 0, width =5 , height = 50)
		grad.place(relwidth = 0.01005 , relheight = 1 , relx = (0 + (i*0.01)))
		forgot_frame.columnconfigure(i , weight = 1)

	#LABELS FOR FORGOT FRAME
	ff_l1 = Label(forgot_frame , text='Your registered Email' , font=('courier') ,bg = '#ff68df' , relief = GROOVE)
	ff_e1 = Entry(forgot_frame)
	ff_b1 = Button(forgot_frame , text = 'Send OTP' , command=confirm,bg='#03ccbd' , fg='black',relief = GROOVE)
	ff_cancel = Button(forgot_frame , text = 'Cancel ' , bg='#03ccbd' , fg='black',relief = GROOVE , command=cancelFrame )
	ff_l2 = Label(forgot_frame)
	ff_e2 = Entry(forgot_frame)

	ff_l1.place(relx = 0.05 , rely = 0.2 , relheight= 0.15 , relwidth=0.4)
	ff_e1.place(relx = 0.55 , relwidth=0.35 , rely = 0.2 , relheight=0.15 )
	ff_b1.place(relx = 0.15 , rely = 0.65 , relwidth=0.4 , relheight=0.2)
	ff_cancel.place(relx = 0.6 , rely = 0.65 , relwidth=0.2 , relheight=0.2)


	#PUSHING FRAME ONTO SCREEN
	forgot_frame.place( relx = 0.4 , rely = 0.4 ,relheight = 0.4 , relwidth = 0.375 )


	#FORGOTPASS FRAME BINDINGS
	def resize2(e):
		if(ff_l1.cget('text') == 'Your registered Email') :
			ff_l1.config(font=('courier' , int(e.width/47) , 'bold'))
			ff_b1.config(font=('courier' , int(e.width/20)))
			ff_e1.config(font=('courier' , int(e.width/35)))
			ff_e2.config(font=('courier' , int(e.width/35)))
			ff_cancel.config(font=('courier' , int(e.width/30) , BOLD))
		
		if(ff_l1.cget('text') == 'Verify OTP'):
			ff_l1.config(font=('courier' , int(e.width/42) , 'bold'))
			ff_b1.config(font=('courier' , int(e.width/22)))
			ff_cancel.config(font=('courier' , int(e.width/31) , BOLD))
		
		if(ff_l1.cget('text') == 'Enter new password'):
			ff_l1.config(font=('courier' , int(e.width/47) , 'bold'))
			ff_b1.config(font=('courier' , int(e.width/47)))
			ff_cancel.config(font=('courier' , int(e.width/30) , BOLD))
			ff_e1.config(font=('courier' , int(e.width/35)))
			ff_e2.config(font=('courier' , int(e.width/35)))
			ff_l2.config(font=('courier' , int(e.width/47) , 'bold'))



	relief_widget(ff_b1 , '#03ccbd' , 'black')
	relief_widget(ff_cancel , '#03ccbd' , 'black')
	forgot_frame.bind('<Configure>' , resize2)



def create_acc_fxn():
	AccFrame = LabelFrame(root , bd = 0)
	

	def finalStep(verify_mail , uid , email , pass1):

				if(af_e1.get() == verify_mail):
					insert_user(uid,pass1,email)
					print('DONEEEEEEEEEE')
					AccFrame.destroy()	
				else:
					messagebox.showerror('incorrect otp' , 'The OTP you entered is incorrect')


	def validate(uid , email , pass1 , pass2):
		items = [uid , email,pass1 , pass2]
		l = [len(i)  for i in items]
		l.sort()

		if pass1.strip() != pass2.strip():
			messagebox.showerror('ERROR' , 'Password fields do not match')
			af_e3.delete(0,END)
			af_e4.delete(0,END)

		elif user_check_mail(email):
			messagebox.showinfo('ERROR' , 'Email already registered')
		elif user_details(uid):
			messagebox.showinfo('ERROR' , 'USERNAME already taken by another user')
		elif l[-1] == 0:
			messagebox.showerror('ERROR' , 'Some input field is empty')

		else:
			
			verify_mail = otp_email((uid , pass1,email) , 6)
			if(verify_mail == '!'*6):
				messagebox.showerror('ERROR' , 'INVALID EMAIL PROVIDED')
				af_e2.delete(0,END)
				return

			af_l2.place_forget()
			af_l3.place_forget()
			af_l4.place_forget()
			af_e2.place_forget()
			af_e3.place_forget()
			af_e4.place_forget()

			af_e1.delete(0,END)
			
			#messagebox.showinfo('info','Please verify your email by entering otp sent to your mail')


			af_l1.config(text="Verify Your mail\nby entering OTP" ,font=('courier',12))
			af_e1.place(relx=0.55 , rely=0.35 , relwidth=0.4 , relheight=0.17)
			af_l1.place(relx=0.05 , rely = 0.2 , relwidth=0.4 , relheight= 0.4)
			af_b1.config(text='Verify mail' , command=lambda:finalStep(verify_mail,uid,pass1,email))
			af_b1.place(relx=0.05,rely=0.85,relwidth=0.4,relheight=0.1)
			
			
	
	def cancelAcc():
		AccFrame.destroy()
		return


	for i in range(100):
		grad = LabelFrame(AccFrame , bg = '#ff'+ li1[i] + li2[99-i] , bd = 0, width =5 , height = 50)
		grad.place(relwidth = 0.01005 , relheight = 1 , relx = (0 + (i*0.01)))
		AccFrame.columnconfigure(i , weight = 1)

	af_l1=Label(AccFrame,text='Username',bg = '#ff68df' , relief = GROOVE)
	af_l2=Label(AccFrame,text='Email',bg = '#ff68df' , relief = GROOVE)
	af_l3=Label(AccFrame,text='Password',bg = '#ff68df' , relief = GROOVE)
	af_l4=Label(AccFrame,text='Re-Enter pass',bg = '#ff68df' , relief = GROOVE)

	af_e1=Entry(AccFrame)
	af_e2=Entry(AccFrame)
	af_e3=Entry(AccFrame)
	af_e4=Entry(AccFrame)

	af_b1 = Button(AccFrame,text='Create Account',bg = '#03ccbd' , relief = GROOVE , 
	command=lambda:validate(af_e1.get() , af_e2.get(),af_e3.get(),af_e4.get()))
	af_b2 = Button(AccFrame,text='Cancel' , bg='#03ccbd',relief= GROOVE,command=cancelAcc)


	af_l1.place(relx=0.05 , rely=0.05 , relheight=0.12 , relwidth=0.3)
	af_l2.place(relx=0.05 , rely=0.25 , relheight=0.12 , relwidth=0.3)
	af_l3.place(relx=0.05 , rely=0.45 , relheight=0.12 , relwidth=0.3) 
	af_l4.place(relx=0.05 , rely=0.65 , relheight=0.12 , relwidth=0.3)

	af_e1.place(relx=0.5 , rely=0.05 , relheight=0.12 , relwidth=0.4) 
	af_e2.place(relx=0.5 , rely=0.25 , relheight=0.12 , relwidth=0.4)
	af_e3.place(relx=0.5 , rely=0.45 , relheight=0.12 , relwidth=0.4)
	af_e4.place(relx=0.5 , rely=0.65 , relheight=0.12 , relwidth=0.4) 

	af_b1.place(relx=0.15,rely=0.85,relwidth=0.3,relheight=0.1)
	af_b2.place(relx=0.6,rely=0.85,relwidth=0.3,relheight=0.1)
	
	
	
	

	def resize3(e):
		if af_l1.cget('text') == 'Username':
			af_l1.config(font=('courier',int(e.width / 25) , 'bold'))
			af_l2.config(font=('courier',int(e.width / 25) , 'bold'))
			af_l3.config(font=('courier',int(e.width / 25) , 'bold'))
			af_l4.config(font=('courier',int(e.width / 37) , 'bold'))

			af_e1.config(font=('courier',int(e.width / 28) ))
			af_e2.config(font=('courier',int(e.width / 28)))
			af_e3.config(font=('courier',int(e.width / 28)))
			af_e4.config(font=('courier',int(e.width / 28)))

			af_b1.config(font=('courier',int(e.width / 38) , 'bold'))
			af_b2.config(font=('courier',int(e.width / 20) , 'bold'))

		if af_b1.cget('text') == 'Verify mail':
			af_b1.config(font=('courier',int(e.width / 30) , 'bold')) 




	AccFrame.place( relx = 0.4 , rely = 0.2 ,relheight = 0.7 , relwidth = 0.375)
	AccFrame.bind('<Configure>',resize3)
	relief_widget(af_b1,'#03ccbd','black')
	relief_widget(af_b2,'#03ccbd','black')





#BINDING FUNCTIONS
def hover_widget(widget , bcolor , fcolor):
	def hovering(a):
		widget['background'] = fcolor
		widget['foreground'] = bcolor

	def not_hovering(a):
		widget['background'] = bcolor
		widget['foreground'] = fcolor
	
	widget.bind('<Enter>' , hovering)
	widget.bind("<Leave>" , not_hovering)

def relief_widget(widget , bg , fg ):
	def widget_hover(e):
		widget.config(highlightbackground = 'black' , highlightthickness = 3 , relief = RAISED)

	def widget_NOThover(e):
		widget.config(bg=bg , fg=fg , relief = GROOVE)

	widget.bind('<Enter>' , widget_hover)
	widget.bind('<Leave>' , widget_NOThover)




#SETTING BG FOR LOGIN PANEL
li1 = ['00']
li2 = ['95']

for i in range(1,110):
	li1.append(add_one(li1[i-1]))
	li2.append(add_one(li2[i-1]))


for i in range(100):
	
	grad = LabelFrame(main , bg = '#ff'+ li1[i] + li2[99-i] , bd = 0, width =5 , height = 50)
	grad.place(relwidth = 0.01005 , relheight = 1 , relx = (0 + (i*0.01)))
	main.columnconfigure(i , weight = 1)

#SELF EXPANDING FRAMES
main.rowconfigure(0 , weight = 1)


#WIDGETS FOR MAIN FRAME
user_label = Label(main , text = 'User Name' , font=('courier') ,  bg='#03ccbd' , fg='black')
user_entry = Entry(main ,bg='#03ccbd' , fg='black')

pass_label = Label(main , text = 'Password', font=('courier'),  bg='#03ccbd' , fg='black' )
pass_entry = Entry(main ,bg='#03ccbd' , fg='black' )
pass_entry.bind('<Return>' , submit )

login_btn = Button(main , text = 'Login', font=('courier') , command = lambda:submit(None),bg='#03ccbd' , fg='black',relief = GROOVE)

pass_forg = Button(main , text = 'Forgot Password?' , font=('courier') , bg = '#ff68df' , relief = GROOVE , command=forgotpass)
create_acc = Button(main , text = 'Create New Account' , font=('courier') , bg = '#ff68df' , relief = GROOVE , command=create_acc_fxn )



#PLACING WIDGETS ON MAIN FRAME

user_label.place(relx = 0.05 , rely = 0.1, relwidth = 0.35, relheight = 0.17 )
pass_label.place(relx = 0.02 , rely = 0.35, relwidth = 0.4 , relheight = 0.17)
user_entry.place(relx = 0.5 , rely = 0.1 , relwidth = 0.41 , relheight = 0.17)
pass_entry.place(relx = 0.5 , rely = 0.35 , relwidth = 0.41 , relheight = 0.17)
login_btn.place(relx = 0.375 , rely = 0.8 , relwidth = 0.35 , relheight = 0.15)
pass_forg.place(relx = 0.025 , rely = 0.65 , relwidth = 0.4 , relheight = 0.12)
create_acc.place(relx = 0.55 , rely = 0.65 , relwidth = 0.4 , relheight = 0.12)



#STYLING

relief_widget(login_btn , '#03ccbd' , 'black')
relief_widget(pass_forg , '#ff68df' , 'black')
relief_widget(create_acc,'#ff68df' , 'black')




#CHANGING TEXT SIZE AUTOMATICALLY ON ROOT RESIZE 
def resize(e):
	lb_width = e.width
	user_label.config(font=('courier' ,int (e.width/25) ))
	pass_label.config(font=('courier' , int(e.width/25)))
	login_btn.config(font=('courier' , int(e.width/23)))
	user_entry.config(font=('courier' , int(e.width/24)))
	pass_entry.config(font=('courier' , int(e.width/24)))
	pass_forg.config(font=('courier' , int(e.width/38 + 0.5) , 'bold'))
	create_acc.config(font=('courier' , int(e.width/40 + 0.5) , 'bold'))


#ROOT GRIDS
main.place( relx = 0.4 , rely = 0.4 ,relheight = 0.4 , relwidth = 0.375 )
root.rowconfigure(0 , weight = 1)
main.bind('<Configure>' , resize)



mainloop()
