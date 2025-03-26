import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2 # type: ignore

# Kích thước của texture
width = 256
height = 256

# Tần số của Perlin noise
scale = 100.0

# Độ sâu của noise
octaves = 6

# Độ phức tạp
persistence = 0.5
lacunarity = 2.0

# Tạo mảng 2D cho texture
texture = np.zeros((height, width))

# Tạo Perlin noise
for y in range(height):
    for x in range(width):
        noise_value = pnoise2(x / scale,
                              y / scale,
                              octaves=octaves,
                              persistence=persistence,
                              lacunarity=lacunarity,
                              repeatx=1024,
                              repeaty=1024,
                              base=42)
        # Chuyển đổi giá trị noise từ [-1, 1] sang [0, 1]
        texture[y][x] = (noise_value + 1) / 2

# Hiển thị texture
plt.imshow(texture, cmap='gray')
plt.colorbar()
plt.show()
