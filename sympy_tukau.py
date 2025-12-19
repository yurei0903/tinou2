from sympy import symbols, integrate
import time
x = symbols('x')
start = time.perf_counter()
ans = integrate(3 * x**2, (x, 0, 10))
end = time.perf_counter()
print(f"計算時間:{end - start}秒\n")
print(f"積分値:{ans}\n")
