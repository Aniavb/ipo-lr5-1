string = str(input('Введите строку: ')) #приглашение для ввода строки
b = len(string)  #определение длинсы строки
vowels = "аАоОиИуУэЭюЮяЯеЕёЁыЫ"  #переменная для гласных букв
consonats= "вВгГдДжЖзЗкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩъЪьЬ"  #переменная для согласных букв
count=0 #начало счётчика для гласных
count1=0   #начало счётчика для согласных
for i in string:   #цикл для перебора элементов в переменной string
    for c in vowels:   #цикл для перебора элементов в переменной vowels
         if c in i:    #если есть  элементы с в i
              count += 1  #увеличиваем счётчик на один
    for f in consonats:  #цикл для перебора элементов в consonats
         if f in i:    #если есть элементы f в i
              count1+=1   #увеличиваем счётчик на один      
print("Длина строки: ", b)   #выводим переменную b
print("Количество гласных: ", count)  #выводим переменную count
print("Количество согласных: ", count1)  #выводим переменную count1
