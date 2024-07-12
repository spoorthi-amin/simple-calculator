print("simple calculator")
print('select an operation')
print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.division')
while True:
        
              operation=int(input('enter choice(1/2/3/4) >>     '))
    
              num1=float(input('enter num1>>     '))
              num2=float(input('enter num2>>  '))           
              if operation==1:
                  print(num1+num2)
              elif operation==2:
                  print(num1-num2)
              elif operation==3:
                    print(num1*num2)
              elif operation==4:
                    print(num1/num2) 
              else:
                   print('invalid choice plz try once again')    

