def ratio():
    m = eval(input("Enter the current width:"))
    n = eval(input("Enter the current height:"))
    z = eval(input("Enter the desired width:"))
    x = calc_new_height(m,n,z)
    print("The corresponding height is:",x)
    
def calc_new_height (m, n, z):
    ratio = m/n
    x = z/ratio
    return(x)
ratio()


