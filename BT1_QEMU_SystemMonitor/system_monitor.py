import psutil
from datetime import datetime
from time import sleep

log_file = open('system_log.txt', 'w')

try:
    while True:
        # Bước 2: Đọc CPU usage
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        # Bước 7: Logic phân loại trạng thái 3 mức
        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        # Bước 3: Đọc RAM và Disk
        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024 ** 2)
        ram_total_mb = ram.total // (1024 ** 2)
        ram_pct = ram.percent

        disk = psutil.disk_usage('/')
        disk_pct = disk.percent

        # Bước 4 & Bước 7: Format output có chứa {status}
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = (
            f"[{now}] CPU: {cpu_avg:.1f}% | "
            f"RAM: {ram_used_mb}/{ram_total_mb} MB ({ram_pct}%) | "
            f"Disk: {disk_pct}% | {status}"
)
        print(line)

        # Bước 7: In dòng cảnh báo riêng nếu cảnh báo
        if status != 'NORMAL':
            print(f'  ⚠ {status}: CPU đang ở {cpu_avg:.1f}%')

        # Bước 5: Ghi dòng line (đã có status) vào file + flush
        log_file.write(line + '\n')
        log_file.flush()

        sleep(2)

# Bước 6: Đóng an toàn
except KeyboardInterrupt:
    print('\nDừng giám sát.')
finally:
    log_file.close()
    print('Log saved to system_log.txt')
