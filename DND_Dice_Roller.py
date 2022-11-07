import random

while True:
   
 
 crit = int(input("you want 1. normal roll, 2. critical roll, 3. Advantage/Disadvantage roll, 4. to end program:  "))
 if crit != 4 and crit != 3:
   x = input("Enter which type of die you want to use (d4, d6, d8, d10, d12, d20, dp, or n to close program) : ")   
   if crit == 1:
     if x == "d4":  
       y = int(input("enter the number of die you need to roll: "))
       z = int(input("Enter your skill/ability mod if any: "))
       b = 0
       for j in range(y):
         a = random.randint(1,4)
         print(a)
         b += a
       b += z
    
       if b <= 0:
         print(1)
    
       else :  
         print(b) 
   
     if x =="d6":
       y = int(input("enter the number of die you need to roll: "))
       z = int(input("Enter your skill/ability mod if any: "))
       b = 0
       for j in range(y):
         a = random.randint(1,6)
         print(a)
         b += a
       b += z
    
       if b <= 0:
        print(1)
    
       else :  
        print(b)
 
     if x == "d8":
       y = int(input("enter the number of die you need to roll: "))
       z = int(input("Enter your skill/ability mod if any: "))
       b = 0
       for j in range(y):
         a = random.randint(1,8)
         print(a)
         b += a
       b += z
    
       if b <= 0:
         print(1)
    
       else :  
         print(b)
 
     if x == "d10":
       y = int(input("enter the number of die you need to roll: "))
       z = int(input("Enter your skill/ability mod if any: "))
       b = 0
       for j in range(y):
         a = random.randint(1,10)
         print(a)
         b += a
       b += z
    
       if b <= 0:
         print(1)
    
       else :  
         print(b)
 
     if x == "d12":
       y = int(input("enter the number of die you need to roll: "))
       z = int(input("Enter your skill/ability mod if any: "))
       b = 0
       for j in range(y):
         a = random.randint(1,12)
         print(a)
         b += a
       b += z
    
       if b <= 0:
         print(1)
    
       else :  
         print(b)
  
     if x == "d20":
       y = int(input("enter the number of die you need to roll: "))
       z = int(input("Enter your skill/ability mod if any: "))
       b = 0
       for j in range(y):
         a = random.randint(1,20)
         print(a)
         b += a
       b += z
    
       if b <= 0:
         print(1)
    
       else :  
         print(b)
 
     if x == "dp":
       y = int(input("enter the number of die you need to roll: "))
       z = int(input("Enter your skill/ability mod if any: "))
       b = 0
       for j in range(y):
         a = random.randint(1,10)*10
         print(a)
         b += a
       b += z
    
       if b <= 0:
         print(1)
    
       else :  
         print(b)
   if crit == 2:
       if x == "d4":  
         y = int(input("enter the number of die you need to roll: "))
         z = int(input("Enter your skill/ability mod if any: "))
         b = 0
         for i in range(2):
           for j in range(y):
             a = random.randint(1,4)
             print(a)
             b += a
         b += z
    
         if b <= 0:
           print(1)
    
         else :  
           print(b) 
   
       if x =="d6":
         y = int(input("enter the number of die you need to roll: "))
         z = int(input("Enter your skill/ability mod if any: "))
         b = 0
         for i in range(2):
           for j in range(y):
             a = random.randint(1,6)
             print(a)
             b += a
         b += z
    
         if b <= 0:
           print(1)
    
         else :  
           print(b)
 
       if x == "d8":
         y = int(input("enter the number of die you need to roll: "))
         z = int(input("Enter your skill/ability mod if any: "))
         b = 0
         for i in range(2):
           for j in range(y):
             a = random.randint(1,8)
             print(a)
             b += a
         b += z
    
         if b <= 0:
           print(1)
    
         else :  
           print(b)
 
       if x == "d10":
         y = int(input("enter the number of die you need to roll: "))
         z = int(input("Enter your skill/ability mod if any: "))
         b = 0
         for i in range (2):
           for j in range(y):
             a = random.randint(1,10)
             print(a)
             b += a
         b += z
    
         if b <= 0:
           print(1)
    
         else :  
           print(b)
 
       if x == "d12":
         y = int(input("enter the number of die you need to roll: "))
         z = int(input("Enter your skill/ability mod if any: "))
         b = 0
         for i in range(2):
           for j in range(y):
             a = random.randint(1,12)
             print(a)
             b += a
         b += z
    
         if b <= 0:
           print(1)
    
         else :  
           print(b)
  
       if x == "d20":
         y = int(input("enter the number of die you need to roll: "))
         z = int(input("Enter your skill/ability mod if any: "))
         b = 0
         for i in range(2):
           for j in range(y):
             a = random.randint(1,20)
             print(a)
             b += a
         b += z
    
         if b <= 0:
           print(1)
    
         else :  
           print(b)
 
       if x == "dp":
         y = int(input("enter the number of die you need to roll: "))
         z = int(input("Enter your skill/ability mod if any: "))
         b = 0
         for i in range(2):
           for j in range(y):
             a = random.randint(1,10)*10
             print(a)
             b += a
         b += z
    
         if b <= 0:
           print(1)
    
         else :  
           print(b)
 if  crit != 4 and crit == 3:
   ad = int(input("what would you like to roll: 1. for advantage, 2. for disadvantage:"))
   if ad == 1:
      mod = int(input("enter ability/skill modifier if any: "))
      mod_count = mod
      a_arr = []
      
      for i in range(2):
       adv = random.randint(1,20)
       adv += mod_count
       a_arr.insert(i,adv)
      
      if a_arr[0] >= a_arr[1]:
        print(str(a_arr[0])+" is the largest")
      
      
      elif a_arr[0] < a_arr[1]:
        print(str(a_arr[1])+" is the largest")
   if ad == 2:
     mod = int(input("enter ability/skill modifier if any: "))
     mod_count = mod
     a_arr = []
      
     for i in range(2):
       adv = random.randint(1,20)
       adv += mod_count
       a_arr.insert(i,adv)
      
     if a_arr[0] >= a_arr[1]:
        print(str(a_arr[1])+" is the smallest")
      
      
     elif a_arr[0] < a_arr[1]:
        print(str(a_arr[0])+" is the smallest")       
    
 if crit == 4:
    break