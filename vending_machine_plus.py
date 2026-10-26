# ==============================================================================
# PROYEK 1 BERPIKIR KOMPUTASIONAL (WI1102) - KELOMPOK 6
# File : vendingmachine.py
# Fitur: Keranjang Belanja Multi-Item, Kalkulasi Keuntungan Harian,
#        Auto-Restock Terlaris (+5 pcs), dan Refill Stok Habis (+10 pcs).
# ==============================================================================

produk_vending = [
    ["Aqua Air Mineral", 4000, 10, 0],
    ["Teh Pucuk", 5000, 10, 0],
    ["Pocari Sweat", 8000, 10, 0],
    ["Beng-Beng", 2500, 10, 0]
]

N = len(produk_vending)
status_mesinmenyala = True

while status_mesinmenyala:
    print("\n" + "="*35)
    print("    DAFTAR MENU VENDING MACHINE")
    print("="*35)
    print(" 1. Beli Barang")
    print(" 2. Tutup Hari (KHUSUS PEMILIK)")
    print(" 3. Keluar")

    pilihan = input("Pilih menu (1-3): ").strip()

    if pilihan == "1":
        # Menggunakan dictionary {indeks_barang: jumlah_dibeli} agar gampang gabungin barang yang sama
        keranjang = {}

        while True:
            print("\n" + "-"*35)
            print(" DAFTAR PRODUK TERSEDIA")
            print("-"*35)
            for i in range(N):
                stok_di_keranjang = keranjang.get(i, 0)
                stok_sisa = produk_vending[i][2] - stok_di_keranjang
                print(f" {i}. {produk_vending[i][0]} - Rp{produk_vending[i][1]} (Sisa Stok: {stok_sisa})")

            try:
                input_indeks = input("\nMasukkan Indeks Barang (atau ketik 'selesai' untuk checkout): ").strip()
                if input_indeks.lower() == 'selesai':
                    break

                indeks = int(input_indeks)
                if 0 <= indeks < N:
                    stok_di_keranjang = keranjang.get(indeks, 0)
                    stok_sisa = produk_vending[indeks][2] - stok_di_keranjang

                    if stok_sisa > 0:
                        jumlah = int(input(f"Masukkan jumlah {produk_vending[indeks][0]} yang mau dibeli (1-{stok_sisa}): "))
                        if 0 < jumlah <= stok_sisa:
                            keranjang[indeks] = keranjang.get(indeks, 0) + jumlah
                            print(f"\n[+] Berhasil menambahkan {jumlah}x {produk_vending[indeks][0]} ke keranjang!")
                        else:
                            print("\n[!] Jumlah tidak valid atau melebihi sisa stok!")
                    else:
                        print("\n[!] Stok barang ini sudah habis atau maksimal di keranjang!")
                else:
                    print("\n[!] Indeks barang tidak ditemukan!")

            except ValueError:
                print("\n[!] Input tidak valid! Masukkan angka indeks atau ketik 'selesai'.")

            lanjut = input("\nMau tambah barang lain ke keranjang? (y/n): ").strip().lower()
            if lanjut != 'y':
                break

        # Sesi Checkout Keranjang Belanja
        if keranjang:
            print("\n" + "="*40)
            print("         RINGKASAN KERANJANG BELANJA")
            print("="*40)
            total_bayar = 0
            for idx, qty in keranjang.items():
                nama = produk_vending[idx][0]
                harga = produk_vending[idx][1]
                subtotal = harga * qty
                total_bayar += subtotal
                print(f" - {nama} x{qty} @ Rp{harga} = Rp{subtotal}")
            print("-" * 40)
            print(f" TOTAL TAGIHAN: Rp{total_bayar}")
            print("="*40)

            print("\n [QRIS]")
            print(f"Silakan scan & bayar QRIS sebesar Rp{total_bayar}")
            konfirmasi = input("Konfirmasi Pembayaran? (y/n): ").strip().lower()

            if konfirmasi == 'y':
                for idx, qty in keranjang.items():
                    produk_vending[idx][2] -= qty
                    produk_vending[idx][3] += qty
                print("\n[✓] TRANSAKSI SUKSES! Silakan ambil semua barang kamu.")
            else:
                print("\n[X] PEMBAYARAN DIBATALKAN/GAGAL.")
        else:
            print("\n[*] Keranjang belanja kosong. Kembali ke menu utama.")

    elif pilihan == "2":
        print("\n" + "="*40)
        print("       PROSES PENUTUPAN HARI (PEMILIK)")
        print("="*40)

        # 1. Perhitungan Keuntungan Harian
        print("\n--- LAPORAN KEUNTUNGAN HARIAN ---")
        total_keuntungan = 0
        for i in range(N):
            pendapatan_item = produk_vending[i][1] * produk_vending[i][3]
            total_keuntungan += pendapatan_item
            print(f" - {produk_vending[i][0]}: Terjual {produk_vending[i][3]} pcs | Omset: Rp{pendapatan_item}")
        print("-" * 40)
        print(f" TOTAL KEUNTUNGAN HARI INI: Rp{total_keuntungan}")

        # 2. Restock Produk Terlaris (+5 Pcs)
        print("\n--- EVALUASI RESTOCK STOK ---")
        indeks_terlaris = 0
        maks_terjual = produk_vending[0][3]

        for i in range(N):
            if produk_vending[i][3] > maks_terjual:
                maks_terjual = produk_vending[i][3]
                indeks_terlaris = i

        produk_vending[indeks_terlaris][2] += 5
        print(f"[*] Produk Terlaris: {produk_vending[indeks_terlaris][0]} (Terjual {produk_vending[indeks_terlaris][3]} pcs). Otomatis ditambah +5 pcs stok.")

        # 3. Refill Stok Habis (Stok == 0 -> +10 Pcs)
        stok_habis = False
        for i in range(N):
            if produk_vending[i][2] == 0:
                produk_vending[i][2] += 10
                print(f"[*] Stok {produk_vending[i][0]} habis (0 pcs)! Pemilik melakukan refill +10 pcs.")
                stok_habis = True

        if not stok_habis:
            print("[*] Tidak ada barang lain yang stoknya habis (0 pcs).")

    elif pilihan == "3":
        print("\n Mematikan mesin... Terima kasih!")
        status_mesinmenyala = False

    else:
        print("\n[!] Pilihan menu tidak valid!")