from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios

crearCSVUsuarios(usuarios, 'bdUsuarios.csv')