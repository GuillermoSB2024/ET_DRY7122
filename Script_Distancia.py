from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def obtener_coordenadas(ciudad):
    geolocalizador = Nominatim(user_agent="mygeocoder")
    coordenadas = geolocalizador.geocode(ciudad)
    if coordenadas:
        return coordenadas.latitude, coordenadas.longitude
    else:
        return None

def calcular_distancia(ciudad1, ciudad2):
    coordenadas_ciudad1 = obtener_coordenadas(ciudad1)
    coordenadas_ciudad2 = obtener_coordenadas(ciudad2)
    if coordenadas_ciudad1 and coordenadas_ciudad2:
        distancia = geodesic(coordenadas_ciudad1, coordenadas_ciudad2).kilometers
        return distancia
    else:
        return None

def mostrar_resultados(distancia_km, transporte, origen, destino):
    millas = distancia_km * 0.621371
    velocidad_promedio = {
        'avion': 800,  # km/h
        'auto': 100,   # km/h
        'bicicleta': 20,  # km/h
        'caminando': 5   # km/h
    }.get(transporte, 0)
    
    if velocidad_promedio:
        duracion_horas = distancia_km / velocidad_promedio
        duracion_minutos = duracion_horas * 60
        print(f"Distancia entre {origen} y {destino}: {distancia_km:.2f} km ({millas:.2f} millas)")
        print(f"Duración del viaje en {transporte}: {duracion_horas:.2f} horas ({duracion_minutos:.0f} minutos)")
        print(f"Medio de transporte: {transporte.capitalize()}\n")
    else:
        print("Medio de transporte no válido.")

def main():
    while True:
        origen = input("Introduce la Ciudad de Origen (o 'e' para salir): ")
        if origen.lower() == 'e':
            break
        destino = input("Introduce la Ciudad de Destino: ")
        transporte = input("Introduce el medio de transporte (avion, auto, bicicleta, caminando): ").lower()
        
        distancia_km = calcular_distancia(origen, destino)
        
        if distancia_km:
            mostrar_resultados(distancia_km, transporte, origen, destino)
        else:
            print("No se pudieron obtener las coordenadas de las ciudades. Por favor, verifica los nombres ingresados.")

if __name__ == "__main__":
    main()