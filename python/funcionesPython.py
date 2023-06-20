import numpy as np

def print_array(entradas):
    rows, columns = entradas.shape
    for j in range(rows):
        for x in range(columns):
            print(f"{entradas[j][x]:>2s}", end=' ')
        print()

def reservation(seat_number, entradas):
    indices = np.where(entradas == seat_number)
    row = indices[0][0]
    column = indices[1][0]
    entradas[row][column] = "X"

def compra_tickets_asientos(tipo, compras, tickets_compras, contadoresAsientos):
    datos_ingresados = np.array([0, 0, 0, 0])
    prices = np.array([50000, 100000, 200000])
    compras[datos_ingresados[2]][tipo] += prices[tipo]
    tickets_compras[datos_ingresados[2]][tipo] += 1
    contadoresAsientos[tipo] += 1  # Increment seat counter for the purchased type
    
def print_client_purchase(ticket, index, tickets_compras, compras):
    if ticket == 0:
        nombres = "normales"
    elif ticket == 1:
        nombres = "buenos"
    elif ticket == 2:
        nombres = "premium"
    if tickets_compras[index][ticket] != 0:
        print(f"Total tickets {nombres}: {tickets_compras[index][ticket]} por ${compras[index][ticket]}")
