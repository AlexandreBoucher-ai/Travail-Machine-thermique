print('hello world')

# on aura pas besoin de d'autres modules dans CoolProp que CoolProp
import CoolProp.CoolProp as CP

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
