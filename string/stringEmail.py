email = "cka@kj.com"
condition="@."
valid=0
for ch in email:
    if ch in condition:
        valid += 1
   
if valid==2:
    print("Email is Valid.","Email is:", email)
else:
    print("Email is not Valid.")