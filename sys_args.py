import sys

list_dict = [{'nome': 'Ana', 'cpf': '1000'}, {'nome': 'João', 'cpf': '7770'}]
app_item = eval(sys.argv[1].replace("\"", ""))

list_dict.append(app_item) 

print(list_dict)