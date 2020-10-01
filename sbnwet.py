import pandas as nikh
first = """These are the data of all people with their name and montly salary in rupees \n"""
print(first)
n = nikh.DataFrame({
    "Name":["Rishav","Akr","Zoya","Prachi","Pari","RTG","Aishwary","Deepa","Nikhat","Harry","Rahul","Piyush","aastha","jay","Anshika","Jasmine","Nakab posh","safalta","Rose","lamya","skr","Arshita","everyone"],
    "Monthly Income":[1000,2000000,3000000,4000000,5000000,600,1700,8000000,9000000,1000000,11000000,1200000,13000000,14000000,1500000,1600000,1700000,20000000,6000000,5000000,12000000,3900000,1800000]
    
})
print(n)
print("\nData Of Rich peoples 😁 -\n")
rich = n.loc[n["Monthly Income"] > 100000]
print(rich)
print("\nNon Rich peoples 😁 -\n")
non_rich = n.loc[n["Monthly Income"] < 100000]
print(non_rich)
