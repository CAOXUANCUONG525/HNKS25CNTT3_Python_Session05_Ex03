# (1) Phân tích và thiết kế giải pháp 
# Toàn bộ dữ liệu đầu vào là string
# Output:
#   Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]

# Thiết kế thuật toán: Viết mã giả (Pseudocode) hoặc mô tả các bước thực hiện tuần tự.
#  Nhập thông tin bệnh nhân từ bàn phím
#  In ra tiêu đề "PHIẾU KHÁM BỆNH ĐIỆN TỬ"
#  In ra chuỗi định dạng: "Bệnh nhân: ho_ten - Mã BA: ma_benh_an - Chuyển tới: khoa_chi_dinh"

print (" --- HỆ THỐNG NHẬP CHI SỐ SINH TON --- ")
name_patient =input("Nhập họ và tên bệnh nhân:")
patient_code = input("Nhập mã bệnh nhân:")
department = input("Khoa chỉ định:")

print (" --- PHIẾU KHÁM BỆNH ĐIỆN TỬ --- ")
print ("Bệnh nhân : ", name_patient," - Mã BA:",patient_code," - Chuyển tới: ",department)


