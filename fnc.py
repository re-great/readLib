def createSearch(newRoot):
	options = ['By Author' , 'By Book Name']
	query = StringVar()
	SearchFrame = LabelFrame(newRoot , text = "Search For Book", padx = 10 , pady = 10 , height = 2)

	#WIDGETS FOR SEARCHFRAME FRAME
	fl_l1 = Label(SearchFrame,text = options[0] , bg = 'black' , fg = 'orange')
	fl_e1 = Entry(SearchFrame)
	fl_b1 = Button(SearchFrame , text = 'Search' ,command = lambda:Search(fl_e1.get()) , bg = 'black' , fg = 'orange' )

	fl_l2 = Label(SearchFrame,text = options[1] , bg = 'black' , fg = 'orange' )
	fl_e2 = Entry(SearchFrame)
	fl_b2 = Button(SearchFrame , text = 'Search' , command = lambda:Search(fl_e2.get()) , bg = 'black' , fg = 'orange')

	#PUSHING ONTO SCREEN
	fl_l1.grid(row = 0 , column = 0  , ipadx = 20 , ipady = 25)
	fl_e1.grid(row = 0 , column = 1 , padx = 20)
	fl_b1.grid(row = 0 , column = 2, ipadx = 20 )

	fl_l2.grid(row = 1 , column = 0 , pady = 20 , ipadx = 20 , ipady = 20)
	fl_e2.grid(row = 1 , column = 1 , padx = 20 )
	fl_b2.grid(row = 1 , column = 2, ipadx = 25 )


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

    