import requests
page = requests.get("https://www.sme.sk")
#print(page.text)
brutal_string = page.text
is_in_tag = False
for i in brutal_string:
    if i=="<":
        is_in_tag = True
    
        print(i, end="")   
    if i==">":
        is_in_tag = False
        print(i, end="")
