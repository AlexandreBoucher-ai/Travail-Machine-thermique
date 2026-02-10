print('hello world')

# on aura pas besoin de d'autres modules dans CoolProp que CoolProp
import CoolProp.CoolProp as CP



# 1. Température max du cycle

# 1.1 On setup notre table de l'air à basse pression:
# 1.1.1 Constante de l'air
R = CP.PropsSI('GAS_CONSTANT', 'Air') / CP.PropsSI('M', 'Air')

# 1.1.2 Les constantes arbitraitres
Tref = 288.15 # K | 15 celcius
Pstandard = 101325 # Pa

# 1.2 Volume relatif à l'état 1 (T = 300K):
T = 300
v = (R * T) / Pstandard
vref = (R * Tref) / Pstandard
vrel = v / vref

# volume massique relatif de l'air à T = 300K
