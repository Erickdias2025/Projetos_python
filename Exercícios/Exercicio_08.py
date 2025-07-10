m = float(input('Metro: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('Metros: {}\nQuilômetros: {}\nHectômetros: {}\nDecâmetros: {}\nDecímetros: {:.0f}\nCentímetros: {:.0f}\nMilímetros: {:.0f}'.format(
    m, km, hm, dam, dm, cm, mm))
