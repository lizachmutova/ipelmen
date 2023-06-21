violator_songs = { 
    'World in My Eyes': 4.86, 
    'Sweetest Perfection': 4.43, 
    'Personal Jesus': 4.56, 
    'Halo': 4.9, 
    'Waiting for the Night': 6.07, 
    'Enjoy the Silence': 4.20, 
    'Policy of Truth': 4.76, 
    'Blue Dress':4.29, 
    'Clean': 5.83, 
    'Killer queen': 3.01,
    'Under Pressure' : 4.05,
    'Teeth' : 3.24,
    'Smells Like Teen Spirit' : 5.00
} 
 
summ = 0 
n = int(input("Сколько песен вы хотите прослушать? ")) 
for i in range(n): 
    name = input("Введите название  "+str(i+1)+" песни: ") 
    time = violator_songs[name] 
    summ = summ + time 
print("Общее время для прослушивания песен:",summ," минут")