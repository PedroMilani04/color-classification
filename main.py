import cv2  
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.axis('off')
plt.show()

heigth, width, channel = img_rgb.shape
print(f"[DATA] Analasyng {heigth * width} pixels")

pixels = img_rgb.reshape(-1, 3) # R G B
mean_color = np.mean(pixels, axis=0) 

print(f"[MEAN] Red: {mean_color[0]:.0f}")
print(f"[MEAN] Green: {mean_color[1]:.0f}")
print(f"[MEAN] Blue: {mean_color[2]:.0f}")

r, g, b = mean_color

def create_square(color):
    square = np.full((100,100, 3), color, dtype=np.uint8)
    return square


def analyze_color(r, g, b):
    # Calculate color intensity
    intensity = (r + g + b) / 3
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    delta = max_color - min_color
    
    # Calculate saturation
    saturation = delta / max_color if max_color != 0 else 0
    
    # Dominance thresholds
    dominance_threshold = 20
    high_intensity = 180
    medium_intensity = 100

    # Achromatic colors
    if delta < 15 and saturation < 0.15:
        if intensity > 220:
            return "Pure white"
        elif intensity > 180:
            return "Grayish white"
        elif intensity < 30:
            return "Pure black"
        elif intensity < 60:
            return "Grayish black"
        else:
            return f"Gray ({intensity:.0f}%)"
    
    # Chromatic colors
    if r > g + dominance_threshold and r > b + dominance_threshold:
        if intensity > high_intensity:
            return "Vibrant red" if saturation > 0.7 else "Light red"
        elif intensity < medium_intensity:
            return "Dark red" if saturation > 0.5 else "Burgundy"
        else:
            return "Medium red"
            
    elif g > r + dominance_threshold and g > b + dominance_threshold:
        if intensity > high_intensity:
            return "Vibrant green" if saturation > 0.7 else "Light green"
        elif intensity < medium_intensity:
            return "Dark green" if saturation > 0.5 else "Moss green"
        else:
            return "Medium green"
            
    elif b > r + dominance_threshold and b > g + dominance_threshold:
        if intensity > high_intensity:
            return "Vibrant blue" if saturation > 0.7 else "Light blue"
        elif intensity < medium_intensity:
            return "Dark blue" if saturation > 0.5 else "Navy blue"
        else:
            return "Medium blue"
    
    # Mixed colors
    if abs(r - g) < 15 and r > b + dominance_threshold:
        return "Yellow" if intensity > high_intensity else "Dark yellow"
    elif abs(r - b) < 15 and r > g + dominance_threshold:
        return "Magenta" if intensity > high_intensity else "Purple"
    elif abs(g - b) < 15 and g > r + dominance_threshold:
        return "Cyan" if intensity > high_intensity else "Turquoise"
    
    return "Undefined mixed color"

result = analyze_color(r, g, b)

square = create_square(mean_color)

plt.figure(figsize=(8, 6))
plt.imshow(square)
plt.title("Color")
plt.axis('off')  # Remove os números dos eixos
plt.show()

print(f"[COLOR] The dominant color is: {result}")

