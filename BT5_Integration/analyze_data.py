import csv

temps, hums, dists = [], [], []
warnings = 0
intrusions = 0  # distance < 30cm

# Đọc file CSV bạn vừa đẩy vào
with open('wokwi_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        t = float(row['temperature'])
        h = float(row['humidity'])
        d = float(row['distance'])
        
        temps.append(t)
        hums.append(h)
        dists.append(d)
        
        if row['status'] != 'NORMAL':
            warnings += 1
        if d < 30:
            intrusions += 1

# In Báo cáo ra Terminal
print('\n=== BÁO CÁO PHÒNG SERVER ===')
print(f'Tổng số mẫu đo: {len(temps)}')
print(f'Nhiệt độ: TB={sum(temps)/len(temps):.1f}°C, Min={min(temps):.1f}°C, Max={max(temps):.1f}°C')
print(f'Độ ẩm: TB={sum(hums)/len(hums):.1f}%, Min={min(hums):.1f}%, Max={max(hums):.1f}%')
print(f'Phát hiện người vào (Khoảng cách < 30cm): {intrusions} lần')
print(f'Số lần cảnh báo (WARNING): {warnings}/{len(temps)} ({warnings/len(temps)*100:.0f}%)\n')

# Ghi report vào file text
with open('report.txt', 'w') as f:
    f.write('=== BÁO CÁO PHÒNG SERVER ===\n')
    f.write(f'Tong mau: {len(temps)}\n')
    f.write(f'Nhiet do TB: {sum(temps)/len(temps):.1f}\n')
    f.write(f'Phat hien nguoi vao: {intrusions}\n')
    f.write(f'So lan canh bao: {warnings}\n')

print("Đã ghi báo cáo tóm tắt vào file: report.txt")
