import random
from random import randint
from texttable import Texttable
from pyfiglet import Figlet


myz = Figlet(font='graffiti')
print(myz.renderText("MYZDice\nRoller"))

print("*------------------------------------------------------*")
print("|     MYZ Dice Roller by EledunGM beta  0.6 - 2019     |")
print("|            Comments: ilgabo@gmail.com                |")
print("|------------------------------------------------------|")
print("|                    -INFO-                            |")
print("|------------------------------------------------------|")
print("|Mutant Year Zero es un juego de ROL publicado por:    |")
print("|Free League Publishing todos los derechos reservados  |")
print("*------------------------------------------------------*")



while True:
    def entrada_numerica(pregunta, limite_inferior, limite_superior):
        numero_de_dados_por_usuario = None
        while True:
            numero_de_dados_por_usuario = input(pregunta)
            try:
                numero_de_dados_por_usuario = int(numero_de_dados_por_usuario)
                if numero_de_dados_por_usuario < limite_inferior or numero_de_dados_por_usuario > limite_superior:
                    raise ValueError
            except ValueError:
                print(f"\nSolo numeros entre {limite_inferior} y {limite_superior}\n")
                continue
            return numero_de_dados_por_usuario


    def seleccion_de_dados():
        print("Puedes lanzar entre 1 a 8 dados de tres colores:\n \nAmarillos [BASE]\nVerdes o de [HABILIDAD]\nNegros [EQUIPO]\n")
        print("Realiza tu tirada: \n")
        
        tirada_amarilla = entrada_numerica("Cuantos Amarillos vas a lanzar?: ", 1 ,8)
        tirada_verde = entrada_numerica("Cuantos Verdes vas a lanzar?: ", 1 ,8)
        tirada_negra = entrada_numerica("Cuantos Negros vas a lanzar?: ", 1 ,8)
        return tirada_amarilla, tirada_verde, tirada_negra

    tirada_amarilla, tirada_verde, tirada_negra = seleccion_de_dados()

    


    def generador(a,v,n):
        resultado = []
        
        lista_a = []
        lista_v = []
        lista_n = []
        
        resultado.append(lista_a)
        resultado.append(lista_v)
        resultado.append(lista_n)
        
        for _ in range(a):
            a = random.randint(1 ,6)
            lista_a.append(a)
        
        for _ in range(v):
            v = random.randint(1 ,6)
            lista_v.append(v)

        for _ in range(n):
            n = random.randint(1 ,6)
            lista_n.append(n)
            
        return lista_a, lista_v, lista_n
            

    lista_a, lista_v, lista_n = generador(tirada_amarilla, tirada_verde, tirada_negra)


    def clasificador():
            exitos_amarillos = lista_a.count(6)
            exitos_verdes = lista_v.count(6)
            exitos_negros = lista_n.count(6)
            total_exitos = exitos_amarillos + exitos_verdes + exitos_negros
            unos_amarillos = lista_a.count(1)
            unos_negros = lista_n.count(1)
            amarillos_segunda_tirada = len(lista_a) - unos_amarillos
            verdes_segunda_tirada = len(lista_v)
            negros_segunda_tirada = len(lista_n) - unos_negros
            
            return exitos_amarillos , exitos_verdes , exitos_negros , total_exitos, unos_amarillos, unos_negros, amarillos_segunda_tirada, verdes_segunda_tirada, negros_segunda_tirada
        
    exitos_amarillos , exitos_verdes , exitos_negros , total_exitos, unos_amarillos, unos_negros, amarillos_segunda_tirada, verdes_segunda_tirada, negros_segunda_tirada = clasificador()

    def tabla_primera_tirada():   

        t = Texttable()
        t.add_rows([['Color', 'Dados', 'Tirada', 'Exitos', 'Mutacion', 'Daño a Equipo'], 
                    ['Amarillo', 'x', lista_a , exitos_amarillos, unos_amarillos, '-'],
                    ['Verde', 'y', lista_v , exitos_verdes, '-', '-'],
                    ['Negro', 'z', lista_n , exitos_negros, '-', unos_negros]])

        print(t.draw())


    def generador_segunda_tirada(amarillos_segunda_tirada,verdes_segunda_tirada,negros_segunda_tirada):
        resultado = []
        
        f_lista_a = []
        f_lista_v = []
        f_lista_n = []
        
        resultado.append(f_lista_a)
        resultado.append(f_lista_v)
        resultado.append(f_lista_n)
        
        for _ in range(amarillos_segunda_tirada):
            amarillos_segunda_tirada = random.randint(1 ,6)
            f_lista_a.append(amarillos_segunda_tirada)
        
        for _ in range(verdes_segunda_tirada):
            verdes_segunda_tirada = random.randint(1 ,6)
            f_lista_v.append(verdes_segunda_tirada)

        for _ in range(negros_segunda_tirada):
            negros_segunda_tirada = random.randint(1 ,6)
            f_lista_n.append(negros_segunda_tirada)
        
        return f_lista_a ,f_lista_v, f_lista_n
            

    f_lista_a ,f_lista_v, f_lista_n = generador_segunda_tirada(amarillos_segunda_tirada,verdes_segunda_tirada,negros_segunda_tirada)

    def clasificador_forzado(f_lista_a, f_lista_v, f_lista_n):
            f_exitos_amarillos = f_lista_a.count(6)
            f_exitos_verdes = f_lista_v.count(6)
            f_exitos_negros = f_lista_n.count(6)
            f_total_exitos = exitos_amarillos + exitos_verdes + exitos_negros
            f_unos_amarillos = f_lista_a.count(1)
            f_unos_negros = f_lista_n.count(1)
            amarillos_segunda_tirada = len(f_lista_a) - exitos_amarillos
            verdes_segunda_tirada = len(f_lista_v)
            negros_segunda_tirada = len(f_lista_n) - unos_negros
            return f_exitos_amarillos, f_exitos_verdes , f_exitos_negros, f_total_exitos, f_unos_amarillos, f_unos_negros, amarillos_segunda_tirada, verdes_segunda_tirada, negros_segunda_tirada
        
    f_exitos_amarillos, f_exitos_verdes , f_exitos_negros, f_total_exitos, f_unos_amarillos, f_unos_negros, amarillos_segunda_tirada, verdes_segunda_tirada, negros_segunda_tirada = clasificador_forzado(f_lista_a, f_lista_v, f_lista_n)

    def tabla_segunda_tirada():

        f = Texttable()
        f.add_rows([['Color', 'Dados', 'Tirada', 'Exitos', 'Daño', 'Daño a Equipo'], 
                    ['Amarillo', 'x', f_lista_a , f_exitos_amarillos , f_unos_amarillos + unos_amarillos, '-'],
                    ['Verde', 'y', f_lista_v , f_exitos_verdes, '-', '-'],
                    ['Negro', 'z', f_lista_n , f_exitos_negros, '-', f_unos_negros + unos_negros]])

        print(f.draw())
        


    if total_exitos == 1:
        exito = Figlet(font='standard')
        print(exito.renderText("Exito!"))
        tabla_primera_tirada()
    elif total_exitos >= 2:
        proeza = Figlet(font='epic')
        print(proeza.renderText(f"ProezA x {total_exitos}"))
        tabla_primera_tirada()
    elif total_exitos == 0:
        primera_sin_exitos = Figlet(font='standard')
        print(primera_sin_exitos.renderText(f"{total_exitos} exitos..."))
        tabla_primera_tirada()
        while True:
            tirar_otra_vez = input("\nDeseas forzar la tirada (S/N): ").upper()
            
            if tirar_otra_vez == 'S':
                tirada_forzada = Figlet(font='ogre')
                print(tirada_forzada.renderText("Tirada forzada\n"))
                tabla_segunda_tirada()
                break
            elif tirar_otra_vez == 'N':
                break
    while True:
        roll_again = input("Deseas lanzar otra vez? (S/N):").upper()
        if roll_again not in ["S", "N", "SI", "NO"]:
            continue
        break
    if roll_again in ["N", "NO"]:
        print("Winners Don't Use Drugs")
        break


