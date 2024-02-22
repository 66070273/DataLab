def selectionSort(lst, last):
    comparisons = 0  # นับจำนวนการเปรียบเทียบ
 
    for current in range(last):
        smallest = current
 
        for walker in range(current + 1, last + 1):
            if lst[walker] < lst[smallest]:
                smallest = walker
            comparisons += 1
 
        lst[current], lst[smallest] = lst[smallest], lst[current]
        print(lst)
 
    print("Comparison times:", comparisons)
 
# รับข้อมูล input
data = input()
data = list(map(int, data[1:-1].split(', ')))
last_index = int(input())
 
# เรียกใช้งานฟังก์ชัน selectionSort
selectionSort(data, last_index)