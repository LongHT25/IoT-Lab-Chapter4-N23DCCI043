from sense_emu import SenseHat
import time

sense = SenseHat()

# Định nghĩa màu sắc
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

def draw_dashboard(t, h):
    sense.clear()
    # Bar chart nhiệt độ (Hàng 0-2) - Giả sử max là 50 độ
    t_pixels = int((t / 50.0) * 8)
    for y in range(3):
        for x in range(min(t_pixels, 8)):
            sense.set_pixel(x, y, RED)
            
    # Bar chart độ ẩm (Hàng 3-5) - Max là 100%
    h_pixels = int((h / 100.0) * 8)
    for y in range(3, 6):
        for x in range(min(h_pixels, 8)):
            sense.set_pixel(x, y, BLUE)
            
    # Hàng trạng thái (Hàng 6-7)
    color = GREEN
    if t > 30 or h > 80:
        color = RED if t > 30 else YELLOW
        
    for y in range(6, 8):
        for x in range(8):
            sense.set_pixel(x, y, color)

print("Bắt đầu giám sát trên Sense HAT...")

while True:
    # Lấy thông số trực tiếp từ thanh trượt của Emulator
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    
    draw_dashboard(temp, hum)
    
    # Báo động chữ chạy nếu quá nóng
    if temp > 30:
        sense.show_message("HOT!", text_colour=RED, scroll_speed=0.05)
        
    # Bắt sự kiện ấn Joystick ở giữa (middle)
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "middle":
            sense.show_message(f"{temp:.1f}C", text_colour=YELLOW, scroll_speed=0.05)
            
    time.sleep(0.1)
