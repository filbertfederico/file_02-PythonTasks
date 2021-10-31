num = int(input("Enter the number: "))  
reverse_num = 0    

def prior_incantato(num):  
    global reverse_num   
    if (num > 0):  
        Reminder = num % 10  
        reverse_num = (reverse_num * 10) + Reminder  
        prior_incantato(num // 10)  
    return reverse_num  
reverse_num = prior_incantato(num)  

def PrimeChecker(a):  
    if a > 1:  
        for j in range(2, int(a/2) + 1):  
            if (a % j) == 0:  
                print("False")  
                break  
        else:  
            print(num,a)  
    else:  
        print(a, "False")   
a = reverse_num 
PrimeChecker(a)      
