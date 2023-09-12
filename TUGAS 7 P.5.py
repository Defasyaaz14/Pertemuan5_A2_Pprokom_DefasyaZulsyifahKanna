#deklarasi variable

var_nilai = 0
var_i = 1 

#perulangan FOR
for var_nilai in range (0,10):
    print("perulangan pertama ke ",var_nilai)
    while(var_i < 3):
        print("perulangan ke ",var_nilai,",",var_i)
        var_i+=1

#diluar perulangan var_i 
    var_i = 1

#diluar_perulangan var_nilai
print("var_nilai =", int(var_nilai)," = 10. bernilai false")