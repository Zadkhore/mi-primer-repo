def double(arr):
    return [elem * 2 for elem in arr]

def maximum(arr):
    if not arr:
        return None
    return max(arr)

def average(arr):
    if not arr:
        return 0
    
    sumatotal = sum(arr)
    cantidad = len(arr)
    return sumatotal / cantidad

def main():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [10, 20, 5, 40]
    lista3 = [-5, 0, 5, 10]
    lista4 = [0, 0, 0, 0]

    print("Prueba lista 1:", lista1, "--->")
    print(f"La lista es: {lista1}")
    print(f"Doble: {double(lista1)}")
    print(f"Máximo: {maximum(lista1)}")
    print(f"Promedio: {average(lista1)}")
    print("----------------------------")

    print("Prueba lista 2:", lista2, "--->")
    print(f"La lista es: {lista2}")
    print(f"Doble: {double(lista2)}")
    print(f"Máximo: {maximum(lista2)}")
    print(f"Promedio: {average(lista2)}")
    print("----------------------------")
    
    print("Prueba lista 3:", lista3, "--->")
    print(f"La lista es: {lista3}")
    print(f"Doble: {double(lista3)}")
    print(f"Máximo: {maximum(lista3)}")
    print(f"Promedio: {average(lista3)}")
    print("----------------------------")

    print("Prueba lista 4:", lista4, "--->")
    print(f"La lista es: {lista4}")
    print(f"Doble: {double(lista4)}")
    print(f"Máximo: {maximum(lista4)}")
    print(f"Promedio: {average(lista4)}")

if __name__ == "__main__":
    main()