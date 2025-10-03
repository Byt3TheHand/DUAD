time_in_seconds = int(input("Digite su tiempo en segundos: "))
ten_minutes = 600

if time_in_seconds < ten_minutes:
    time_remaining = ten_minutes - time_in_seconds
    print(f"Te faltan {time_remaining} segundos para llegar a 10 minutos")
elif time_in_seconds == ten_minutes:
    print("Tu tiempo es igual a 10 minutos")
else:
    print("Tu tiempo es mayor a 10 minutos")