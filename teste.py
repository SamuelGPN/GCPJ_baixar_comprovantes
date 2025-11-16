import clipboard

# Copiar texto para a área de transferência
clipboard.copy("Texto para copiar")

# Colar texto da área de transferência
texto = clipboard.paste()
print("Texto colado:", texto)

