import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

temps, hums, dists = [], [], []

# Đọc dữ liệu
with open('wokwi_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        temps.append(float(row['temperature']))
        hums.append(float(row['humidity']))
        dists.append(float(row['distance']))

# Tạo 3 subplot
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# Đồ thị Nhiệt độ (Đỏ)
axes[0].plot(temps, 'r-', linewidth=1.5)
axes[0].axhline(y=30, color='orange', linestyle='--', linewidth=2, label='Threshold 30°C')
axes[0].set_ylabel('Temp (°C)')
axes[0].set_title('Server Room Dashboard')
axes[0].legend(loc='upper right')
axes[0].grid(True, alpha=0.3)

# Đồ thị Độ ẩm (Xanh dương)
axes[1].plot(hums, 'b-', linewidth=1.5)
axes[1].axhline(y=80, color='orange', linestyle='--', linewidth=2, label='Threshold 80%')
axes[1].set_ylabel('Humidity (%)')
axes[1].legend(loc='upper right')
axes[1].grid(True, alpha=0.3)

# Đồ thị Khoảng cách (Xanh lá)
axes[2].plot(dists, 'g-', linewidth=1.5)
axes[2].axhline(y=30, color='red', linestyle='--', linewidth=2, label='Intrusion < 30cm')
axes[2].set_ylabel('Distance (cm)')
axes[2].set_xlabel('Sample')
axes[2].legend(loc='upper right')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('server_dashboard.png', dpi=150)
print('Saved: server_dashboard.png')
