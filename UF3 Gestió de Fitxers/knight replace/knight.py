caballero=open('Knight.txt', mode='rt', encoding='utf-8')
lectura=caballero.read()
caballero.close()
#----------------------------------
caballerocerrar=open('knight.close', mode='wt', encoding='utf-8')
caballerocerrar.write(lectura.replace('0','X'))
caballerocerrar.close()
