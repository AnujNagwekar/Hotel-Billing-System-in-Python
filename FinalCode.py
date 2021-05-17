from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("1300x700+0+0")
window.maxsize(width = 1280,height = 700)
window.minsize(width = 1280,height = 700)
window.title("Hotel Billing System")
window.wm_iconbitmap("Burger.ico")

bg_color = "grey"
fg_color = "white"
lbl_color = 'white'


# ========================Methods are defined here====================
total_food = StringVar()
total_bev = StringVar()
def total():
        a= bug_en.get() 
        b= bread_en.get()
        c= pizza_en.get()
        d= hotdog_en.get()
        e= sw_en.get()
        f= alooparatha_en.get()
        g= pavbhaji_en.get()
        h= dosa_en.get()
        i= idli_en.get()
        j=icecream_en.get()
        k= cocen.get()
        l= d2en.get()
        m= d3en.get()
        n= d4en.get()
        o= d5en.get()
        total_food_prices = (
            (int(a) * 50) +
            (int(b) * 20) +
            (int(c) * 100) +
            (int(d) * 40) +
            (int(e) * 45) +
            (int(f) * 20) +
            (int(g) * 45) +
            (int(h) * 35) +
            (int(i) * 25) +
            (int(j) * 30) 
             )
          
        total_food.set(str(total_food_prices))

        total_bev_prices= (
            (int(k) * 25) +
            (int(l) * 20) +
            (int(m) * 30) +
            (int(n) * 20) +
            (int(o) * 10)
        )
        total_bev.set(str(total_bev_prices))

def bill_a():
        
        
        txt.insert(END,"       Welcome To Hotel SAYOTA\n")
        txt.insert(END,f"\nBill No. : {str(cbill_en.get())}")
        txt.insert(END,f"\nCustomer Name : {str(cname_en.get())}")
        txt.insert(END,f"\nPhone No. : {str(cphon_en.get())}")
        txt.insert(END,"\n===================================")
        txt.insert(END,"\nProduct          Qty         Price")
        txt.insert(END,"\n===================================")
        if bug_en.get() != "0":
            txt.insert(END,f"\nBurger            {bug_en.get()}           {int(bug_en.get()) * 50}")
            
            
        if bread_en.get() != "0":
            txt.insert(END,f"\nBread             {bread_en.get()}           {int(bread_en.get()) * 20}")
            
        if pizza_en.get() != "0":
            txt.insert(END,f"\nPizza             {pizza_en.get()}           {int(pizza_en.get()) * 100}")
            
        if hotdog_en.get() != "0":
            txt.insert(END,f"\nHotdog            {hotdog_en.get()}           {int(hotdog_en.get()) * 40}")
            
        if sw_en.get() != "0":
            txt.insert(END,f"\nSandwich          {sw_en.get()}           {int(sw_en.get()) * 45}")
            
        if alooparatha_en.get() != "0":
            txt.insert(END,f"\nAloo Paratha      {alooparatha_en.get()}           {int(alooparatha_en.get()) * 20}")
            
        if pavbhaji_en.get() != "0":
            txt.insert(END,f"\nPav Bhaji         {pavbhaji_en.get()}           {int(pavbhaji_en.get()) * 45}")
            
        if dosa_en.get() != "0":
            txt.insert(END,f"\nDosa              {dosa_en.get()}           {int(dosa_en.get()) * 35}")
             
        if idli_en.get() != "0":
            txt.insert(END,f"\nIdli              {idli_en.get()}           {int(idli_en.get()) * 25}")
            
        if icecream_en.get() != "0":
            txt.insert(END,f"\nIcecream          {icecream_en.get()}           {int(icecream_en.get()) * 30}")
            
        if cocen.get() != "0":
            txt.insert(END,f"\nCoca Cola         {cocen.get()}           {int(cocen.get()) * 25}")
            
        if d2en.get() != "0":
            txt.insert(END,f"\nSprite            {d2en.get()}           {int(d2en.get()) * 20}")
            
        if d3en.get() != "0":
            txt.insert(END,f"\nThumps Up         {d3en.get()}           {int(d3en.get()) * 30}")
            
        if d4en.get() != "0":
            txt.insert(END,f"\nPepsi             {d4en.get()}           {int(d4en.get()) * 20}")
            
        if d5en.get() != "0":
            txt.insert(END,f"\nPaper Boat        {d5en.get()}           {int(d5en.get()) * 10}")
            
        txt.insert(END,"\n===================================")
        
        txt.insert(END,f"\n                    Total : Rs {int(total_food.get())+int(total_bev.get())}")
         
   

def save_bill():
    san = cname_en.get()
    rad = cphon_en.get()
    tri = cbill_en.get()
    st = "       Welcome To Hotel SAYOTA\n"
    st += f"\nBill No. : {str(cbill_en.get())}"
    st +=  f"\nCustomer Name : {str(cname_en.get())}"
    st += f"\nPhone No. : {str(cphon_en.get())}"
    st += "\n==================================="
    st += "\nProduct          Qty         Price"
    st += "\n==================================="
    if bug_en.get() != "0":
        
        st += (f"\nBurger            {bug_en.get()}           {int(bug_en.get()) * 50}")
            
    if bread_en.get() != "0":
         
        st += (f"\nBread             {bread_en.get()}           {int(bread_en.get()) * 20}")
    if pizza_en.get() != "0":
         
        st += f"\nPizza             {pizza_en.get()}           {int(pizza_en.get()) * 100}"
    if hotdog_en.get() != "0":
        
        st += f"\nHotdog            {hotdog_en.get()}           {int(hotdog_en.get()) * 40}"
    if sw_en.get() != "0":
        
        st += f"\nSandwich          {sw_en.get()}           {int(sw_en.get()) * 45}"
    if alooparatha_en.get() != "0":
        
        st += f"\nAloo Paratha      {alooparatha_en.get()}           {int(alooparatha_en.get()) * 20}"
    if pavbhaji_en.get() != "0":
        
        st += f"\nPav Bhaji         {pavbhaji_en.get()}           {int(pavbhaji_en.get()) * 45}"
    if dosa_en.get() != "0":
         
        st += f"\nDosa              {dosa_en.get()}           {int(dosa_en.get()) * 35}"
    if idli_en.get() != "0":
         
        st += f"\nIdli              {idli_en.get()}           {int(idli_en.get()) * 25}"
    if icecream_en.get() != "0":
        
        st += f"\nIcecream          {icecream_en.get()}           {int(icecream_en.get()) * 30}"
    if cocen.get() != "0":
    
        st += f"\nCoca Cola         {cocen.get()}           {int(cocen.get()) * 25}"
    if d2en.get() != "0":
        
        st += f"\nSprite            {d2en.get()}           {int(d2en.get()) * 20}"
    if d3en.get() != "0":
        
        st += f"\nThumps Up         {d3en.get()}           {int(d3en.get()) * 30}"
    if d4en.get() != "0":
        
        st += f"\nPepsi             {d4en.get()}           {int(d4en.get()) * 20}"
    if d5en.get() != "0":
        
        st += f"\nPaper Boat        {d5en.get()}           {int(d5en.get()) * 10}"
    st += "\n==================================="
    st += f"\n                      Total : Rs {int(total_food.get())+int(total_bev.get())}"
    file = open(f"{san+tri}.txt", "w")
    file.write(st)
    file.close()
    messagebox.showinfo("Billing Status" , "Bill Saved Succesfully!")

def clear():
        
        
        txt.delete('1.0',END)
        bug_en.delete(0, 'end')                      #Food
        bug_en.insert(END, '0')
        bread_en.delete(0, 'end')
        bread_en.insert(END, '0')
        pizza_en.delete(0, 'end')
        pizza_en.insert(END, '0')
        hotdog_en.delete(0, 'end')
        hotdog_en.insert(END, '0')
        sw_en.delete(0, 'end')
        sw_en.insert(END, '0')
        alooparatha_en.delete(0, 'end')
        alooparatha_en.insert(END, '0')
        pavbhaji_en.delete(0, 'end')
        pavbhaji_en.insert(END, '0')
        dosa_en.delete(0, 'end')
        dosa_en.insert(END, '0')
        idli_en.delete(0, 'end')
        idli_en.insert(END, '0')
        icecream_en.delete(0, 'end')
        icecream_en.insert(END, '0')
        cocen.delete(0, 'end')
        cocen.insert(END, '0')
        d2en.delete(0, 'end')
        d2en.insert(END, '0')
        d3en.delete(0, 'end')
        d3en.insert(END, '0')
        d4en.delete(0, 'end')
        d4en.insert(END, '0')
        d5en.delete(0, 'end')
        d5en.insert(END, '0')
        cphon_en.delete(0, 'end')                   #Customer Details
        
        cname_en.delete(0, 'end')
        
        cbill_en.delete(0, 'end')
                          
        Total_beverages_en.delete(0, 'end')
        Total_beverages_en.insert(END, '0')
        total_food_en.delete(0, 'end')
        total_food_en.insert(END, '0') 


def exit():
    window.destroy()


# =====================Methods are defined above======================






title = Label(window,text = "HOTEL SAYOTA",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("comic sans ms",30,"bold"),pady = 3).pack(fill = X)

F1 = LabelFrame(window,bd=10,text = 'Beverages',bg = "grey",
                            fg = "gold",font = ("comic sans ms",13,"bold"))
F1.place(x = 650,y = 160,width = 325,height = 380)

coc = Label(F1,font = ("comic sans ms",13,"bold"),fg ="white",bg = "grey",text = "Coca Cola")
coc.grid(row = 0,column = 0,padx = 10,pady = 20)
cocen = Entry(F1,bd = 8,relief = GROOVE)
cocen.insert(END, '0')
cocen.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

d2 = Label(F1,font = ("comic sans ms",13,"bold"),fg ="white",bg = "grey",text = "Sprite")
d2.grid(row = 1,column = 0,padx = 10,pady = 20)
d2en = Entry(F1,bd = 8,relief = GROOVE)
d2en.insert(END, '0')
d2en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

d3 = Label(F1,font = ("comic sans ms",13,"bold"),fg ="white",bg = "grey",text = "Thumbs Up")
d3.grid(row = 2,column = 0,padx = 10,pady = 20)
d3en = Entry(F1,bd = 8,relief = GROOVE)
d3en.insert(END, '0')
d3en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

d4 = Label(F1,font = ("comic sans ms",13,"bold"),fg ="white",bg = "grey",text = "Pepsi")
d4.grid(row = 3,column = 0,padx = 10,pady = 20)
d4en = Entry(F1,bd = 8,relief = GROOVE)
d4en.insert(END, '0')
d4en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

d5 = Label(F1,font = ("comic sans ms",13,"bold"),fg ="white",bg = "grey",text = "Paper Boat")
d5.grid(row = 4,column = 0,padx = 10,pady = 20)
d5en = Entry(F1,bd = 8,relief = GROOVE)
d5en.insert(END, '0')
d5en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)



F2 = LabelFrame(window,text = 'Food',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("comic sans ms",13,"bold"))
F2.place(x = 325,y = 160,width = 325,height = 380)
#==========Frame Content=============  
alooparatha_lbl = Label(F2,font = ("comic sans ms",13,"bold"),fg = lbl_color, bg = bg_color, text = "Aloo Paratha")
alooparatha_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
alooparatha_en = Entry(F2,bd = 8,relief = GROOVE,)
alooparatha_en.insert(END, '0')
alooparatha_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)
#=======
pavbhaji_lbl = Label(F2,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Pav Bhaji")
pavbhaji_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
pavbhaji_en = Entry(F2,bd = 8,relief = GROOVE,)
pavbhaji_en.insert(END, '0')
pavbhaji_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
#=======
dosa_lbl = Label(F2,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Dosa")
dosa_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
dosa_en = Entry(F2,bd = 8,relief = GROOVE,)
dosa_en.insert(END, '0')
dosa_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
#========
idli_lbl = Label(F2,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Idli")
idli_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
idli_en = Entry(F2,bd = 8,relief = GROOVE,)
idli_en.insert(END, '0')
idli_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)
#========
icecream_lbl = Label(F2,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Icecream")
icecream_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
icecream_en = Entry(F2,bd = 8,relief = GROOVE,)
icecream_en.insert(END, '0')
icecream_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)



F3 = LabelFrame(window,bd=10,text = 'Food',bg = "grey",
                            fg = "gold",font = ("comic sans ms",13,"bold"))
F3.place(x = 0,y = 160,width = 325,height = 380)
# Food labels
        # ======Burger
bug_lbl = Label(F3,font = ("comic sans ms",13,"bold"),fg =lbl_color,bg =bg_color ,text = "Burger")
bug_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
bug_en = Entry(F3,bd = 8,relief=GROOVE)
bug_en.insert(END, '0')
bug_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
       
       
        # =======Bread Butter
bread_lbl = Label(F3,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Bread Butter")
bread_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
bread_en = Entry(F3,bd = 8,relief = GROOVE)
bread_en.insert(END, '0')
bread_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

       
        #=======Pizza
pizza_lbl = Label(F3,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Pizza")
pizza_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
pizza_en = Entry(F3,bd = 8,relief = GROOVE)
pizza_en.insert(END, '0')
pizza_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

      
        #========Hotdog
hotdog_lbl = Label(F3,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Hotdog")
hotdog_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
hotdog_en = Entry(F3,bd = 8,relief = GROOVE)
hotdog_en.insert(END, '0')
hotdog_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

       
        #============Sandwich
sw_lbl = Label(F3,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Sandwich")
sw_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
sw_en = Entry(F3,bd = 8,relief = GROOVE)
sw_en.insert(END, '0')
sw_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)


#Total===============================================================================



# Buttons and Total Frame ===================================================

F4 = LabelFrame(window,bd=20,text = 'Generate Bill',bg = "grey",
                            fg = "gold",font = ("comic sans ms",13,"bold"))
F4.place(x = 0,y = 540,relwidth = 1,height = 145)

total_food_lbl = Label(F4,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Total Food")
total_food_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
total_food_en = Entry(F4,bd = 8,relief = GROOVE, textvariable =total_food)
total_food_en.insert(END, '0')
total_food_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
Total_beverages_lbl = Label(F4,font = ("comic sans ms",13,"bold"),fg = lbl_color,bg = bg_color,text = "Total beverages")
Total_beverages_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
Total_beverages_en = Entry(F4,bd = 8,relief = GROOVE , textvariable = total_bev)
Total_beverages_en.insert(END, '0')
Total_beverages_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)
        #====================
total_btn = Button(F4,text = "Total",bg = bg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE, command= total)
total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
genrate_bill_btn = Button(F4,text = "Generate Bill",bg = bg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE , command = bill_a)
genrate_bill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
clear_btn = Button(F4,text = "Clear",bg = bg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE, command = clear)
clear_btn.grid(row = 1,column = 7,ipadx = 20)

        #======================
exit_btn = Button(F4,text = "Exit",bg = bg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE , command = exit)
exit_btn.grid(row = 1,column = 8,ipadx = 20,padx = 30)


save_btn = Button(F4, text = "Save",bg = bg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE , command =save_bill)
save_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)


# Bill frame===========================================================================================
F5 = Label(window,bd = 10,relief = GROOVE)
F5.place(x = 970,y = 160,width = 310,height = 380)
bill_title = Label(F5,text = "Bill List",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
bill_title.pack(fill = X)

txt = Text(F5)
txt.pack(fill = BOTH,expand = 1)



# Customer Frame==================================================================================================
#Frame 1
F = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),
 fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F.place(x = 0,y = 80,relwidth = 1)


#===============Customer Name===========#
cname_lbl = Label(F,text="Customer Name",bg = bg_color,fg = fg_color,font=("comic sans ms",13,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
cname_en = Entry(F,bd = 8,relief = GROOVE)
cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

#=================Customer Phone==============#
cphon_lbl = Label(F,text = "Phone No",bg = bg_color,fg = fg_color,font = ("comic sans ms",13,"bold")).grid(row = 0,column = 2,padx = 20)
cphon_en = Entry(F,bd = 8,relief = GROOVE)
cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

#====================Customer Bill No==================#
cbill_lbl = Label(F,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("comic sans ms",13,"bold"))
cbill_lbl.grid(row = 0,column = 4,padx = 20)
cbill_en = Entry(F,bd = 8,relief = GROOVE)
cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)



window.mainloop()
