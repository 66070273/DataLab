# ฟังก์ชัน summation แบบที่ 1: ใช้การวนลูปหาผลรวม
def summation_loop(n):
    result = 0
    i = 1
    while i <= n:
        result += i
        i += 1
    return result
# O(n)

# ฟังก์ชัน summation แบบที่ 2: ใช้การบวกเลขต่อเนื่อง n ครั้ง
def summation_formula(n):
    result = 0
    for i in range(n):
        result += n - i
    return result
# O(n)

# ฟังก์ชันรับค่า n และทดสอบ summation ทั้ง 2 แบบ
def main():
    n = int(input())
    print(summation_formula(n))
    
main()
