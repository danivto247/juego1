# juego de turnos
from random import randint

# Variable de la duracion del globo
durDelGlobo = randint(0, 20)

# Variables de los tipos de globos
globoChiquito = randint(0, 8)
globoMediano = randint(8, 14)
globoGrande = randint(14, 19)

# bucle principal del juego
x = True
while x:
    # bucle del jugador 1
    y = True
    while y:
        # Ingreso del turno del jugador
        print("TURNO DEL JUGADOR 1")
        jugadaJugador1 = input("inflar glovo (si/no): ")
        if jugadaJugador1 == "si":
            durDelGlobo += 1
            print("ESTADO DEL GLOBO:\n")
            # Condicionales del estado del globo y de quien gano
            if durDelGlobo == 20:
                print("____~~~~~ <--- esto es un globo reventado\n")
                print("el globo se rompio")
                print("el jugador 2 gano!!!!")
                x = False
            elif 0 < durDelGlobo <= globoChiquito:
                print("  0\n  |\n  |\n")
            elif globoChiquito < durDelGlobo <= globoMediano:
                print("   *\n  ***\n   *\n   |\n   |\n")
            elif globoMediano < durDelGlobo <= globoGrande:
                print("  ***\n *****\n*******\n *****\n  ***\n   |\n   |\n")
            elif globoGrande < durDelGlobo < 20:
                print("   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    |\n    |\n")
        elif jugadaJugador1 == "no":
            y = False
        else:
            print("el jugador se da su tiempo")
    # bucle del jugador 2
    z = True
    while z:
        # Ingreso del turno del jugador
        print("TURNO DEL JUGADOR 2")
        jugadaJugador2 = input("inflar glovo (si/no): ")

        if jugadaJugador2 == "si":
            durDelGlobo += 1
            print("ESTADO DEL GLOBO:\n")
            # Condicionales del estado del globo y de quien gano
            if durDelGlobo == 20:
                print("____~~~~~ <--- esto es un globo reventado")
                print("el globo se rompio")
                print("el jugador 1 gano!!!!")
                x = False
            elif 0 < durDelGlobo <= globoChiquito:
                print("  0\n  |\n  |\n")
            elif globoChiquito < durDelGlobo <= globoMediano:
                print("   *\n  ***\n   *\n   |\n   |\n")
            elif globoMediano < durDelGlobo <= globoGrande:
                print("  ***\n *****\n*******\n *****\n  ***\n   |\n   |\n")
            elif globoGrande < durDelGlobo < 20:
                print("   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    |\n    |\n")
        elif jugadaJugador2 == "no":
            z = False
        else:
            print("el jugador se da su tiempo")
    # para que los bucles de los jugadores sigan haciendo su trabajo
    y = True
    z = True
