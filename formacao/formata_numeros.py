def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# 3. Função para formatar quantidade

# Para quantidades:

def formatar_quantidade(valor):
    return f"{valor:,.0f}".replace(",", ".")