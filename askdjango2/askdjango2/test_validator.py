

import re

val ="01088059492"
#01 [] 그리고 내번호는 [1-9]6번나타남
pattern = r"^01[016789][1-9]\d{6}$"   


if re.match(pattern , val):
    print("matched")
else:
    print("valid")

