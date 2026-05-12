import pandas as pd
import numpy as np

def hitung_npv_kpr():
    print("=== KPR NPV ANALYZER ===")
    
    # --- INPUT HARGA & PPN ---
    harga_dasar = 1000000000  # 1 Milyar
    inc_ppn_harga = False     # Set True jika harga sudah termasuk PPN
    inc_ppn_utj = True        # Set True jika UTJ sudah termasuk PPN
    ppn_rate = 0.11

    # --- KOMPONEN BIAYA ---
    utj = 10000000            # Uang Tanda Jadi
    persen_dp = 0.10          # DP 10%
    tenor_cicil_dp = 6        # DP dicicil berapa bulan? (Isi 1 jika cash)
    bunga_kpr_anual = 0.05    # Bunga Bank 5%
    tenor_kpr_tahun = 20      # Tenor KPR
    
    # --- PERHITUNGAN DASAR ---
    harga_jual = harga_dasar if inc_ppn_harga else harga_dasar * (1 + ppn_rate)
    utj_bersih = utj / (1 + ppn_rate) if inc_ppn_utj else utj
    
    total_dp_nominal = harga_jual * persen_dp
    sisa_dp_setelah_utj = total_dp_nominal - utj_bersih
    cicilan_dp_per_bulan = sisa_dp_setelah_utj / tenor_cicil_dp
    
    plafon_kpr = harga_jual - total_dp_nominal
    biaya_akad = 0.05 * plafon_kpr
    biaya_ajb = 0.005 * harga_jual
    biaya_bphtb = 0.05 * (harga_jual - 60000000)
    
    # --- PEMBENTUKAN CASHFLOW ---
    # Bulan 0: UTJ + Biaya Akad + AJB + BPHTB
    cf_awal = utj + biaya_akad + biaya_ajb + biaya_bphtb
    
    # Masa Cicil DP
    cf_dp = [cicilan_dp_per_bulan] * tenor_cicil_dp
    
    # Masa Cicil KPR
    n_kpr = tenor_kpr_tahun * 12
    i_kpr = bunga_kpr_anual / 12
    cicilan_kpr = plafon_kpr * (i_kpr / (1 - (1 + i_kpr)**-n_kpr))
    cf_kpr = [cicilan_kpr] * n_kpr
    
    # Gabungkan semua pengeluaran (Cash Outflow)
    full_cashflow = [cf_awal] + cf_dp + cf_kpr
    
    # --- ANALISIS NPV ---
    discount_rates = [0.09, 0.095, 0.10, 0.105, 0.11, 0.115, 0.12]
    hasil_npv = []

    for dr in discount_rates:
        dr_bulanan = dr / 12
        # Rumus NPV: Σ (CFt / (1 + r)^t)
        npv_val = sum([val / (1 + dr_bulanan)**t for t, val in enumerate(full_cashflow)])
        
        hasil_npv.append({
            "Discount Rate (%)": f"{dr*100}%",
            "NPV (Nilai Sekarang)": f"Rp {npv_val:,.0f}",
            "Selisih vs Harga Jual": f"Rp {npv_val - harga_jual:,.0f}"
        })

    # --- OUTPUT ---
    df = pd.DataFrame(hasil_npv)
    print(f"\nRingkasan Properti:")
    print(f"Harga Jual Final: Rp {harga_jual:,.0f}")
    print(f"Plafon KPR: Rp {plafon_kpr:,.0f}")
    print(f"Cicilan KPR/Bulan: Rp {cicilan_kpr:,.0f}")
    print(f"Total Cashflow Awal (Bln 0): Rp {cf_awal:,.0f}")
    print("-" * 50)
    print(df.to_string(index=False))

if __name__ == "__main__":
    hitung_npv_kpr()
