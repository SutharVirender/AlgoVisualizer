# Import tkinter for GUI

from tkinter import *
from tkinter import ttk
import random 
import time

window = Tk()  # Created main screen window instants (top level widgets)

window.title("Algo Visualizer")
window.maxsize(900,900)
window.config(bg='light steel blue')

# Create two UI frame in the root window 

# top UI frame 
top_frame1 = Frame(window,width=800,height=200,bg="grey")
top_frame1.grid(row=0,column=0,padx=5,pady=5)

top_frame = Canvas(top_frame1,width=750,height=200)
top_frame.grid(row=0,column=0,padx=5,pady=5)

# bottom UI frame 
bottom_frame = Frame(window,width=800,height=300,bg="grey")
bottom_frame.grid(row=1,column=0,padx=5,pady=5)

#create canvas on bottom_frame
canvas = Canvas(bottom_frame,width=750,height=300)
canvas.grid(row=0,column=0,padx=5,pady=5)

label1 = Label(top_frame,text="Choose Algo :",fg="black")
label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")

# create Combobox for selecting algo drop down
def combobox_creation():
	global algoChoosen
	n = StringVar()
	selected_algo = n.get() # value of n can stored permanently otherwise become null during garbage collection
	algoChoosen = ttk.Combobox(top_frame,textvariable=selected_algo)

	# add items for algochoose as list
	algoChoosen["values"] = ("Linear Search","Binary Search")

	# algoChoosen.place(relx=0.23,rely=0.1)
	algoChoosen.grid(row=0,column=1,padx=5,pady=5,sticky="w")
	algoChoosen.current(0)

combobox_creation()  #combobox is created on top_frame



# putting label for generating data options

label2 = Label(top_frame,text="Gener. Data :",fg="black")
label2.grid(row=2,column=0,padx=5,pady=5,sticky="w")



def genData():
	manually_button["state"] = DISABLED

	global data_list,min_value,min_label,max_label,max_value,search_label_auto,ele_search_auto

	size_label = Label(top_frame,text="Size :").grid(row=3,column=0,padx=5,pady=5,sticky="w")
	max_label = Label(top_frame,text="Max Val :").grid(row=3,column=4,padx=5,pady=5,sticky="w")
	min_label = Label(top_frame,text="Min Val :").grid(row=3,column=2,padx=5,pady=5,sticky="w")
	search_label_auto = Label(top_frame,text="Search :").grid(row=3,column=6,padx=5,pady=5,sticky="w")

	# create entry widgets for taking min & max value from user
	size = Entry(top_frame,textvariable=StringVar)
	size.grid(row=3,column=1,padx=5,pady=5,sticky="w")

	min_value = Entry(top_frame,textvariable=StringVar)
	min_value.grid(row=3,column=3,padx=5,pady=5,sticky="w")

	max_value = Entry(top_frame,textvariable=StringVar)
	max_value.grid(row=3,column=5,padx=5,pady=5,sticky="w")

	ele_search_auto = Entry(top_frame,textvariable=StringVar)
	ele_search_auto.grid(row=3,column=7,padx=5,pady=5,sticky="w")

	# backend function for generate button

	def generate_data1():

		global algo_type, search, colors, data_list

		data_list = []
		try :
			m = int(size.get())
		except:
			m = 10

		try :
			mn = int(min_value.get())
		except:
			mn = 1

		try :
			mx = int(max_value.get())
		except:
			mx = 20	

		try :
			search = int(ele_search_auto.get())
		except:
			search = 10

		for i in range(m):
			data_list.append(random.randint(mn,mx))

		algo_type = algoChoosen.get()

		

		colors = ["gray84" for i in range(len(data_list))]

	def Draw_Data1():
		# global data_list,algo_type
		# all visual representation is done here
		canvas.delete("all")

		if algo_type == "Binary Search":
			data_list.sort()

		f_width = 800
		f_height = 300

		# bars
		bar_width = f_width//(len(data_list)+1)
		offset = 30
		spacing = 10
		mx_data = max(data_list)

		for i,height in enumerate(data_list):
			# parameter for rectangle and for that need two point
			#topleft
			x0 = bar_width*i + offset + spacing
			y0 = f_height - (height/mx_data)*(f_height-20)

			#bottomRight
			x1 = bar_width*(i+1) + offset
			y1 = f_height

			canvas.create_rectangle(x0,y0,x1,y1,fill=colors[i],outline="black")
			canvas.create_text(x0+2,y0,anchor="sw",text=str(data_list[i])) 

		# time.sleep(.4)
		window.update_idletasks()


		# making choice for Linear & Binary Search

	def start_search():

		result_frame1 = Frame(window,width=200,height= 50,bg="grey")
		result_frame1.grid(row=2,column=0,padx=5,pady=5)

		result_frame = Canvas(result_frame1,width=150,height=50)
		result_frame.grid(row=0,column=0,padx=5,pady=5)

		Label(result_frame,text="Searching",width=10).grid(row=0,column=0,padx=5,pady=5)

		generate_data1()

		Draw_Data1()
		time.sleep(.4)

		flag = 0

		if algo_type == "Linear Search":

			flag = 0

			for i in range(len(data_list)):
				if data_list[i] == search:
					flag = 1
					colors[i] = "green"
					Draw_Data1()
					time.sleep(.8)
					break
				else:
					colors[i] = "pink"
					Draw_Data1()
					time.sleep(.8)

		else:
			# code for binary search
			i,j = 0,len(data_list)-1

			while i<=j:
				mid = (i+j)//2

				if data_list[mid] == int(search):
					flag = 1
					colors[mid] = "seaGreen1"
					Draw_Data1()
					time.sleep(.8)
					break
				elif data_list[mid] < int(search):
					for i1 in range(i,mid+1):
						colors[i1] = "pink"
					Draw_Data1()
					time.sleep(.8)
					i = mid+1
				else:
					for i1 in range(mid,j+1):
						colors[i1] = "pink"
					Draw_Data1()
					time.sleep(.4)
					j = mid-1

				# time.sleep(.5)

		if flag == 0:
			result_frame.delete("all")
			Label(result_frame,text="Not Found",width=10).grid(row=0,column=0,padx=5,pady=5)
		else:
			result_frame.delete("all")
			Label(result_frame,text="Found",width=10).grid(row=0,column=0,padx=5,pady=5)





	# create a button for generating data from details enteres by user or for reset also
	generate = Button(top_frame,text="Reset Data",command=generate_data1,width=10,bg="white")
	generate.grid(row=5,column=6,padx=5,pady=5,sticky="w")

	Visualize = Button(top_frame,text="Search",command=start_search,width=10,bg="white")
	Visualize.grid(row=5,column=7,padx=5,pady=5,sticky="w") 

def manData():
	# use try and except for removing existing widgets on this position
	auto_button["state"] = DISABLED

	enterData_label = Label(top_frame,text="Enter Data :").grid(row=3,column=0,padx=5,pady=5,sticky="w")
	search_label = Label(top_frame,text="Search :").grid(row=3,column=4,padx=5,pady=5,sticky="w")

	data_set = Entry(top_frame,width=30,textvariable=StringVar)
	data_set.grid(row=3,column=1,padx=5,pady=5,sticky="w")

	ele_search = Entry(top_frame,textvariable=StringVar)
	ele_search.grid(row=3,column=5,padx=5,pady=5,sticky="w")

	# extracting enterd integer value

	def generate_data1():

		global data_list, algo_type, search, colors

		try :
			s = data_set.get().split()
			data_list = list(map(int,s))
			if len(data_list) == 0:
				data_list = [1,2,3,4,5]

		except:
			data_list = [1,2,3,4,5]

		try:
			search = int(ele_search.get())
		except:
			search = 4

		algo_type = algoChoosen.get()

		colors = ["gray84" for i in range(len(data_list))]

	def Draw_Data1():
		# global data_list,algo_type
	# all visual representation is done here
		canvas.delete("all")
		
		search = ele_search.get()

		if algo_type == "Binary Search":
			data_list.sort()

		f_width = 800
		f_height = 300

		# bars
		bar_width = f_width//(len(data_list)+1)
		offset = 30
		spacing = 10
		mx_data = max(data_list)

		for i,height in enumerate(data_list):
			# parameter for rectangle and for that need two point
			#topleft
			x0 = bar_width*i + offset + spacing
			y0 = f_height - (height/mx_data)*(f_height-20)

			#bottomRight
			x1 = bar_width*(i+1) + offset
			y1 = f_height

			canvas.create_rectangle(x0,y0,x1,y1,fill=colors[i],outline="black")
			canvas.create_text(x0+2,y0,anchor="sw",text=str(data_list[i])) 

		# time.sleep(.4)
		window.update_idletasks()


		# making choice for Linear & Binary Search

	def start_search():

		result_frame1 = Frame(window,width=200,height= 50,bg="grey")
		result_frame1.grid(row=2,column=0,padx=5,pady=5)

		result_frame = Canvas(result_frame1,width=150,height=50)
		result_frame.grid(row=0,column=0,padx=5,pady=5)

		Label(result_frame,text="Searching",width=10).grid(row=0,column=0,padx=5,pady=5)

		generate_data1()

		Draw_Data1()
		time.sleep(.4)

		flag = 0

		if algo_type == "Linear Search":

			for i in range(len(data_list)):
				if data_list[i] == search:
					flag = 1
					colors[i] = "seaGreen1"
					Draw_Data1()
					time.sleep(.8)
					break
				else:
					colors[i] = "pink"
					Draw_Data1()
					time.sleep(.8)

		else:
			# code for binary search
			i,j = 0,len(data_list)-1

			while i<=j:
				mid = (i+j)//2

				if data_list[mid] == int(search):
					flag = 1
					colors[mid] = "seaGreen1"
					Draw_Data1()
					time.sleep(.8)
					break
				elif data_list[mid] < int(search):
					for i1 in range(i,mid+1):
						colors[i1] = "pink"
					Draw_Data1()
					time.sleep(.8)
					i = mid+1
				else:
					for i1 in range(mid,j+1):
						colors[i1] = "pink"
					Draw_Data1()
					time.sleep(.8)
					j = mid-1

		if flag == 0:
			result_frame.delete("all")
			Label(result_frame,text="Not Found",width=10).grid(row=0,column=0,padx=5,pady=5)
		else:
			result_frame.delete("all")
			Label(result_frame,text="Found",width=10).grid(row=0,column=0,padx=5,pady=5)

			# time.sleep(.5)

	Visualize = Button(top_frame,text="Search",command=start_search,bg="white")
	Visualize.grid(row=4,column=10,padx=5,pady=5,sticky="e") 

auto_button = Button(top_frame,text="Auto",width=10,command=genData,bg="white")
auto_button.grid(row=2,padx=5,pady=5,column=2,sticky="w")

manually_button = Button(top_frame,text="Manually",command=manData,bg="white")
manually_button.grid(row=2,column=1,padx=5,sticky="w")


window.mainloop()