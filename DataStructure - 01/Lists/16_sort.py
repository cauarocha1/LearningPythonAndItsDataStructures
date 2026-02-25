#sort: sort a list in different ways, alphabetic, reverse alphabetic, by number of caracters..
languages = ["python", "js", "c", "java", "csharp"]
languages.sort()  # ["c", "csharp", "java", "js", "python"]
print(languages)

languages = ["python", "js", "c", "java", "csharp"]
languages.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(languages)

languages = ["python", "js", "c", "java", "csharp"]
languages.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(languages)

languages = ["python", "js", "c", "java", "csharp"]
languages.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(languages)