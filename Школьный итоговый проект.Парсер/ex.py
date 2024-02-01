from openpyxl import Workbook
from parcourse import getCourse,day,time
# Открываем Excel-файл
workbook = Workbook()


# Получаем активный лист
sheet = workbook.active

# Добавляем заголовки
#sheet.append(['День', 'Время',"Валюта","Курс к рублю"])

# Добавляем данные
#sheet.append([getCourse('R01215'),'рублей за 1 Датскую крону'])
sheet.append(['Курс к рублю',"Валюта","Дата","Время"])
sheet.append([getCourse('R01235'), 'доллар',day,time])
sheet.append([getCourse('R01239'),'евро',day,time])
sheet.append([getCourse('R01375') , 'юань',day,time])
sheet.append([getCourse('R01215') , 'крона',day,time])
sheet.append([getCourse('R01700J') , 'лира ',day,time])
sheet.append([getCourse('R01775') , 'франк',day,time])
sheet.append([getCourse('R01805F'),'динар ',day,time])
sheet.append([getCourse('R01820') ,'иен',day,time])
workbook.save('course.xlsx')
workbook.close()

