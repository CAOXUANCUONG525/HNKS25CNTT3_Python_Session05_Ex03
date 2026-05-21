# (1) Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input

# Người dùng nhập:

# Số lượng phòng học → int
# Số hàng ghế của từng phòng → int
# Số ghế trên mỗi hàng → int
# Output
# In sơ đồ phòng học bằng dấu *
# Hoặc thông báo lỗi nếu dữ liệu không hợp lệ

# Đề xuất giải pháp

# Chương trình sử dụng:

# Vòng lặp ngoài để duyệt từng phòng học
# Vòng lặp giữa để duyệt từng hàng ghế
# Vòng lặp trong để in dấu *

# Pseudocode
# Nhập room_count

# Nếu room_count <= 0
#     In "Số lượng phòng học không hợp lệ"
#     Kết thúc chương trình

# Lặp từng phòng học

#     Nhập rows
#     Nhập seats

#     Nếu rows <= 0 hoặc seats <= 0
#         In "Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này"
#         Bỏ qua phòng hiện tại

#     Nếu rows > 10 hoặc seats > 10
#         In "Phòng quá lớn. Dừng nhập dữ liệu"
#         Kết thúc chương trình

#     In tên phòng học

#     Lặp theo từng hàng
#         Lặp theo từng ghế
#             In *
#         Xuống dòng



room_count = int(input("Nhập số lượng phòng học: "))
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for room in range(1, room_count + 1):
        print(f"\n--- Phòng học {room} ---")
        rows = int(input("Nhập số hàng ghế: "))
        seats = int(input("Nhập số ghế mỗi hàng: "))
        if rows <= 0 or seats <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue
        if rows > 10 or seats > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break
        print("Sơ đồ chỗ ngồi:")
        for row in range(rows):
            for seat in range(seats):
                print("*", end="")
            print()