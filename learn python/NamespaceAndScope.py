# tao bien toan cuc
bien_toan_cuc = 10

def func_bien_cuc_bo():

    # bien cuc bo
    bien_cuc_bo = 20

    def func_bien_long_cuc_bo():
        # bien long cuc bo
        bien_long_cuc_bo = 30

        print(bien_long_cuc_bo)
    print(bien_cuc_bo)

    # goi ham long cuc bo ra bien cuc bo
    func_bien_long_cuc_bo()

print(bien_toan_cuc)

# goi bien cuc bo ra globbal
func_bien_cuc_bo()



# su dung tu khoa toan cuc
