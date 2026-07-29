import json

# Caminho do arquivo person.json
file_path = 'person.json'

# Lendo o conteúdo do arquivo JSON
with open(file_path, 'r') as file:
    person_data = json.load(file)

# Imprimindo o conteúdo do arquivo
print(person_data)