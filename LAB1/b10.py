def Xác_suất_của_TH(Số_bi):
    Tổng_bi = 50
    Bi_đỏ = 20
    Bi_xanh = 15
    Bi_vàng = 15

    # Tất cả bóng đỏ
    Tất_cả_bi_đỏ = (Bi_đỏ / Tổng_bi) ** Số_bi

    # Ít nhất 1 viên bi xanh
    a = (1 - Bi_xanh / Tổng_bi) ** Số_bi
    Ít_nhất_1vienbixanh = 1 - a

    # Đúng hai viên bi vàng
    Hai_viên_bi_vàng = (Bi_vàng / Tổng_bi) * ((Bi_vàng - 1) / (Tổng_bi - 1))
    print("Tât cả là bi đỏ: {:.4f}".format(Tất_cả_bi_đỏ))
    print("Ít nhất một viên bi xanh: {:.4f}".format(Ít_nhất_1vienbixanh))
    print("Đúng hai viên bi là vàng: {:.4f}".format(Hai_viên_bi_vàng))
n = int(input("Nhập số lượng bóng mà bạn muốn tìm: "))
Xác_suất_của_TH(n)