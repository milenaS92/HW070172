# This is a test

dict = {}

with open('Mi_biblioteca.bib', 'r', encoding = 'utf8') as file1:
    record_list = file1.read().split("\n@")

    for record in record_list[1:10]:
        if ".pdf" in record.lower():
            record = record.strip()
            record = record.split("\n")[:-1] #??
            print(record)
    print(len(record_list))
