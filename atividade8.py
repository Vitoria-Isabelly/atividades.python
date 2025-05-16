meta = 5000
economia_mensal = 200

meses_necessarios = meta // economia_mensal
resto = meta % economia_mensal

meses_necessarios += bool(resto)

print(f"Serão necessários {meses_necessarios} meses para atingir a meta.")
