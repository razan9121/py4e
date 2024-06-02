score = input("Enter Score: ")
try:
    s = float(score)
except:
    print('this is not number!')
    quit()

if 0.0 <= s <= 1.0:
    if s >= 0.9:
        grade='A'
    elif s >= 0.8:
        grade='B'
    elif s >= 0.7:
        grade='C'
    elif s >= 0.6:
        grade='D'
    else:
        grade='F'
    print(grade)
else:
    print('error! a score must be between 0.0 and 1.0.')