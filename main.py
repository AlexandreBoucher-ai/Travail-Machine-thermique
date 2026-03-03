
import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt

# CP.PropsSI('OUTPUT', 'INPUT1', VALUE1, 'INPUT2', VALUE2, 'FLUID')
# S entropie
# P Pression
# T températue
# D densité
# U énergie interne
# H enthalpie

# constant de l'air
R = CP.PropsSI('GAS_CONSTANT', 'Air') / CP.PropsSI('M', 'Air')


# Question 1: Pression max et Température max du cycle
# 1. v1 (P1 = 200 Kpa et T1 = 300K ) (remarque: D = densité,
# donc il faut inversé pour volume massique)
v1 = 1 / (CP.PropsSI('D', 'P', 200000, 'T', 300, 'air'))

# 2. s1 (P1 = 200 Kpa et T1 = 300K)
s1 = CP.PropsSI('S', 'P', 200000, 'T', 300, 'air')

# 3. s2 (1->2 est isentropique)
s2 = s1
# 4. v2 (r =20)
v2 = v1 / 20
# 5. P2 = Pmax
Pmax = CP.PropsSI('P', 'D', 1 / v2, 'S', s2, 'air') # Réponse
P2 = Pmax
# 6. T2
T2 = CP.PropsSI('T', 'P', Pmax, 'S', s2, 'air')

# 7. P3 (2->3 isobare)
P3 = Pmax
# 8. v3 (r_c = 1.5)
v3 = v2 * 1.5
# 9 T3 = Tmax
Tmax = CP.PropsSI('T', 'P', P3, 'D', 1 / v3, 'air') # Réponse
T3 = Tmax


# Question 2: PME et rendement du cycle
# 1. s3
s3 = CP.PropsSI('S', 'T', Tmax, 'P', P3, 'air')

# 2. s4
s4 = s3
# 3. P4
P4 = P1 = 200000
# 4. u4
u4 = CP.PropsSI('U', 'P', P4, 'S', s4, 'air')

# 5. u1
T1 = 300
u1 = CP.PropsSI('U', 'P', P1, 'T', T1, 'air')

# 6. qout
qout = u4 - u1

# 7. h2
h2 = CP.PropsSI('H', 'T', T2, 'P', P2, 'air')
# 8. h3
h3 = CP.PropsSI('H', 'T', T3, 'P', P3, 'air')

# 9. qin
qin = h3 - h2

# 10. wnet
wnet = qin - qout

# 11. PME
PME = wnet / (v1 - v2) # Réponse

# 12. rendement
n = wnet / qin # Réponse


# Question 3: Consommation de carburant
# 1. L nécessaire par cycle (Conso per cycle = cpc)
Pcal = 38220000 # J/L
cpc = wnet / Pcal

# 2. Nb de cycle par heure (nph)
nph = 3600 * (200 / 60)

# 3. Consommation par heure (cph)
cph = cpc * nph # Réponse


# Question 4: On enlève turbo, P1 = 100000
# 1. On réutilise calcul question 1 en modifiant P1
# Indice t pour chaque pour les différencier d'avec turbo
# (P1 = 100 Kpa)
v1t = 1 / (CP.PropsSI('D', 'P', 100000, 'T', 300, 'air'))
s1t = CP.PropsSI('S', 'P', 100000, 'T', 300, 'air')
s2t = s1t
v2t = v1t / 20
Pmaxt = CP.PropsSI('P', 'D', 1 / v2t, 'S', s2t, 'air')
P2t = Pmaxt
T2t = CP.PropsSI('T', 'P', Pmaxt, 'S', s2t, 'air')
P3t = Pmaxt
v3t = v2t * 1.5
Tmaxt = CP.PropsSI('T', 'P', P3t, 'D', 1 / v3t, 'air')
T3t = Tmaxt
# 2. On réutilise calcul question 2
s3t = CP.PropsSI('S', 'T', Tmaxt, 'P', P3t, 'air')
s4t = s3t
P4t = P1t = 200000
u4t = CP.PropsSI('U', 'P', P4t, 'S', s4t, 'air')
T1t = 300
u1t = CP.PropsSI('U', 'P', P1t, 'T', T1t, 'air')
qoutt = u4t - u1t
h2t = CP.PropsSI('H', 'T', T2t, 'P', P2t, 'air')
h3t = CP.PropsSI('H', 'T', T3t, 'P', P3t, 'air')
qint = h3t - h2t
wnett = qint - qoutt
# 3. Puissance (en Hp)
mt = 25 / (v1t - v2t)
Pt = mt * wnett * (200/60)
PHPt = Pt/745.7 # Réponse
# 4. PME
PMEt = wnett / (v1t - v2t) # Réponses
# 5. Rendement
nt = wnett / qint # Réponse


# Question 5:
# On crée un fonction qui accèpte le taux de compression en entré (seul variable) et 
# qui utilise les équations des numéros 1-2-4
# L'équation retourne Tmax, Pmax, n, PME et Puissance
def moteur(r):
    v1 = 1 / (CP.PropsSI('D', 'P', 200000, 'T', 300, 'air'))
    s1 = CP.PropsSI('S', 'P', 200000, 'T', 300, 'air')
    s2 = s1
    v2 = v1 / r # ici l'impact de r
    Pmax = CP.PropsSI('P', 'D', 1 / v2, 'S', s2, 'air') # Réponse
    P2 = Pmax
    T2 = CP.PropsSI('T', 'P', Pmax, 'S', s2, 'air')
    P3 = Pmax
    v3 = v2 * 1.5 # rc (ne varie pas)
    Tmax = CP.PropsSI('T', 'P', P3, 'D', 1 / v3, 'air') # Réponse
    T3 = Tmax
    s3 = CP.PropsSI('S', 'T', Tmax, 'P', P3, 'air')
    s4 = s3
    P4 = P1 = 200000
    u4 = CP.PropsSI('U', 'P', P4, 'S', s4, 'air')
    T1 = 300
    u1 = CP.PropsSI('U', 'P', P1, 'T', T1, 'air')
    qout = u4 - u1
    h2 = CP.PropsSI('H', 'T', T2, 'P', P2, 'air')
    h3 = CP.PropsSI('H', 'T', T3, 'P', P3, 'air')
    qin = h3 - h2
    wnet = qin - qout
    PME = wnet / (v1 - v2) # Réponse
    n = wnet / qin # Réponse
    m = 25 / (v1 - v2)
    P = m * wnet * (200/60)
    PHP = P/745.7
    return(Tmax, Pmax, n, PME, PHP)
# On calcul pour chaque r
print(moteur(14))
print(moteur(16))
print(moteur(18))
print(moteur(20))
print(moteur(22))
print(moteur(24))


# Question 6: Tracer (utilise résultats de question 5)
liste_r = [14, 16, 18, 20, 22, 24]
liste_tmax = [1259.5669333581325, 1324.2622971453927, 1384.0953845779875,
              1439.9953392488885, 1492.6487353412208, 1542.5782117510264]
liste_pmax = [8009809.711578557, 9656349.015308954, 11392304.868808817,
              13213735.297730844, 15117606.450237328, 17101559.312165264]
liste_n = [0.7347801182015559, 0.7467413626720683, 0.7567846934996245,
           0.7653918288090097, 0.7728890681341257, 0.7795065415600817]
liste_PME = [903594.5516141937, 967150.2480030286, 1027382.2421808725,
             1084880.0106525351, 1140102.860307167, 1193414.9945206803]
liste_P = [100978.3370897807, 108080.80193140994, 114811.83699665553,
           121237.31735869375, 127408.5713990397, 133366.299508368]

plt.cla()
plt.figure()

plt.subplot(6, 6, 1)
plt.plot(liste_r, liste_tmax)
plt.title('Tmax en fonction de r')
plt.xlabel('r')
plt.ylabel('Tmax')

plt.subplot(6, 6, 2)
plt.plot(liste_r, liste_pmax)
plt.title('Pmax en fonction de r')
plt.xlabel('r')
plt.ylabel('Pmax')