def isIntersect(a, b, c):
    # ตรวจสอบสมาชิกในลิสต์ a ว่ามีอยู่ใน b และ c หรือไม่
    for item_a in a:
        if item_a in b and item_a in c:
            return True
    return False
# O(n**2)

# รับค่าลิสต์ a, b, และ c จากผู้ใช้
a_input = input()
b_input = input()
c_input = input()

# แปลงข้อมูลจาก string เป็นลิสต์โดยแยกด้วยเครื่องหมาย ","
a = [int(x) for x in a_input[1:-1].split(',')]
b = [int(x) for x in b_input[1:-1].split(',')]
c = [int(x) for x in c_input[1:-1].split(',')]

# ทดสอบฟังก์ชัน isIntersect
print(isIntersect(a, b, c))
