import csv

def crearCSVUsuarios(lista, nombreArchivo):
    
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Nombre', 'Contrasena', 'Edad'])
        writer.writerows(lista)
        
def crearCsvRefrigerio(lista, nombreArchivo):
    
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Tipo', 'Nombre', 'Precio'])
        writer.writerows(lista)