hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h <= 40 :
    regularPay = h * r
    overtimePay = 0
else :
    regularPay = (h-(h-40)) * r
    overtimePay = (h-40) * (1.5*r)

totalPay = regularPay + overtimePay
print( totalPay )