import matplotlib.pyplot as plt
import time
kaisu = 10000
menseki = 0
katan = 0
jotan = 10
memori = float((jotan - katan) / kaisu)
if (jotan <= 0 or kaisu <= 0):
  print("Invalid input values.\n")
  exit()
start = time.perf_counter()
i = 1

while True:

  x = katan + memori * (i - 1)
  base1 = 3 * x * x
  base2 = 3 * (x + memori) * (x + memori)
  menseki += (base1 + base2) * memori / 2

  if (i >= kaisu):
    break
  i += 1
end = time.perf_counter()
print(f"計算時間:{end - start}秒\n")
print(f"台形近似値:{menseki}\n")
