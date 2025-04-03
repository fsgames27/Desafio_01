h1 = int(input("Horas 1: "))
m1 = int(input("minutos 1: "))
h2 = int(input("Horas 2: "))
m2 = int(input("minutos 2: "))
print(f"Entrada 1: {h1}:{m1}")
print(f"Entrada 2: {h2}:{m2}")
mf = m1 + m2

if h1 > 12:
    h1 -= 12
if h2 > 12:
    h2 -= 12
hf = h1 +h2
if mf >= 60:
    hf += 1
    mf -= 60

if hf >= 12:
    hff = hf - 12
    print(f"saída: {hff}:{mf}")
else:
    print(f"saída: {hf}:{mf}")


