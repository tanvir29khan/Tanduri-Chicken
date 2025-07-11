print("Enter your all 3 subjects marks")
sub1 = int(input("Enter your 1st subject marks: "))
sub2 = int(input("Enter your 2nd subject marks: "))
sub3 = int(input("Enter your 3rd subject marks: "))

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and (sub1+sub2+sub3) >= 120:
    print("You are pass")

else:
    if sub1 < 33:
        print("You are fail in 1st subject")
    if sub2 < 33:
        print("You are fail in 2nd subject")
    if sub3 < 33:
        print("You are fail in 3rd subject")

    print("You are fail in the exam")


