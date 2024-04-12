
g1 = graph(title="Delta Area",xtitle = "t ",ytitle="dA",width=500, height=250)
f1 = gcurve(color=color.blue)
G = 1
M = 1
m = 1
r1 = 1
v1 = 0.7

sun = sphere(pos=vector(0,0,0),radius=0.03, color=color.yellow)
planet = sphere(pos=sun.pos+vector(r1,0,0), radius=0.01, color=color.cyan, make_trail=True)

planet.p = m*vector(0,v1,0)

t = 0
dt = 0.001

T = 0.5
r1 = cylinder(pos=sun.pos, axis=planet.pos-sun.pos, radius=0.01)
A1 = 0

t2 = 1.5
while t<T:
  rate(1000)
  r = planet.pos - sun.pos
  F = -G*M*m*norm(r)/mag(r)**2
  planet.p = planet.p + F*dt
  planet.pos = planet.pos + planet.p*dt/m
  dA = .5*mag(cross(r,planet.p/m))*dt
  A1 = A1 + dA
  f1.plot(t,dA)

  t = t + dt

print("A1 = ",A1)
r2 = cylinder(pos=sun.pos, axis=planet.pos-sun.pos, radius=0.01)

while t<t2:
  rate(1000)
  r = planet.pos - sun.pos
  F = -G*M*m*norm(r)/mag(r)**2
  planet.p = planet.p + F*dt
  planet.pos = planet.pos + planet.p*dt/m
  dA = .5*mag(cross(r,planet.p/m))*dt

  f1.plot(t,dA)

  t = t + dt

r3 = cylinder(pos=sun.pos, axis=planet.pos-sun.pos, radius=0.01, color=color.yellow)
A2 = 0

while t<t2+T:
  rate(1000)
  r = planet.pos - sun.pos
  F = -G*M*m*norm(r)/mag(r)**2
  planet.p = planet.p + F*dt
  planet.pos = planet.pos + planet.p*dt/m
  dA = .5*mag(cross(r,planet.p/m))*dt
  A2 = A2 + dA
  f1.plot(t,dA)

  t = t + dt

r4 = cylinder(pos=sun.pos, axis=planet.pos-sun.pos, radius=0.01, color=color.yellow)
print("A2 = ",A2)
