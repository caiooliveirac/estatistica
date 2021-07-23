def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    media = sum(vals) / n
    numerador = []
    for i in vals:
        distancia = i - media
        numerador.append(distancia**2)
    variancia = sum(numerador) / n
    print(round(math.sqrt(variancia),1))

if __name__ == '__main__':
    #n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(stdDev(vals))
