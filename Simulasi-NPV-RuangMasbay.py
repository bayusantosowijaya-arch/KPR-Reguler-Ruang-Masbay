import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Elite KPR Simulator", layout="wide")

st.markdown("""
    <style>
        .block-container { padding: 0rem; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #f8fafc; margin: 0; }
        .luxury-card { background: white; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.02); border: 1px solid #f1f5f9; }
        .dark-card { background: #0f172a; color: white; border-radius: 24px; }
        .input-premium { width: 100%; border-bottom: 2px solid #e2e8f0; padding: 10px 0; font-size: 1.25rem; font-weight: 700; outline: none; transition: 0.3s; background: transparent; }
        .input-premium:focus { border-color: #0f172a; }
        .label-style { font-size: 11px; font-weight: 800; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.05em; }
        .highlight-gold { color: #eab308; }
    </style>
</head>
<body>

    <div id="login-screen" class="fixed inset-0 z-50 flex items-center justify-center bg-[#0f172a]">
        <div class="w-full max-w-md bg-white rounded-3xl p-10 text-center mx-4">
            <h1 class="text-2xl font-bold text-slate-900">PRIVATE ACCESS</h1>
            <p class="text-sm text-slate-400 mb-8 mt-1">Portfolio Masbay 2026</p>
            <input type="password" id="passInput" placeholder="Password" class="w-full p-4 rounded-xl border mb-4 text-center">
            <button onclick="checkAuth()" class="w-full bg-[#0f172a] text-white py-4 rounded-xl font-bold">LOG IN</button>
        </div>
    </div>

    <div id="main-app" class="hidden min-h-screen pb-20">
        <nav class="bg-white border-b px-6 py-5 flex justify-between items-center sticky top-0 z-40">
            <span class="font-bold tracking-tighter text-xl">ELITE<span class="text-slate-300 italic">KPR</span></span>
            <div class="text-[10px] bg-slate-100 px-3 py-1 rounded-full font-bold">STATION: RuangMasbay2026</div>
        </nav>

        <div class="max-w-6xl mx-auto p-6 mt-6 grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div class="lg:col-span-5 space-y-6">
                <div class="luxury-card p-8">
                    <h2 class="label-style mb-8 border-b pb-4">Parameter Simulasi</h2>
                    
                    <div class="space-y-8">
                        <div>
                            <label class="label-style">Harga Properti (Exclude PPN)</label>
                            <div class="flex items-center border-b-2 border-slate-200 focus-within:border-slate-900 transition">
                                <span class="text-xl font-bold text-slate-400">Rp</span>
                                <input type="text" id="rawPrice" value="2.500.000.000" oninput="handleInput(this)" class="w-full p-3 text-xl font-bold outline-none bg-transparent">
                            </div>
                            <p class="text-[11px] text-slate-400 mt-2 italic">Harga Inc PPN (11%): <span id="incPPNLabel" class="font-bold text-slate-600">Rp 0</span></p>
                        </div>

                        <div class="grid grid-cols-2 gap-6">
                            <div>
                                <label class="label-style">Booking Fee (UTJ)</label>
                                <input type="text" id="rawBooking" value="10.000.000" oninput="handleInput(this)" class="input-premium">
                            </div>
                            <div>
                                <label class="label-style">Down Payment (%)</label>
                                <input type="number" id="dpPct" value="10" oninput="calculate()" class="input-premium">
                                <p id="dpNominal" class="text-[10px] font-bold text-blue-600 mt-1">Rp 0</p>
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-6">
                            <div>
                                <label class="label-style">Tenor (Tahun)</label>
                                <input type="number" id="tenor" value="15" oninput="calculate()" class="input-premium">
                            </div>
                            <div>
                                <label class="label-style">Suku Bunga (% p.a)</label>
                                <input type="number" id="rate" value="4.75" step="0.01" oninput="calculate()" class="input-premium">
                            </div>
                        </div>

                        <div>
                            <label class="label-style">Biaya Akad KPR (%)</label>
                            <input type="number" id="akadPct" value="5" oninput="calculate()" class="input-premium">
                            <p id="akadNominal" class="text-[10px] font-bold text-slate-500 mt-1">Estimasi: Rp 0</p>
                        </div>
                    </div>
                </div>

                <div class="p-6 bg-blue-50 rounded-2xl border border-blue-100">
                    <p class="text-[11px] text-blue-800 leading-relaxed italic">
                        <b>Note:</b> Uang Tanda Jadi (Booking Fee) bersifat mengurangi nilai pembayaran Down Payment (DP) atau harga jual saat pelunasan.
                    </p>
                </div>
            </div>

            <div class="lg:col-span-7 space-y-6">
                <div class="dark-card p-10 shadow-2xl relative overflow-hidden">
                    <div class="relative z-10">
                        <p class="label-style text-slate-400 mb-2">Estimasi Angsuran / Bulan</p>
                        <h3 id="monthlyInstallment" class="text-5xl md:text-6xl font-bold tracking-tight text-white">Rp 0</h3>
                        
                        <div class="grid grid-cols-2 gap-6 mt-10 pt-8 border-t border-white/10">
                            <div>
                                <p class="text-[10px] uppercase opacity-50">Plafon Kredit (Bank)</p>
                                <p id="plafon" class="text-lg font-bold highlight-gold">Rp 0</p>
                            </div>
                            <div class="text-right">
                                <p class="text-[10px] uppercase opacity-50">Total Pinjaman</p>
                                <p id="totalLoan" class="text-lg font-bold">Rp 0</p>
                            </div>
                        </div>
                    </div>
                    <div class="absolute -right-20 -bottom-20 w-80 h-80 bg-blue-500/10 rounded-full blur-3xl"></div>
                </div>

                <div class="grid grid-cols-2 gap-4">
                    <div class="luxury-card p-6">
                        <p class="label-style mb-1 text-slate-400">BPHTB & AJB (Est)</p>
                        <p id="resLegal" class="text-xl font-bold text-slate-800">Rp 0</p>
                        <p class="text-[9px] text-slate-400 mt-1 italic">*Estimasi 5.5% dari harga jual</p>
                    </div>
                    <div class="luxury-card p-6">
                        <p class="label-style mb-1 text-slate-400">Total Biaya Akad</p>
                        <p id="resAkadTotal" class="text-xl font-bold text-slate-800">Rp 0</p>
                        <p class="text-[9px] text-slate-400 mt-1 italic">*Provisi, Admin, Asuransi</p>
                    </div>
                </div>

                <div class="luxury-card overflow-hidden">
                    <div class="p-6 border-b bg-slate-50">
                        <p class="label-style">Tabel Amortisasi (Tahun 1)</p>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-sm">
                            <thead class="bg-slate-50 text-[10px] uppercase text-slate-400">
                                <tr>
                                    <th class="px-6 py-3">Bln</th>
                                    <th class="px-6 py-3">Pokok</th>
                                    <th class="px-6 py-3 text-right">Sisa Pinjaman</th>
                                </tr>
                            </thead>
                            <tbody id="amortTable" class="divide-y divide-slate-100"></tbody>
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
            }
        }

        // Fungsi format ribuan (titik)
        function formatNumber(n) {
            return n.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        }

        function parseNumber(s) {
            return parseFloat(s.replace(/\./g, "")) || 0;
        }

        function formatIDR(val) {
            return "Rp " + new Intl.NumberFormat('id-ID', { maximumFractionDigits: 0 }).format(val);
        }

        function handleInput(el) {
            let cursorPosition = el.selectionStart;
            let originalLength = el.value.length;
            el.value = formatNumber(el.value);
            let newLength = el.value.length;
            el.selectionEnd = cursorPosition + (newLength - originalLength);
            calculate();
        }

        function calculate() {
            const price = parseNumber(document.getElementById('rawPrice').value);
            const booking = parseNumber(document.getElementById('rawBooking').value);
            const dpPct = parseFloat(document.getElementById('dpPct').value) || 0;
            const tenor = parseFloat(document.getElementById('tenor').value) || 0;
            const rate = parseFloat(document.getElementById('rate').value) || 0;
            const akadPct = parseFloat(document.getElementById('akadPct').value) || 0;

            const incPPN = price * 1.11;
            const dpNominal = incPPN * (dpPct / 100);
            const plafon = incPPN - dpNominal;
            const akadCost = plafon * (akadPct / 100);
            
            // Cicilan
            const r = (rate / 100) / 12;
            const n = tenor * 12;
            const monthly = r > 0 ? plafon * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1) : plafon/n;

            // Update UI
            document.getElementById('incPPNLabel').innerText = formatIDR(incPPN);
            document.getElementById('dpNominal').innerText = "Setara: " + formatIDR(dpNominal);
            document.getElementById('akadNominal').innerText = "Estimasi: " + formatIDR(akadCost);
            document.getElementById('monthlyInstallment').innerText = formatIDR(monthly);
            document.getElementById('plafon').innerText = formatIDR(plafon);
            document.getElementById('totalLoan').innerText = formatIDR(plafon);
            document.getElementById('resLegal').innerText = formatIDR(price * 0.055);
            document.getElementById('resAkadTotal').innerText = formatIDR(akadCost);

            // Table
            let tableHTML = "";
            let balance = plafon;
            for(let i=1; i<=12; i++) {
                let bungaBln = balance * r;
                let pokokBln = monthly - bungaBln;
                balance -= pokokBln;
                tableHTML += `<tr class="hover:bg-slate-50"><td class="px-6 py-4 font-bold text-slate-400">${i}</td><td class="px-6 py-4">${formatIDR(pokokBln)}</td><td class="px-6 py-4 text-right font-bold">${formatIDR(Math.max(0, balance))}</td></tr>`;
            }
            document.getElementById('amortTable').innerHTML = tableHTML;
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=1800, scrolling=True)
