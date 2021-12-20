from tkinter import *
from tkinter import ttk, messagebox


# ==================================== Exit Function ===================================================
def iExit():
    iExit = messagebox.askyesno("Vehicle Trading System", "Confirm if you want to exit!")
    if iExit > 0:
        root.destroy()
        return


# ==================================== Reset Function ===================================================
def Reset():
    CustomerName.set("")
    CustomerAddress.set("")
    CustomerPin.set("")
    CustomerNumber.set("")
    Modified.set("0")
    Stereo.set("0")
    Customized.set("0")
    Leather.set("0")
    GPS.set("0")
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var18.set(0)
    CustomerName.set("")
    CustomerAddress.set("")
    CustomerNumber.set("")
    CustomerPin.set("")
    CostofCar.set("0")
    CarMileage.set("0")
    VAT.set("0")
    Discount.set("0")
    Tax.set("0")
    SubTotal.set("0")
    Total.set("0")
    txtReceipt.delete("1.0", END)


def CarCost():
    if var7.get() == 'Lamborghini':
        myCar = float(98734.90)
        CostofCar.set(myCar)
    elif var7.get() == 'Bugatti Veyron':
        myCar = float(103875.45)
        CostofCar.set(myCar)
    elif var7.get() == 'Rolls Royce':
        myCar = float(89757.29)
        CostofCar.set(myCar)
    elif var7.get() == 'Aston Martin':
        myCar = float(123775.80)
        CostofCar.set(myCar)
    # ==================================== Lamborghini ===================================================
    if var18.get() == '100-5000' and var7.get() == 'Lamborghini':
        myCar = float(98734.71)
        iMile = float(5012.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '5001-20000' and var7.get() == 'Lamborghini':
        myCar = float(98734.71)
        iMile = float(4010.70)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '20001-100000' and var7.get() == 'Lamborghini':
        myCar = float(98734.71)
        iMile = float(2002.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '100001-1000000' and var7.get() == 'Lamborghini':
        myCar = float(98734.71)
        iMile = float(1312.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    # ==================================== Bugatti ===================================================
    if var18.get() == '100-5000' and var7.get() == 'Bugatti Veyron':
        myCar = float(78354.71)
        iMile = float(6501.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '5001-20000' and var7.get() == 'Bugatti Veyron':
        myCar = float(78354.71)
        iMile = float(5012.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '20001-100000' and var7.get() == 'Bugatti Veyron':
        myCar = float(78354.71)
        iMile = float(3789.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '100001-1000000' and var7.get() == 'Bugatti Veyron':
        myCar = float(78354.71)
        iMile = float(2310.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)

    # ==================================== Rolls Royce ===================================================
    if var18.get() == '100-5000' and var7.get() == 'Rolls Royce':
        myCar = float(89734.94)
        iMile = float(6501.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '5001-20000' and var7.get() == 'Rolls Royce':
        myCar = float(89734.94)
        iMile = float(5012.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '20001-100000' and var7.get() == 'Rolls Royce':
        myCar = float(89734.94)
        iMile = float(4789.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '100001-1000000' and var7.get() == 'Rolls Royce':
        myCar = float(89734.94)
        iMile = float(3310.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)

    # ==================================== Aston Martin ===================================================
    if var18.get() == '100-5000' and var7.get() == 'Aston Martin':
        myCar = float(127734.84)
        iMile = float(10100.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '5001-20000' and var7.get() == 'Aston Martin':
        myCar = float(127734.84)
        iMile = float(8010.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '20001-100000' and var7.get() == 'Aston Martin':
        myCar = float(127734.84)
        iMile = float(6989.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)
    if var18.get() == '100001-1000000' and var7.get() == 'Aston Martin':
        myCar = float(127734.84)
        iMile = float(4340.90)
        CarMileage.set(iMile)
        CostofCar.set(myCar)

    # ===============================================================================================================
    if var1.get() == 1:
        Modified.set(5023)
    elif var1.get() == 0:
        Modified.set(0)

    if var2.get() == 1:
        Stereo.set(356)
    elif var2.get() == 0:
        Stereo.set(0)

    if var3.get() == 1:
        Leather.set(4699)
    elif var3.get() == 0:
        Leather.set(0)

    if var4.get() == 1:
        Customized.set(10089)
    elif var4.get() == 0:
        Customized.set(0)

    if var5.get() == 1:
        GPS.set(5023)
    elif var5.get() == 0:
        GPS.set(0)

    if var8.get() == 1:
        VAT.set("YES")
    elif var8.get() == 0:
        VAT.set("NO")

    if var9.get() == 1:
        Discount.set("YES")
    elif var9.get() == 0:
        Discount.set("NO")

    Item1 = float(CostofCar.get())
    Item2 = float(CarMileage.get())
    Item3 = float(Modified.get())
    Item4 = float(Stereo.get())
    Item5 = float(Leather.get())
    Item6 = float(Customized.get())
    Item7 = float(GPS.get())
    Item8 = str('%.2f' % ((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7))
    Item9 = (((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7) * 0.45) / 100
    Item9 = str('%.2f' % Item9)
    Item10 = (((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7) * 0.45) / 100
    Item11 = ((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7)
    Item12 = str('%.2f' % (Item10 + Item11))
    SubTotal.set(Item8)
    Tax.set(Item9)
    Total.set(Item12)


def Receipt():
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items\n\n")
    txtReceipt.insert(END, '===================================='"\n")
    txtReceipt.insert(END, 'Customer Name:\t\t\t\t' + CustomerName.get() + "\n")
    txtReceipt.insert(END, '===================================='"\n")
    txtReceipt.insert(END, 'Type of Car:\t\t\t\t' + var7.get() + "\n")
    txtReceipt.insert(END, 'Cost of Car:\t\t\t\t' + CostofCar.get() + "\n")
    txtReceipt.insert(END, 'Trade in value:\t\t\t\t' + CarMileage.get() + "\n")
    txtReceipt.insert(END, 'Cost of Modification:\t\t\t\t' + Modified.get() + "\n")
    txtReceipt.insert(END, 'Cost of Stereo:\t\t\t\t' + Stereo.get() + "\n")
    txtReceipt.insert(END, 'Cost of Leather:\t\t\t\t' + Leather.get() + "\n")
    txtReceipt.insert(END, 'Cost of Customization:\t\t\t\t' + Customized.get() + "\n")
    txtReceipt.insert(END, 'Cost of GPS:\t\t\t\t' + GPS.get() + "\n")
    txtReceipt.insert(END, '===================================='"\n")
    txtReceipt.insert(END, 'Tax:\t\t\t\t' + Tax.get() + "\n")
    txtReceipt.insert(END, 'SubTotal:\t\t\t\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Total:\t\t\t\t' + Total.get() + "\n")
    txtReceipt.insert(END, '===================================='"\n")


# ==================================== Defining Frame Size ===================================================
root = Tk()
root.geometry("1352x650+0+0")
root.title("Vehicle Trading Management System")
root.configure(background='black')

Tops = Frame(root, width=1352, height=100, bd=4, relief="raise")
Tops.pack(side=TOP)

lblInfo = Label(Tops, font=('ariel', 49, 'bold'), text='  Vehicle Trading Management System  ', bd=5, anchor='w')
lblInfo.grid(row=0, column=0)

bottom = Frame(root, width=1350, height=600, bd=2, relief="raise")
bottom.pack(side=TOP)

bottomLeft = Frame(bottom, width=1000, height=600, bd=2, relief="raise")
bottomLeft.pack(side=LEFT)
# -----------------------------------------------------------------------------------------------------------------
bottomLeftTop = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
bottomLeftTop.pack(side=TOP)

bottomLeftTopL = Frame(bottomLeftTop, width=500, height=300, bd=2, relief="raise")
bottomLeftTopL.pack(side=LEFT)

bottomLeftTopR = Frame(bottomLeftTop, width=500, height=300, bd=2, relief="raise")
bottomLeftTopR.pack(side=RIGHT)
# -----------------------------------------------------------------------------------------------------------------
bottomLeftBottom = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
bottomLeftBottom.pack(side=BOTTOM)

bottomLeftBottomL = Frame(bottomLeftBottom, width=500, height=300, bd=2, relief="raise")
bottomLeftBottomL.pack(side=LEFT)

bottomLeftBottomR = Frame(bottomLeftBottom, width=500, height=300, bd=2, relief="raise")
bottomLeftBottomR.pack(side=RIGHT)
# -----------------------------------------------------------------------------------------------------------------
bottomRight = Frame(bottom, width=350, height=600, bd=4, relief="raise")
bottomRight.pack(side=RIGHT)

# ===================================== Top Left Table =================================================================
# -------------------------------Personal Details-------------------------------------------------------------------
CustomerName = StringVar()
CustomerAddress = StringVar()
CustomerPin = StringVar()
CustomerNumber = StringVar()

# Name of Customer
lblName = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Name", fg="black", width=15, bd=10, anchor='w')
lblName.grid(row=0, column=0)
txtName = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
                textvariable=CustomerName)
txtName.grid(row=0, column=1)

# Address of Customer
lblAddress = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Address", fg="black", width=15, bd=10, anchor='w')
lblAddress.grid(row=1, column=0)
txtAddress = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
                   textvariable=CustomerAddress)
txtAddress.grid(row=1, column=1)

# Pin Code of Customer's Address
lblPin = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="PIN Code", fg="black", width=15, bd=10, anchor='w')
lblPin.grid(row=2, column=0)
txtPin = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
               textvariable=CustomerPin)
txtPin.grid(row=2, column=1)

# Contact Number of Customer
lblNumber = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Contact Number", fg="black", width=15, bd=10,
                  anchor='w')
lblNumber.grid(row=3, column=0)
txtNumber = Entry(bottomLeftTopL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
                  textvariable=CustomerNumber)
txtNumber.grid(row=3, column=1)

# ======================================= Bottom Left Table ========================================================
Modified = StringVar()
Stereo = StringVar()
Customized = StringVar()
Leather = StringVar()
GPS = StringVar()

Modified.set("0")
Stereo.set("0")
Customized.set("0")
Leather.set("0")
GPS.set("0")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

# ------------------------------------ Modifications ------------------------------------------------------
lblModified = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), onvalue=1, offvalue=0, text="Modified",
                          fg="black", width=20, bd=10, anchor='w', variable=var1)
lblModified.grid(row=0, column=0)
txtModified = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
                    textvariable=Modified)
txtModified.grid(row=0, column=1)

# ------------------------------------ Stereo -------------------------------------------------------------
lblStereo = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Stereo System", onvalue=1, offvalue=0,
                        fg="black", width=20, bd=10, anchor='w', variable=var2)
lblStereo.grid(row=1, column=0)
txtStereo = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
                  textvariable=Stereo)
txtStereo.grid(row=1, column=1)

# ------------------------------------ Leather -------------------------------------------------------------
lblLeather = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), onvalue=1, offvalue=0,
                         text="Leather Interior", fg="black", width=20, bd=10, anchor='w', variable=var3)
lblLeather.grid(row=2, column=0)
txtLeather = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
                   textvariable=Leather)
txtLeather.grid(row=2, column=1)
# ------------------------------------ Customized ----------------------------------------------------------
lblCustomized = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), onvalue=1, offvalue=0,
                            text="Customization Details", fg="black", width=20, bd=10, anchor='w', variable=var4)
lblCustomized.grid(row=3, column=0)
txtCustomized = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
                      textvariable=Customized)
txtCustomized.grid(row=3, column=1)
# -------------------------------------- GPS ---------------------------------------------------------------
lblGPS = Checkbutton(bottomLeftBottomL, font=('arial', 16, 'bold'), onvalue=1, offvalue=0,
                     text="Global Positioning System", fg="black", width=20, bd=10, anchor='w', variable=var5)
lblGPS.grid(row=4, column=0)
txtGPS = Entry(bottomLeftBottomL, font=('arial', 16, 'bold'), width=24, bd=2, bg="white", justify='left',
               textvariable=GPS)
txtGPS.grid(row=4, column=1)
# ============================== Receipt and Total Cost Button ========================================================
btnTotalCost = Button(bottomLeftBottomL, pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Total",
                      bg="white", command=CarCost).grid(row=5, column=0)
btnReceipt = Button(bottomLeftBottomL, pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Receipt",
                    bg="white", command=Receipt).grid(row=5, column=1)

# ====================================== Car's Cost, Mileage, Trade ===================================================
var6 = IntVar()
var7 = StringVar()
var18 = StringVar()

CostofCar = StringVar()
CarMileage = StringVar()

CostofCar.set("0")
CarMileage.set("0")

lblChooseCar = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Choose a Car", fg="black", width=13, bd=14,
                     anchor='w')
lblChooseCar.grid(row=0, column=0)
cboChooseCar = ttk.Combobox(bottomLeftTopR, textvariable=var7, state='readonly', font=('arial', 20, 'bold'), width=12)
cboChooseCar['value'] = ('', 'Lamborghini', 'Bugatti Veyron', 'Rolls Royce', 'Aston Martin')
cboChooseCar.current(0)
cboChooseCar.grid(row=1, column=0)

lblCost = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Cost of a Car", fg="black", width=13, bd=14,
                anchor='w')
lblCost.grid(row=2, column=0)
txtCost = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), width=16, bd=2, bg="white", justify='left',
                textvariable=CostofCar)
txtCost.grid(row=3, column=0)

lblTrade = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Trade in a Car", fg="black", width=13, bd=14,
                 anchor='w')
lblTrade.grid(row=0, column=1)
cboTrade = ttk.Combobox(bottomLeftTopR, textvariable=var18, state='readonly', font=('arial', 20, 'bold'),
                        width=12)
cboTrade['value'] = ('', '100-5000', '5001-20000', '20001-100000', '100001-1000000')
cboTrade.current(0)
cboTrade.grid(row=1, column=1)

lblMileage = Label(bottomLeftTopR, font=('arial', 16, 'bold'), text="Car Mileage", fg="black", width=13, bd=14,
                   anchor='w')
lblMileage.grid(row=2, column=1)
txtMileage = Entry(bottomLeftTopR, font=('arial', 16, 'bold'), width=16, bd=2, bg="white", justify='left',
                   textvariable=CarMileage)
txtMileage.grid(row=3, column=1)

# ==================================== VAT, Discount, TAX, Total ===================================================
VAT = StringVar()
Discount = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

var8 = IntVar()
var9 = IntVar()

lblVAT = Checkbutton(bottomLeftBottomR, font=('arial', 16, 'bold'), text="VAT", fg="black", width=13, bd=14, anchor='w',
                     onvalue=1, offvalue=0, variable=var8)
lblVAT.grid(row=0, column=0)
txtVAT = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), width=16, bd=2, bg="white", justify='left',
               textvariable=VAT)
txtVAT.grid(row=0, column=1)

lblDiscount = Checkbutton(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Discount", fg="black", width=13, bd=14,
                          anchor='w', onvalue=1, offvalue=0, variable=var9)
lblDiscount.grid(row=1, column=0)
txtDiscount = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), width=16, bd=2, bg="white", justify='left',
                    textvariable=Discount)
txtDiscount.grid(row=1, column=1)

lblTax = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Tax", fg="black", width=13, bd=14, anchor='w')
lblTax.grid(row=2, column=0)
txtTax = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), width=16, bd=2, bg="white", justify='left',
               textvariable=Tax)
txtTax.grid(row=2, column=1)

lblSubTotal = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Sub Total", fg="black", width=13, bd=14,
                    anchor='w')
lblSubTotal.grid(row=3, column=0)
txtSubTotal = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), width=16, bd=2, bg="white", justify='left',
                    textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1)

lblTotal = Label(bottomLeftBottomR, font=('arial', 16, 'bold'), text="Total", fg="black", width=13, bd=14, anchor='w')
lblTotal.grid(row=4, column=0)
txtTotal = Entry(bottomLeftBottomR, font=('arial', 16, 'bold'), width=16, bd=2, bg="white", justify='left',
                 textvariable=Total)
txtTotal.grid(row=4, column=1)

# ==================================== Reset & Exit Button ===========================================================
btnReset = Button(bottomLeftBottomR, pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Reset",
                  bg="white", command=Reset).grid(row=6, column=0)
btnExit = Button(bottomLeftBottomR, pady=8, bd=2, fg="black", font=('arial', 16, 'bold'), width=13, text="Exit",
                 bg="white", command=iExit).grid(row=6, column=1)

# ==================================== Receipt Generation ===========================================================
lblReceipt = Label(bottomRight, font=('arial', 16, 'bold'), text="Receipt:", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(bottomRight, font=('arial', 11, 'bold'), width=46, bd=8, bg="white")
txtReceipt.grid(row=1, column=0)

root.mainloop()
