veg=['onion','carrot','beetroot','cucumber','potato','tomato','greenchilli']
quantity=[30,15,20,10,25,35,40]
sellingprice=[30,35,45,25,50,40,55]
costprice=[20,30,35,15,25,31,45]
original_qty=quantity.copy()
password='12345'
totalrevenue=[]
cdetails=[]
sold_qty=[0]*len(veg)
shop_open=True
while shop_open:
    print("1.owner view")
    print("2.customer view")
    print("3.exit")
    option=input("choose one option(1/2/3):")
    #----------owner view--------------------------
    if option=='1':
        while True:
            name=input("enter your name:")
            if name.isalpha():
                pswrd=input("enter your password:")
                if pswrd==password and pswrd.isdigit():
                    print("login is successful!")
                    break
                else:
                    print("wrong password.Try again")
            else:
                print("enter valid name")
            
        while True:
            print("===="*15)
            print("==============owner view=================")
            print("1.view menu")
            print("2.add items")
            print("3.remove items")
            print("4.update items")
            print("5.view customer details")
            print("6.itemized profit")
            print("7.exit")
            print("===="*15)
            option2=input("choose one option(1/2/3/4/5/6/7):")
            if option2=='1':
                #viewing menu
                print("-"*10,"Welcome To Menu","-"*10)
                print("ITEMS".ljust(15),"QUANTITY".ljust(15),"COSTPRICE".ljust(15),"SELLINGPRICE".ljust(15))
                for v,q,c,s in zip(veg,quantity,costprice,sellingprice):
                    print(v.ljust(15),str(q).ljust(15),str(c).ljust(15),str(s).ljust(15))
            elif option2=='2':
                #Adding items to inventory
                while True:
                    item=input("do you want to add a vegetable(or done):")
                    if item=='done':
                        print('Return to menu....')
                        break
                    elif item in veg:
                            print(item,"is already exists")
                    else:
                        qty=int(input("how many kgs do you want to add:"))
                        cprice=int(input("enter costprice:"))
                        sprice=int(input("enter sellingprice:"))
                        veg.append(item)
                        quantity.append(qty)
                        sellingprice.append(sprice)
                        costprice.append(cprice)
                        print("-"*10,"item is added successfully","-"*10)        
            elif option2=='3':
                #Removing item from inventory
                while True:
                        item = input("enter vegetable name to remove(or done): ")
                        if item=="done":
                            print("return to menu...")
                            break
                        elif item in veg:
                            index = veg.index(item)   # Get the index of the item
                            # Remove all related values using index
                            veg.pop(index)
                            quantity.pop(index)
                            sellingprice.pop(index)
                            costprice.pop(index)
                            print("*" * 10, "Item is removed from menu", "*" * 10)
                            print("-----" * 10)
                        else:
                            print("Item not found in veg")
                            print("===" * 15)
            elif option2=='4':
                #Updating item in inventory
                while True:
                        item=input("enter vegetable name to modify(or done):")
                        if item=="done":
                            print("return to menu...")
                            break
                        elif item in veg:
                            index=veg.index(item)
                            qty=input("Do you want to add or reduce(add/reduce):").lower()
                            if qty=='add':
                                add_qty=int(input('Enter quantity to add:'))
                                quantity[index]+=add_qty
                                print('stock added successfully')
                            elif qty=='reduce':
                                reduce_qty=int(input('Enter quantity to reduce:'))
                                if reduce_qty<=quantity[index]:
                                    quantity[index]-=reduce_qty
                                    print('Stock reduce successfully')
                                else:
                                    print('Not enough stock')
                            else:
                                print('invalid stock')
                            cprice=int(input("update costprice:"))
                            sprice=int(input("update sellingprice:"))
                            sellingprice[index]=sprice
                            costprice[index]=cprice
                            print("*"*10,"item is updated succefully","*"*10)
                            print("==="*15)
                        else:
                            print("item not found in menu")
                            print("===="*15)
            elif option2=='5':
                #Viewing Customer Details
                print("........customer details..........")
                if not cdetails:
                    print("no customer is recorded")
                else:
                    print("NAME".ljust(15),"PHONE-NUMBER".ljust(15),"BILL".ljust(15))
                    for view in cdetails:
                        print(str(view[0]).ljust(15),str(view[1]).ljust(15),str(view[2]).ljust(15))
                
            elif option2=='6':
                #View Report Itemized Profit
                
                totalprofit=0
                any_sale=False
                print("ITEMS".ljust(15),"SOLD_QTY".ljust(15),"PROFIT".ljust(15))
                for v,sold,oq,sp,cp in zip(veg,sold_qty,original_qty,sellingprice,costprice):
                   #sold=oq-sq
                    if sold>0:
                        any_sale=True
                        profit=(sp-cp)*sold
                        totalprofit+=profit
                        print(v.ljust(15),str(sold).ljust(15),str(profit).ljust(15))
                print("-"*20)
                if not any_sale:
                    print('No sales  recorded today')
                print("TOTAL PROFIT=",totalprofit)
                #Final Inventory
                print("=========================FINAL INVENTORY STATUS=======================")
                print("ITEM".ljust(15),"REMAINING_QTY".ljust(15))
                for item,qty in zip(veg,quantity):
                    print(item.ljust(15),str(qty).ljust(15))
                print("=============="*5)
                print("---"*10,"TOTAL REVENUE","---"*10)
                if not cdetails:
                    print("no sales recorded today")
                else:
                    total_revenue=0
                    for customer in cdetails:
                        total_revenue+=customer[2]
                    print("TOTAL REVENUE:",total_revenue)
                    

                print("*"*15,"shop is closed","*"*15)
                shop_open=False
                break
            elif option2=='7':
                #exiting
                print("......exiting......")
                break
            else:
                print("enter valid option")
                break
    #------------------------customer view---------------------------------
    elif option=='2':
        cart_item=[]
        cart_qty=[]
        cart_price=[]
        while True:
            print("---"*10,"customer view","---"*10)
            print("1.VIEW MENU")
            print("2.ADD ITEMS TO CART")
            print("3.REMOVE ITEMS FROM CART")
            print("4.UPDATE ITEMS IN CART")
            print("5.VIEW CART")
            print("6.BILLING")
            print("7.EXIT")
            option3=input("choose one option(1/2/3/4/5/6/7):")
            cname=[]
            cphone=[]
            ccity=[]
            cbill=[]
            if option3=='1':
                #viewing menu
                print("*"*10,"welcome to menu","*"*10)
                print("Items".ljust(15),"AVAILABLE-QTY".ljust(15),"PRICE/KG".ljust(15))
                for v,q,p in zip(veg,quantity,sellingprice):
                    print(v.ljust(15),str(q).ljust(15),str(p).ljust(15))
            elif option3=='2':
                #adding items to cart
                print("*"*15,"ADD ITEMS","*"*15)
                while True:
                    item=input("enter vegetable name(done):").lower()
                    if item=='done':
                        break
                    else:
                        if item in cart_item:
                            print(item,"already exists in cart")
                        else:
                            if item in veg:
                                idx=veg.index(item)
                                qty=float(input("enter quantity:"))
                                if qty<=quantity[idx]:
                                    cart_item.append(item)
                                    cart_qty.append(qty)
                                    cart_price.append(sellingprice[idx])
                                    quantity[idx]-=qty
                                    print("item is added to cart")
                                else:
                                    print("out of stock")
                            else:
                                print("item not found")
            elif option3=='3':
                if not cart_item:
                    print("your cart is empty.Add items first.")
                    continue
                #removing items from cart
                print("*"*15,"REMOVE ITEMS","*"*15)
                item=input("enter vegetable name to remove(done):").lower()
                if item=='done':
                    break
                else:
                    if item in cart_item:
                        idx=cart_item.index(item)
                        quantity[veg.index(item)]+=cart_qty[idx]
                        cart_item.pop(idx)
                        cart_qty.pop(idx)
                        cart_price.pop(idx)
                        print("Item removed successfully")
                    else:
                        print("Item not in cart")
            elif option3=='4':
                if not cart_item:
                    print("your cart is empty.Add items first.")
                    continue
                #updating/modifying items in cart
                print("*"*15,"UPDATE ITEMS","*"*15)
                item=input("enter vegetable name(done):").lower()
                if item=='done':
                    break
                else:
                    if item in cart_item:
                        idx=cart_item.index(item)
                        veg_index=veg.index(item)
                        new_qty=input("do you want to add or reduce(add/reduce):").lower()
                        if new_qty=='add':
                            add_qty=int(input('Enter quantity to add:'))
                            if add_qty<=quantity[veg_index]:
                                cart_qty[idx]+=add_qty
                                quantity[veg_index]-=add_qty
                                print('Quantity is added to stock')
                            else:
                                print('Not enough stock')
                        elif new_qty=='reduce':
                            reduce_qty=int(input('Enter quantity to reduce:'))
                            if reduce_qty<cart_qty[idx]:
                                cart_qty[idx]-=reduce_qty
                                quantity[veg_index]+=reduce_qty
                                print('Quantity reduce sucessfully')
                            elif reduce_qty==cart_qty[idx]:
                                #remove totally
                                quantity[veg_index]+=cart_qty[idx]
                                cart_item.pop(idx)
                                cart_qty.pop(idx)
                                print('Item removed from cart')
                            else:
                                print('cannot reduce more than cart')
                        else:
                            print('Item not in cart')             
            elif option3=='5':
                #viewing cart
                print("===="*10,"customer cart","==="*10)
                print("ITEMS".ljust(15),"QUANTITY".ljust(15),"PRICE".ljust(15))
                total=0
                for i,q,p in zip(cart_item,cart_qty,cart_price):
                    amt = q * p
                    total += amt
                    print(i.ljust(15),str(q).ljust(15),str(p).ljust(15))
                print("*"*35)
                print("TOTAL =",total)   
            elif option3=='6':
                if not cart_item:
                    print("cart is empty.please add items before billing.")
                    continue
                #billing
                print("*"*15,"BILLING","*"*15)
                while True:
                    name=input("enter customer name:")
                    if name.isalpha():
                        while True:
                            phone=input("enter phone number:")
                            #checking phone number is digits and lenght is equal to 10 and starts with 9,7,6,8
                            if phone.isdigit() and len(phone)==10 and phone[0] in ['9','7','6','8']:
                                cname.append(name)
                                cphone.append(phone)
                                break
                            else:
                                print("invalid number")
                        break
                    else:
                      print("invalid name")
                total=0
                print("==="*10,"BILL","==="*10)
                print("ITEMS".ljust(15),"QUANTITY".ljust(15),"PRICE".ljust(15),"AMOUNT".ljust(15))
                for i,q in zip(cart_item,cart_qty):
                    price=sellingprice[veg.index(i)]
                    amt = q * price
                    total += amt
                    print(i.ljust(15),str(q).ljust(15),str(price).ljust(15),str(amt).ljust(15))
                print("***********"*5)
                print("TOTAL BILL=",total)
                if total==0:
                    print("you did not buy any item")
                    break
                print("***********"*5)
                #payment method
                while True:
                        method=input('Select payment method(cash/card/phonepay):').lower()
                        if method=='cash':
                            print("==="*10,"PAYMENT SUCCESSFULL","==="*10)
                            break
                        elif method=='card':
                            while True:
                                pin=input("enter pin:")
                                if pin.isdigit() and 4<=len(pin)<=6:
                                    print("================PAYMENT SUCCESSFULLY==============")
                                    break
                                else:
                                    print("Invalid pin")
                            break
                        elif method=='phonepay':
                            print('$$$$$$$$$')
                            print('$$$$$$$$$')
                            print('$$$$$$$$$')
                            print('$$$$$$$$$')
                            print('$$$$$$$$$')
                            print('==================PAYMENT SUCCESSFULLY=================')
                            break
                else:
                    print("choose correct payment method")
                for i,q in zip(cart_item,cart_qty):
                    sold_qty[veg.index(i)]+=q
                cdetails.append([name,phone,total])

                cart_item.clear()
                cart_qty.clear()
                cart_price.clear()
                print("THANK YOU FOR SHOPPING")
                print("="*25)
            elif option3=='7':
                #exiting
                print("thank you!visit again")
                print("="*20)
                break
            else:
                print("invalid option")
    
    else:
        print("THANK YOU")
        break
                    
                        
                    
                    
                        
                
    
       
