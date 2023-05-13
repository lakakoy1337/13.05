import glob
import os
import csv
import time


#вывод всех директорий и поддиректорий
def print_docs(directory):
    files = glob.glob(directory + '/**', recursive=True)
    for file in files:
        if not os.path.isdir(file):
            print(file)

directory_path = "C:\\Program Files"
print_docs(directory_path)
input('Нажмити клавишу для некст задания')

# 2
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        slova1 = []
        while True:
            line = f.readline()
            if not line:
                break
            slova1 += line.split()
        print('цикл 1', slova1)

        maxslovo = 0
        longest_slova = []
        for slovO in slova1:
            if len(slovO) > maxslovo:
                maxslovo = len(slovO)
                longest_slova = [slovO]
            elif len(slovO) == maxslovo:
                longest_slova.append(slovO)
        print('цикл 2', maxslovo)

    return longest_slova


result = longest_words('article.txt')
print('Слова с наибольшей длиной:', result)
input('Нажмити клавишу для некст задания')

#3

with open('rows_300.csv', 'w', newline='') as file:
    zapis = csv.writer(file)
    zapis.writerow(['№', 'Секунда', 'Микросекунда'])
    for i in range(1, 301):
        vremya = time.time()
        secynda = int(vremya)
        microsecynda = int((vremya - secynda) * 1000000)
        zapis.writerow([i, secynda, microsecynda])
        time.sleep(0.01)
