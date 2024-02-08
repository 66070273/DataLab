# ฟังก์ชัน summation แบบที่ 1: ใช้การวนลูปหาผลรวม
def summation_loop(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
# O(1)

# ฟังก์ชัน summation แบบที่ 2: ใช้สูตรคำนวณผลรวม
def summation_formula(n):
    return n * (n + 1) // 2
# O(1)

# ฟังก์ชันรับค่า n และทดสอบ summation ทั้ง 2 แบบ
def main():
    n = int(input())
    print(summation_formula(n))

main()
