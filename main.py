list = ["create acc","deposit","withdraw","show balance", "exit"]
print(list)
choose_action = input("airchiet moqmedeba: ")
# აქაუნთის შექმნა
if choose_action == "create acc":
    createacc_username = input("sheiyvanet Momxareblis saxeli: ")
    createacc_password = input("sheiyvanet momxmareblis paroli: ")
    print("აქაუნთი წარმატებით შეიქმნა: ")
else:
    print("აქაუნთი არ არის შექმნილი : ")

# deposit
list = ["create acc","deposit","withdraw","show balance", "exit"]
print(list)
choose_action = input("airchiet moqmedeba: ")
account_balance = 0
important_info1 = input("შეიყვანეთ მომხმარებლის სახელი:")
important_info2 = input("შეიყვანეთ მომხმარებლის პაროლი: ")
if important_info1 != createacc_username or important_info2 != createacc_password:
    print("მომხმარებელი მსგავსი მონაცემებით ვერ მოიძებნა")
elif important_info1 == createacc_username and important_info2 == createacc_password:
    print("იდენტობა წარმატებით დადგინდა გთხოვთ შეიყვანოთ შესატანი თანხა")
deposit_money = int(input("შეიყვანეთ შესატანი თანხა "))
if deposit_money == 0:
    print("შეყვანილი თანხა არის 0 გთხოვთ შეიყვანოთ სწორი თანხა")
else:
      updated_balance = account_balance + deposit_money
print("ბალანსი წარმატებით განახლდა და შეადგენს" + " " + str(updated_balance) + " " + "ლარს")

# withdraw 
updated_balance = account_balance + deposit_money
list = ["create acc","deposit","withdraw","show balance", "exit"]
print(list)
choose_action = input("airchiet moqmedeba: ")
important_info1 = input("შეიყვანეთ მომხმარებლის სახელი:")
important_info2 = input("შეიყვანეთ მომხმარებლის პაროლი: ")
if important_info1 != createacc_username or important_info2 != createacc_password:
    print("მომხმარებელი მსგავსი მონაცემებით ვერ მოიძებნა")
elif important_info1 == createacc_username and important_info2 == createacc_password:
    print("იდენტობა წარმატებით დადგინდა გთხოვთ შეიყვანოთ გამოსატანი თანხა")
withdraw_money = int(input("შეიყვანეთ გამოსატანი თანხა"))
if withdraw_money > updated_balance:
    print("ანგარიშზე საკმარისი თანხა არ არის")
elif withdraw_money == 0:
    print("შეყვანილი გამოსატანი თანხა 0 ლარია და განაღდება შეუძლებელია")
else:
    updated_balance = account_balance + deposit_money - withdraw_money
    print("განაღდება წარმატებით შესრულდა და ბალანსი შეადგენს" +  " " +  str(updated_balance))

# show balance 
