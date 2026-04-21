import matplotlib
import matplotlib.pyplot as plt
from time import sleep
from sensor_sim import SimUltrasonic, SimPotentiometer

# Cấu hình matplotlib sau khi đã import xong tất cả
matplotlib.use('Agg')  # Required for headless QEMU/VirtualBox


# Initialize sensors
us = SimUltrasonic(echo=24, trigger=23, base_distance=30.0)
pot = SimPotentiometer(initial_value=0.3)
span = pot.value * 100  # Threshold: 40cm


# --- Step 5: Collect 50 samples ---
distances = []
print("Bắt đầu thu thập dữ liệu...")
for i in range(50):
    d = us.distance
    distances.append(d)
    print(f"  Mẫu {i+1}/50: {d:.1f} cm")
    sleep(0.1)

print(f"\nThu thập xong {len(distances)} mẫu.")


# --- Step 6: Plotting (English Labels and Print) ---
fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(distances))

# Plot distance line (blue)
ax.plot(x, distances, 'b-', linewidth=1.5, label='Distance (cm)')

# Plot span threshold line (red dashed)
ax.axhline(y=span, color='r', linestyle='--', linewidth=2, label=f'Span = {span:.0f} cm')

# Fill Span Region (distance < span)
fill_area = [min(d, span) for d in distances]
ax.fill_between(x, 0, fill_area, alpha=0.2, color='red', label='Span Region!')

# Labels, title, and grid
ax.set_title('Ultrasonic Sensor Simulation — Span Detection')
ax.set_xlabel('Sample')
ax.set_ylabel('Distance (cm)')
ax.set_ylim(0, max(distances) + 10)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sensor_chart.png', dpi=150)

# STEP 6A REQUIRED OUTPUT:
print('Saved: sensor_chart.png')
