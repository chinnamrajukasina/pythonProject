def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)


person("Raju", age=27, blood_groop="B+", place="india", planet="earth")
