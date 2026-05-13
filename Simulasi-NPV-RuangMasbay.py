import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi dasar Streamlit agar tampilan penuh (Wide Mode)
st.set_page_config(
    page_title="Elite KPR Simulator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Menghilangkan padding bawaan Streamlit agar tampilan HTML kita bersih
st.markdown("""
    <style>
        .block-container { padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

# Variabel berisi kode HTML/JS Mewah yang tadi
html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #fcfcfc; margin: 0; }
        .luxury-gradient { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); }
        input::-webkit-outer-spin-button, input::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
        .input-premium { width: 100%; border-bottom: 2px solid #e2e8f0; padding: 8px 0; font-size: 1.125rem; font-weight: 600; transition: all 0.3s; background: transparent; outline: none; }
        .input-premium:focus { border-color: #0f172a; }
        .card-shadow { box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05); }
    </style>
</head>
<body>
    <div id="login-screen" class="fixed inset-0 z-50 flex items-center justify-center luxury-gradient">
        <div class="w-full max-w-md bg-white rounded-3xl p-10 text-center shadow-2xl mx-4">
            <h1 class="text-2xl font-serif font-bold text-slate-900">PRIVATE ACCESS</h1>
            <p class="text-sm text-slate-500 mb-8 mt-2">Summarecon Emerald Karawang</p>
            <input type="password" id="passInput" placeholder="Security Code" class="w-full p-4 rounded-xl border mb-4 text-center text-lg">
            <button onclick="checkAuth()" class="w-full luxury-gradient text-white py-4 rounded-xl font-bold tracking-widest">UNLOCK SYSTEM</button>
            <p id="errorMsg" class="text-red-500 mt-4 text-xs font-bold hidden">WRONG PASSWORD</p>
        </div>
    </div>

    <div id="main-app" class="hidden min-h-screen">
        <nav class="bg-white border-b px-6 py-4 flex justify-between items-center sticky top-0 z-40">
            <span class="font-bold uppercase tracking-tighter text-lg">Elite <span class="font-light text-slate-400">KPR</span></span>
            <span class="text-[10px] bg-slate-100 px-3 py-1 rounded-full text-slate-500 font-bold uppercase">RuangMasbay2026</span>
        </nav>

        <div class="max-w-6xl mx-auto p-6 space-y-8 mt-4">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
                <div class="lg:col-span-5 space-y-6">
                    <div class="bg-white p-8 rounded-3xl card-shadow">
                        <h2 class="text-xs font-bold uppercase text-slate-400 mb-6 tracking-widest">Parameters</h2>
                        <div class="space-y-6">
                            <div>
                                <label class="text-[10px] font-bold text-slate-500 uppercase">Harga Properti (Exc. PPN)</label>
                                <input type="number" id="basePrice" value="1000000000" oninput="calculate()" class="input-premium">
                            </div>
                            <div class="grid grid-cols-2 gap-4">
                                <div><label class="text-[10px] font-bold text-slate-500 uppercase">Booking Fee</label><input type="number" id="booking" value="10000000" oninput="calculate()" class="input-premium text-sm"></div>
                                <div><label class="text-[10px] font-bold text-slate-500 uppercase">DP (%)</label><input type="number" id="dp" value="10" oninput="calculate()" class="input-premium text-sm"></div>
                            </div>
                            <div class="grid grid-cols-2 gap-4">
                                <div><label class="text-[10px] font-bold text-slate-500 uppercase">Tenor (Thn)</label><input type="number" id="tenor" value="15" oninput="calculate()" class="input-premium text-sm"></div>
                                <div><label class="text-[10px] font-bold text-slate-500 uppercase">Bunga (%)</label><input type="number" id="rate" value="5.5" oninput="calculate()" class="input-premium text-sm"></div>
                            </div>
                            <div><label class="text-[10px] font-bold text-slate-500 uppercase">Biaya Akad (%)</label><input type="number" id="akad" value="3" oninput="calculate()" class="input-premium text-sm"></div>
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-7 space-y-6">
                    <div class="luxury-gradient rounded-3xl p-8 text-white shadow-xl">
                        <p class="text-[10px] uppercase tracking-widest opacity-60 mb-2">Angsuran / Bulan</p>
                        <h3 id="monthlyInstallment" class="text-5xl font-bold mb-6">Rp 0</h3>
                        <div class="grid grid-cols-2 gap-4 border-t border-white/10 pt-4 text-sm">
                            <div><p class="opacity-50 text-[10px] uppercase">Inc. PPN (11%)</p><p id="incPPN" class="font-semibold"></p></div>
                            <div class="text-right"><p class="opacity-50 text-[10px] uppercase">Plafon KPR</p><p id="plafon" class="font-semibold text-yellow-500"></p></div>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-white p-5 rounded-2xl card-shadow border-t-2 border-slate-800">
                            <p class="text-[10px] uppercase font-bold text-slate-400 mb-2">Legal (AJB & BPHTB)</p>
                            <p id="totalSurat" class="text-lg font-bold text-slate-800"></p>
                        </div>
                        <div class="bg-white p-5 rounded-2xl card-shadow border-t-2 border-slate-800">
                            <p class="text-[10px] uppercase font-bold text-slate-400 mb-2">Est. Biaya Akad</p>
                            <p id="resAkad" class="text-lg font-bold text-slate-800"></p>
                        </div>
                    </div>

                    <div class="bg-white rounded-3xl card-shadow overflow-hidden">
                        <div class="bg-slate-50 p-4 border-b"><p class="text-[10px] font-bold uppercase text-slate-500">Amortisasi (Tahun 1)</p></div>
                        <table class="w-full text-xs text-left">
                            <tbody id="amortTable" class="divide-y"></tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function checkAuth() {
            if(document.getElementById('passInput').value === "RuangMasbay2026") {
                document.getElementById('login-screen').classList.add('hidden');
                document.getElementById('main-app').classList.remove('hidden');
                calculate();
            } else {
                document.getElementById('errorMsg').classList.remove('hidden');
            }
        }

        function formatIDR(val) {
            return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', maximumFractionDigits: 0 }).format(val);
        }

        function calculate() {
            const price = parseFloat(document.getElementById('basePrice').value) || 0;
            const dpPct = parseFloat(document.getElementById('dp').value) || 0;
            const incPPN = price * 1.11;
            const plafon = incPPN - (incPPN * dpPct/100);
            const r = (parseFloat(document.getElementById('rate').value) / 100) / 12;
            const n = (parseFloat(document.getElementById('tenor').value) || 0) * 12;

            let monthly = r > 0 ? plafon * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1) : plafon/n;

            document.getElementById('incPPN').innerText = formatIDR(incPPN);
            document.getElementById('monthlyInstallment').innerText = formatIDR(monthly);
            document.getElementById('plafon').innerText = formatIDR(plafon);
            document.getElementById('totalSurat').innerText = formatIDR(price * 0.055);
            document.getElementById('resAkad').innerText = formatIDR(plafon * (document.getElementById('akad').value/100));

            let tableHTML = "";
            let balance = plafon;
            for(let i=1; i<=12; i++) {
                let bunga = balance * r;
                let pokok = monthly - bunga;
                balance -= pokok;
                tableHTML += `<tr class="p-4"><td class="p-3 font-bold text-slate-400">${i}</td><td class="p-3 text-slate-600">Pokok: ${formatIDR(pokok)}</td><td class="p-3 text-right font-semibold">${formatIDR(Math.max(0, balance))}</td></tr>`;
            }
            document.getElementById('amortTable').innerHTML = tableHTML;
        }
    </script>
</body>
</html>
"""

# Menampilkan kode HTML ke dalam aplikasi Streamlit
components.html(html_content, height=1500, scrolling=True)
