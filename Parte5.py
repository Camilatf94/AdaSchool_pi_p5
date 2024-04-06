# MAPA DEL LABERINTO #

# Librerias utilizadas en el proyecto
import os
from typing import List, Tuple
import readchar
from readchar import readkey, key

nombre = input('introduce tu nombre: ')
print('Bienvenido' + nombre + '!')



# Crear clase Juego #

class Juego:
    def __init__(self, laberinto, punto_inicial, punto_final):
        self.mapa = self.transformar_matriz(laberinto)
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def transformar_matriz(self, laberinto):
        filas = laberinto.split('\n')[1:] 
        matriz = [list(fila) for fila in filas]
        return matriz
    
    def mostrar_mapa(self, eje_x, eje_y):
        self.mapa[eje_x][eje_y] = 'P'
        self.vista_de_mapa()

    def mostrar_mapal(self):
        self.clear_terminal()
        for fila in self.mapa:
            print(''.join(fila))
    
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_loop(self):
        eje_x, eje_y = self.punto_inicial

        while (eje_x, eje_y) != self.punto_final:
            self.mostrar_mapa(eje_x, eje_y)

            pressed_key = readchar.readkey()
            nuevo_eje_x, nuevo_eje_y = eje_x, eje_y

            if pressed_key == key.UP and eje_x > 0 and self.mapa[eje_x - 1][eje_y] != '#':
                nuevo_eje_x -= 1
            elif pressed_key == key.DOWN and eje_x < len(self.mapa) - 1 and self.mapa[eje_x + 1][eje_y] != '#':
                nuevo_eje_x += 1
            elif pressed_key == key.LEFT and eje_y > 0 and self.mapa[eje_x][eje_y - 1] != '#':
                nuevo_eje_y -= 1
            elif pressed_key == key.RIGHT and eje_y < len(self.mapa[0]) - 1 and self.mapa[eje_x][eje_y + 1] != '#':
                nuevo_eje_y += 1

            self.mapa[eje_x][eje_y] = '.'
            eje_x, eje_y = nuevo_eje_x, nuevo_eje_y

        self.mostrar_mapa(eje_x, eje_y)

# Clase heredada para la adición de nuevas funcionalidades al juego
class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa_aleatorio, punto_inicial, punto_final = self.elegir_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa_aleatorio, punto_inicial, punto_final)
    
    def elegir_mapa_aleatorio(self, path_a_mapas):
        archivos_de_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_de_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido_mapa = archivo.read()

        # Leer datos de inicio y fin desde la primera fila
        primer_fila = contenido_mapa.strip().split('\n')[0]
        puntos = list(map(int, primer_fila.split()))
        
        punto_inicial = (puntos[0], puntos[1])
        punto_final = (puntos[2], puntos[3])

        return contenido_mapa.strip(), punto_inicial, punto_final
    
    def ejecutar(self):
        self.main_loop()



print('Bienvenido al juego del laberinto.')
name_user = input('Ingrese su nombre: ')
print(f'{name_user} el juego está por comenzar, prepárate.')
input('Enter para comenzar...')

# Instancia mapas aleatorios
path_a_mapas = os.path.join(os.path.dirname(__file__), 'mapas')
juego_archivo = JuegoArchivo(path_a_mapas)

# Ejecucion del juego
juego_archivo.ejecutar()

mensaje_final = 'Felicidades'
print(mensaje_final)

