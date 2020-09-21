from tkinter import *
import sys

sys.setrecursionlimit(10**4)
root = Tk()
root.geometry("662x500+300+100")
grid = []
count = 0
c = 0
start, end=None, None
btn = None
rst = None
branch = []
path = []
path_ind = -1
find = False
for i in range(19*30):
	path.append(-1)


def counter(n):
	global c

	if n-30 < 0:
		return c, n
	else:
		c += 1
		return counter(n-30)


def backtrack(n):
	global start, end, c
	if path[n] != -1:
		a = path[n][0]*30+path[n][1]
		backtrack(a)
	s = start.grid_info()["row"]*30+start.grid_info()["column"]
	e = end.grid_info()["row"]*30+end.grid_info()["column"]
	if n != s and n != e:
		c = 0
		row , col = counter(n)
		grid[row][col]["bg"] = "light blue"
	return


def set_branch(row, col, p_row, p_col):
	global branch, path_ind, find
	if row > 18 or row < 0 or col > 29 or col<0:
		return
	elif grid[row][col]["bg"] == "green":
		find = True
		path_ind = row*30+col
		path[path_ind] = (p_row,p_col)
		return
	elif grid[row][col]["bg"] == "red":
		path_ind = row*30+col
		grid[row][col]["bg"] = "yellow"
		branch.append((row,col))
		path[path_ind] = (p_row,p_col)
	return


def start_game(start_row, start_col):
	#print(start_row,start_col)
	p_row,p_col = start_row,start_col
	global branch
	set_branch(start_row-1,start_col,p_row,p_col)
	set_branch(start_row,start_col+1,p_row,p_col)
	set_branch(start_row+1,start_col,p_row,p_col)
	set_branch(start_row,start_col-1,p_row,p_col)
	branch.remove((start_row,start_col))
	return


def loop(start_row, start_col):
	global branch, end, count
	branch.append((start_row, start_col))
	start_game(start_row, start_col)
	if count == 0 or count == 1:
		pass
	elif find == True:
		backtrack(end.grid_info()["row"]*30+end.grid_info()["column"])
		return
	else:
		loop(branch[0][0],branch[0][1])


def restart():
	global start,end,branch,path,grid,count,c,path_ind,find
	start = None
	end = None
	branch =[]
	path =[-1]*19*30
	grid = []
	count, c = 0,0
	path_ind = -1
	find = False
	make_grid()


def start_fun():
	global btn,rst,start
	btn = Button(root, text="START", command=lambda : loop(start.grid_info()["row"], start.grid_info()["column"]) if (start != None) else False)
	btn.grid(row=30, column=17, columnspan=2)
	rst = Button(root, text="RESTART", command=restart)
	rst.grid(row=30, column=10, columnspan=3)


def click(event):
	global count,start,end
	if count == 0 and event.widget != btn and event.widget != rst:
		start = event.widget
		start["bg"] = "blue"
		count+=1
	elif count == 1 and event.widget != btn and event.widget != start and event.widget != rst:
		end = event.widget
		end["bg"] = "green"
		count+=1
	else:
		if event.widget != start and event.widget != end and event.widget != btn and event.widget != rst:
			event.widget["bg"] = "black"
			count+=1

def make_grid():
	for i in range(19):
		grid.append([])
		for j in range(30):
			b = Button(root, bg="red", width=2, bd=1)
			b.grid(row=i,column=j)
			grid[i].append(b)

make_grid()
start_fun()
root.bind("<Button-1>", click)
root.mainloop()