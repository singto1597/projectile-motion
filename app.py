import math

g = 9.81 
dt = 0.1 

x = 0
y = 0
speed = 50
angle = 45

theta = math.radians(angle)
vx = speed * math.cos(theta)
vy = speed * math.sin(theta)

t = 0
print(f"เวลา: {t:.1f}s -> ตำแหน่ง: ({x:.2f}, {y:.2f})")

while y >= 0:
    x = x + (vx * dt)
    y = y + (vy * dt)
    
    # v = a x t
    # dv = -g x t
    # v = v + dv
    # v = v + (-g x t)
    # v = v - g x t
    vy = vy - (g * dt)
    
    t += dt
    
    if y >= 0:
        print(f"เวลา: {t:.1f}s -> ตำแหน่ง: ({x:.2f}, {y:.2f})")
    else:
        print("บอลตกพื้นแล้ว")