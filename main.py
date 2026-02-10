print('hello world')

# on aura pas besoin de d'autres modules dans CoolProp que CoolProp
import CoolProp.CoolProp as CP

# CP.PropsSI('OUTPUT', 'INPUT1', VALUE1, 'INPUT2', VALUE2, 'FLUID')
# S entropie
# P Pression
# T températue
# D densité


# constant de l'air
R = CP.PropsSI('GAS_CONSTANT', 'Air') / CP.PropsSI('M', 'Air')




# Question 1: Température max du cycle

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
Pmax = CP.PropsSI('P', 'D', 1 / v2, 'S', s2, 'air') #Réponse
# 6. T2
T2 = CP.PropsSI('T', 'P', Pmax, 'S', s2, 'air')

# 7. P3 (2->3 isobare)
P3 = Pmax
# 8. v3 (r_c = 1.5)
v3 = v2 * 1.5
# 9 T3 = Tmax
Tmax = CP.PropsSI('T', 'P', P3, 'D', 1 / v3, 'air')
print(Tmax)