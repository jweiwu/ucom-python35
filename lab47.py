file1 = open('.\\data\\PythonIntroduction', encoding='utf8')
readme_txt1 = file1.read()
print(readme_txt1)
file1.close()

with open('.\\data\\clone', 'w', encoding='utf8') as file2:
    file2.write(readme_txt1)
