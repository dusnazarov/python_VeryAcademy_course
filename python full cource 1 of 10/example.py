# Strin types
# x = 'hello world'

# print(x.title())
# print(x.upper())

# y = 'HELLO WORLD'

# print(y.lower())


# //////////// Data Types ////////////

# x = float(1.1236547)
# y = int(1)

# check = isinstance(y, int)
# print(check)

# z = x+y
# print(z)

# //////////// format ////////////
# x = 1.45236547

# print(format(x, '.f'))


# //////////// forloop ////////
# x = {1:'a', 2:'b', 3:'c', 4:'d' }

# for i in x.values():
#     print(i) 

# //////////// forloop ////////
# x = {1:'a', 2:'b', 3:'c', 4:'d' }

# for i in x.items():
#     print(i) 

# //////////// forloop ////////

# x = {1:'a', 2:'b', 3:'c', 4:'d' }

# for a,b in x.items():
#     print(a,b) 

# //////////// forloop ////////

# for i in range(10, 0, -1):
#     print(i) 

# //////////// forloop ////////

# for i in range(0, 4):
#     x = input("Give me a number: ")

#     if x == '1':
#         print('You guessed right!')
#         break
#     else:
#         print('You failed')
# else:
#     print('end')

# //////////// forloop ////////

# x = (1, 2, 1, 4, 2, 1)

# for i in x:
#     if i == 1:
#         continue
#     print(i)

# //////////// forloop ////////

# x = (1, 2, 1, 4, 2, 1)

# for i in x:
#     print(i)
# else:
#     print("end")

# //////////// forloop ////////

a = (1, 1, 1, 1, 1, 1)
b = (2, 2, 2, 2, 2, 2)

for x in a:
    print(x)
    for y in b:
        print(x, y)




# # //////////// function ////////////

# def get_bill_total():
#     bill_total = float(input("Enter the total: "))
#     return bill_total

# def main():  
#     total = get_bill_total()
#     discount = total - total / 100 * 10
#     final_price = format(discount, '.2f')
#     print(f"Final Price is {final_price}")
    
# main()
        
# //////////// function ////////////

# def claculate_discount(total):
#     dicount = total -total / 100 *10
#     return dicount

# def get_bill_total():
#     bill_total = float(input("Enter the total: "))
#     final_total = format(claculate_discount(bill_total), '.2f')
#     return  final_total

# def main():  
#     total = get_bill_total()    
#     print(f"Final Price is {total}")
    
# main()
        
        




