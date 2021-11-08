from tkinter import *
from ligben import *
import webbrowser

global fl_e1
global fl_e2
global Result


def Redirect(link):
	webbrowser.open_new(link)

def titleAPI(query , frame , k):

	res = GetbyTitle(query)
	output.configure(text = "Results for " + ' Title')
	try:
		res_l1.destroy()
	except:
		print('Not a first Search')

	canvas = Canvas(frame , bg = 'blue' , bd = 0)
	canvas.place(relx = 0 , rely = 0 , relheight = 1 ,relwidth = 1)

	y = 0

	

	Result.update()
	w = Result.winfo_width()
	w -= 30
	h = Result.winfo_height()
	h -= 5
	



def authorAPI(query,frame,k):


	if k == 1:
		res = GetbyAuthor(query)
		output.configure(text = "Results for " + f' Author {query}')
	else:
		res = GetbyTitle(query)
		output.configure(text = "Results for " + f' Title {query}')

	try:
		res_l1.destroy()
	except:
		print('Not a first Search')
	
	canvas = Canvas(frame , bg = 'blue' , bd = 0)
	canvas.place(relx = 0 , rely = 0 , relheight = 1 ,relwidth = 1)

	y = 0

	

	Result.update()
	w = Result.winfo_width()
	w -= 30
	h = Result.winfo_height()
	h -= 5
	
	
	for i in range(1,len(res)):

		try:
			book =  res[i-1]
			
			
			x = int(len(book['Title'])/48) + 1
			x += int(len(book['Author'])/48) + 1
			print(x)
			print(book['Author'])

			TextTitle = book['Title']
			Author = book['Author']
			TextPages = book['Pages']
			TextLang = book['Language']
			Link = book['Mirror_1']

			print(TextTitle)

			lf = LabelFrame(canvas , bg = 'black', width = w+30 , height = (x+8)*40)
			label1 = Label(lf, text= f'Title : {TextTitle}\n', font=("Courier", 18) , bg = 'black' , fg = 'white' , wraplength = w , justify = "center")
			label2 = Label(lf , text = f'Author : {Author}\n',font=("Courier", 18) , bg = 'black' , fg = 'white' , wraplength = w , justify = "center")
			label3 = Label(lf, text= f'Page Count : {TextPages}\n', font=("Courier", 18) , bg = 'black' , fg = 'white' , wraplength = w , justify = "center")
			label4 = Label(lf, text= f'Language: {TextLang}\n', font=("Courier", 18) , bg = 'black' , fg = 'white' , wraplength = w , justify = "center")
			button = Button(lf, text="Download NOW!!!" , bg = 'green' ,font=("Courier", 12) , fg = 'red',justify="center" , pady = 10 ,padx = 10 , command = lambda:Redirect(Link))
			
			label1.grid(row = 1 )
			label2.grid(row = 2 )
			label3.grid(row = 3)
			label4.grid(row = 4)
			# button.grid(row = 5 , width = 30, height =20)
			button.place(relx = 0.4 , relwidth = 0.2 , rely = 0.75 , relheight = 0.15)
			canvas.create_window(0, y, window=lf, anchor=NW , width = Result.winfo_width() ,height = (x+8)*35)
			y += (x+8)*35 + 35
			print((x+8)*35 + 25)
		except:
			# print('exception\n')
			pass

	scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
	scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
	canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))




def createResult(newRoot):
	global Result
	Result = LabelFrame(newRoot )

	t1 = """BOOK NAME
			BOOK INFO 1
			BOOK INFO 2
		"""

	global res_l1
	global output
	output = Label(Result , text = "Search a query to fetch results ")
	res_l1 = Label(Result , text = t1)

	#PUSHING ONto SCREEN
	# output.grid(row = 0 , column = 0 , ipady = 10)
	res_l1.grid(row = 1 , column = 0 , ipady = 10)

	#STYLING WIDGETS
	output.config(font=('courier' , 12))
	
	return Result

def createSearch(newRoot):
	options = ['By Author' , 'By Book Name']
	query = StringVar()
	print("HERE\n")
	SearchFrame = LabelFrame(newRoot , text = "Search For Book")

	global fl_e1 , fl_e2
	global Result
	#WIDGETS FOR SEARCHFRAME FRAME
	fl_l1 = Label(SearchFrame,text = options[0] , bg = 'black' , fg = 'orange')
	fl_e1 = Entry(SearchFrame)
	fl_b1 = Button(SearchFrame , text = 'Search', bg = 'black' , fg = 'orange' , command = lambda:authorAPI(fl_e1.get(),Result,1))

	fl_l2 = Label(SearchFrame,text = options[1] , bg = 'black' , fg = 'orange' )
	fl_e2 = Entry(SearchFrame)
	fl_b2 = Button(SearchFrame , text = 'Search' , bg = 'black' , fg = 'orange' , command = lambda:authorAPI(fl_e2.get(),Result,0))

	#PUSHING ONTO SCREEN
	fl_l1.place(relx = 0.05 , rely = 0.2  , relheight = 0.2, relwidth = 0.3)
	fl_e1.place(relx = 0.4 , rely = 0.2 ,  relheight = 0.2, relwidth = 0.3)
	fl_b1.place(relx = 0.75 , rely = 0.2 ,  relheight = 0.2, relwidth =  0.2)

	fl_l2.place(relx = 0.05 , rely = 0.6,  relheight = 0.2, relwidth = 0.3)
	fl_e2.place(relx = 0.4 , rely = 0.6 ,  relheight = 0.2, relwidth = 0.3 )
	fl_b2.place(relx = 0.75 , rely = 0.6, relheight = 0.2, relwidth = 0.2 )


	#STYLING WIDGETS 
	fl_l1.config(font=('courier',20))
	fl_l2.config(font=('courier',20))

	fl_e1.config(font=('courier',))
	fl_e2.config(font=('courier',))


	fl_b1.config(font = ('courier' , 15))
	fl_b2.config(font = ('courier' , 15))

	binded(fl_b1 , '#000000' , 'orange')
	binded(fl_b2 , '#000000' , 'orange')
	SearchFrame.config(background = 'black' , font = ('courier' , 15) , fg = 'white')

	return SearchFrame

def binded(widget , bcolor , fcolor):
	def hovering(a):
		widget['background'] = fcolor
		widget['foreground'] = bcolor
		widget.config(font=('courier' , 15 , 'bold'))

	def not_hovering(a):
		widget['background'] = bcolor
		widget['foreground'] = fcolor
	
	widget.bind('<Enter>' , hovering)
	widget.bind("<Leave>" , not_hovering)



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
        main.destroy()
        
        NewRoot = Tk()
        SF = createSearch(NewRoot)
        SF.grid(row = 0 , column = 0 , padx = 10 , pady = 20 , ipadx = 50 )

        
        
        print('user verified')
        # root.title('USER VERIFIED')
        root.destroy()
    else:
        print('incorrect password')
        messagebox.showerror('ERROR!!!' , 'Wrong Username password combo' , parent = main )
        user_entry.delete(0,END)
        pass_entry.delete(0,END)

    

