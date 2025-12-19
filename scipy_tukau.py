
from scipy import integrate
import time
def f(x):
  return 3 * x**2


a = 0
b = 10
start = time.perf_counter()
ans, err = integrate.quad(f, a, b)
end = time.perf_counter()
print(f"計算時間:{end - start}秒\n")
print(f"計結果:{ans}")
