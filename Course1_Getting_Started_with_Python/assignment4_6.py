hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print('this is not numbers!')
    quit()

def computepay(h, r):
    if h <= 40 :
        regularPay = h * r
        overtimePay = 0
    else :
        regularPay = (h-(h-40)) * r
        overtimePay = (h-40) * (1.5*r)

    totalPay = regularPay + overtimePay
    return totalPay

p = computepay(h, r)
print("Pay", p)