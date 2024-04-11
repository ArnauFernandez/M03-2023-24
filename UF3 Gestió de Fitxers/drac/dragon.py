dragon=open('Dragon.in', mode='rt', encoding='utf-8')
lectura=dragon.read()
dragon.close()
#----------------------------------
dragonclose=open('Dragonclose', mode='wt', encoding='utf-8')
dragonclose.write(lectura.replace('0','X'))
dragonclose.close()
