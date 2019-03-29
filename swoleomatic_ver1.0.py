unit = input ("kg o lb?\n")
valori_ok = ['kg','lb']
while unit not in valori_ok:
    unit = (input ('inserisci "kg" o "lb"\n'))
if unit=="kg":
    i="i"
else:
    i="e"

lift_a = str(input ("inserisci il primo esercizio\n"))
while True:
    peso_a = (input ("quant{:s} {:s} sollevi?\n".format(i,unit)))
    try:
        peso_a = int(peso_a)
        break
    except:
        print("per favore, inserisci un valore numerico")
while True:
    reps_a = (input ("per quante reps?\n"))
    try:
        reps_a = int(reps_a)
        break
    except:
        print("per favore, inserisci un valore numerico")
maxrep_a = (float(peso_a) / (1.0278 - (0.0278 * float(reps_a))))
print ("il tuo massimale di", lift_a, "è", round(maxrep_a,1),"{:s}s".format(unit))

lift_b = str(input ('\ninserisci il secondo esercizio\n'))
while True:
    peso_b = (input ("quant{:s} {:s} sollevi?\n".format(i,unit)))
    try:
        peso_b = int(peso_b)
        break
    except:
        print("per favore, inserisci un valore numerico")
while True:
    reps_b = (input ("per quante reps?\n"))
    try:
        reps_b = int(reps_b)
        break
    except:
        print("per favore, inserisci un valore numerico")
maxrep_b = (float(peso_b) / (1.0278 - (0.0278 * float(reps_b))))
print ("il tuo massimale di", lift_b, "è", round(maxrep_b,1),"{:s}s".format(unit))
