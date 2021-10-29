"""Programma per anonimizzare un file di log (29.10.21)"""

import json

"Apro il file json da anonimizzare e associo una lista che contiene tutti i log del file"
fin = open(r"C:\Users\massi\OneDrive\Documenti\GitHub\ProgrammazioneUBCM\programmazioneUCBM\indata\anonimizza_test1.json")
log_list = json.load(fin)
fin.close()
log_list=log_list[0]
"Per testrae stampo il primo log"
print(log_list[0])

"Anonimizzo i log assegnando un codice progressivo ad ogni nome utente(campo 1 del log)"
code_tab={}
code = 1
for log in log_list:
    if not log[1] in code_tab:
        code_tab[log[1]] = str(code)
        code +=1
"Sostituisco il nome (campo 1) con il codice ed elimino con la funzione pop il secondo elemento"
for i, log in enumerate(log_list):
    log[1]=code_tab[log[1]]
    log_list[i].pop(2)

"Creo un nuovo file json per contenere il risultato"    
fout= open(r"C:\Users\massi\OneDrive\Documenti\GitHub\ProgrammazioneUBCM\programmazioneUCBM\indata\log_anonimizzati.json", "w")
json.dump(log_list, fout, indent=2)
fout.close()