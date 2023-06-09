import random
import numpy as np
import matplotlib.pyplot as plt

sample = [random.randint(0, 10) for _ in range(30)]
print(f"sample: {sample}")
print(f"mean:{np.mean(sample)}")
print(f"variance: {np.var(sample)}")

plt.hist(sample)
plt.show()
