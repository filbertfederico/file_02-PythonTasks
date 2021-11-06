def convert_to_days():
    hours = eval(input("input hours:"))
    minutes = eval(input("input minutes:"))
    seconds = eval(input("input seconds:"))
    
    day = totaldays(hours, minutes, seconds)
    print(f"The number of days is: {day}")

def totaldays(hours: int , minutes: int, seconds: int):
    Days = ((seconds/3600) + (minutes/60) + hours)/24
    return round(Days,4)
convert_to_days() 