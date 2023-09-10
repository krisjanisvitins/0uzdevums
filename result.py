def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    t=d.strip()
    r=t.replace("$","")
    result=float(r)
    return(result)

def percent_to_float(p):
    a=p.strip()
    b=a.replace("%","")
    c=int(b)/100
    result=float(c)
    return(result)
main()
