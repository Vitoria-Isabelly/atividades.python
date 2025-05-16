autonomia_km_por_litro = 12
tanque_litros = 40
distancia_viagem = 450

autonomia_total = autonomia_km_por_litro * tanque_litros

mensagem = "Viagem possível sem reabastecer" if autonomia_total >= distancia_viagem else "Será necessário reabastecer"
print(mensagem)
