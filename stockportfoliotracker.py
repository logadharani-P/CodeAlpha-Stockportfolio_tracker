n=int(input("Enter the number of stocks: "))
list=[]
for i in range(n):
    stock_name=input("Enter the stock name: ")
    shares=int(input("Enter the number of shares: "))
    price=float(input("Enter the price per share:"))
    total=shares*price
    
    print("Total value of stock",stock_name,"is",total)
    list.append(total)


add=sum(list)
print("Total value of the portfolio is: ",add)





