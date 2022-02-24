# https://hu.wikipedia.org/wiki/Boldog_sz%C3%A1m
# Boldog szám az a pozitív egész szám, amelyre igaz, hogy ha kiszámítjuk számjegyeinek négyzetösszegét, majd ezt az így kapott számmal szükség szerint addig ismételjük, amíg egyjegyű számot nem kapunk, akkor az eredmény 1 lesz.
#
# Például boldog szám a 23, mert 2²+3²=4+9=13, 1²+3²=1+9=10, 1²+0²=1+0=1.
#
# Azt a számot, amelynél a folyamat végeredménye nem 1, boldogtalan számnak nevezzük.

# 1. Döntse el egy számról, hogy boldog-e. Bement a szám, kimenet pedig logikai érték.
#
# 2. Keresse boldog számokat egy paraméterként megadott tartományban.
#
# 3. Minden boldog szám esetében a számítás eredményeként megkapott összes szám boldog, amíg el nem érjük az 1-et.
#    Készítsen adatszerkezetet a boldog számok gráfjának a tárolására, és fűzze fel a keresett számokat.

# 4. A boldog számok keresését gyorsítsa meg úgy, hogy a korábbi keresési eredményeket felhasználja.
