#deklarasi variable

var_nilai = 0
var_i = 1 

#perulangan WHILE
while (var_nilai<10):
    print("perulangan pertama ke ",var_nilai)
    while(var_i < 3):
        print("perulangan ke ",var_nilai,",",var_i)
        var_i +=1

#diluar perulangan var_i 
    var_i = 1
    var_nilai +=1

#diluar_perulangan var_nilai
print("var_nilai =", int(var_nilai)," = 10. bernilai false")