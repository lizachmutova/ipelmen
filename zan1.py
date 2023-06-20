#считать сколько символов в строке
#N**2 - плохая сложность
def strcounter(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter +=1
        print(sym,counter)
#strcounter('aaaabbbbccd')


#M*N
def strcounter_2(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter +=1
        print(sym,counter)
#strcounter_2('aaaabbbbccd')

#N-лучшая сложность
def strcounter_3(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1
    for sym,count in syms_counter.items():
        print(sym,count)
strcounter_3('aaaabbbbccd')   
# от сложности зависит как быстро будет работать программаю.если код или файл очень большой то отрывок с плохой сложностью может не сработать
#отрывок считается плохой сложности если в нем есть цикл в цикле.если просто несколько циклов то скорость хорошая
