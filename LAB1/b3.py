# Tính toán số tiền sau 5 năm
So_tien_ban_dau = 10000
Lai_suat_hang_nam = 0.06
years_5 = 5
amount_after_5_years = So_tien_ban_dau * (1 + Lai_suat_hang_nam) ** years_5

# Tính toán số tiền sau 10 năm
years_10 = 10
amount_after_10_years = So_tien_ban_dau * (1 + Lai_suat_hang_nam) ** years_10

# Tính toán tỷ lệ tăng trưởng
Ti_le_tang_truong = (amount_after_10_years - amount_after_5_years) / amount_after_5_years

# In kết quả
print("Số tiền sau 5 năm:", round(amount_after_5_years, 2))
print("Số tiền sau 10 năm:", round(amount_after_10_years, 2))
print("Tỷ lệ tăng trưởng sau 10 năm so với 5 năm:", round(Ti_le_tang_truong, 2))