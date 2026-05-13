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
        body { font-family: 'Inter', sans-serif; background: #f8fafc; margin: 0; overflow-x: hidden; }
        .luxury-card { background: white; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.02); border: 1px solid #f1f5f9; }
        .dark-card { background: #0f172a; color: white; border-radius: 24px; }
        .input-premium { width: 100%; border-bottom: 2px solid #e2e8f0; padding: 10px 0; font-size: 1.25rem; font-weight: 700; outline: none; transition: 0.3s; background: transparent; }
        .input-premium:focus { border-color: #0f172a; }
        .label-style { font-size: 11px; font-weight: 800; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.05em; }
        .highlight-gold { color: #eab308; }
        
        /* Animasi Running Text */
        .marquee-container {
            overflow: hidden;
            background: #f1f5f9;
            padding: 8px 0;
            border-bottom: 1px solid #e2e8f0;
            display: none; /* Sembunyi dulu sebelum login */
        }
        .marquee-text {
            white-space: nowrap;
            display: inline-block;
            padding-left: 100%;
            animation: marquee 15s linear infinite;
            font-size: 12px;
            font-weight: 700;
            color: #475569;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        @keyframes marquee {
            0% { transform: translate(0, 0); }
            100% { transform: translate(-100%, 0); }
        }

        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #f1f1f1; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
    </style>
</head>
<body>

    <div id="login-screen" class="fixed inset-0 z-50 flex items-center justify-center bg-[#0f172a]">
        <div class="w-full max-w-md bg-white rounded-3xl p-10 text-center mx-4 shadow-2xl">
            <h1 class="text-2xl font-bold text-slate-900">PRIVATE ACCESS</h1>
            <p class="text-sm text-slate-400 mb-8 mt-1">Summarecon Emerald Karawang</p>
            <input type="password" id="passInput" placeholder="Security Code" class="w-full p-4 rounded-xl border mb-4 text-center outline-none">
            <button onclick="checkAuth()" class="w-full bg-[#0f172a] text-white py-4 rounded-xl font-bold hover:bg-slate-800 transition">ACCESS SYSTEM</button>
        </div>
    </div>

    <div id="main-app" class="hidden min-h-screen pb-20">
        <nav class="bg-white border-b px-6 py-5 flex justify-between items-center sticky top-0 z-40">
            <span class="font-bold tracking-tighter text-xl text-slate-900">ELITE<span class="text-slate-300 italic font-light">KPR</span></span>
            <div class="text-[10px] bg-slate-100 px-3 py-1 rounded-full font-bold text-slate-500 uppercase italic">Digital Analyst System</div>
        </nav>

        <div id="marquee" class="marquee-container">
            <div class="marquee-text">
                +++ Ruang Masbay 2026 Property Intelegent System +++ Authorized Access +++ Summarecon Emerald Karawang High-End Residential Project +++ Digital Marketing Tool +++
            </div>
        </div>

        <div class="max-w-6xl mx-auto p-6 mt-6 grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div class="lg:col-span-5 space-y-6">
                <div class="luxury-card p-8">
                    <h2 class="label-style mb-8 border-b pb-4">Input Data Properti</h2>
                    <div class="space-y-8">
                        <div>
                            <label class="label-style">Harga Properti (Inc PPN 11%)</label>
                            <div class="flex items-center border-b-2 border-slate-200 focus-within:border-slate-900 transition">
                                <span class="text-xl font-bold text-slate-400 mr-2">Rp</span>
                                <input type="text" id="rawPriceInc" value="2.775.000.000" oninput="handleInput(this)" class="w-full p-2 text-2xl font-bold outline-none bg-transparent">
                            </div>
                            <p class="text-[11px] text-slate-400 mt-2">Harga Dasar (Excl. PPN): <span id="excPPNLabel" class="font-bold text-slate-600">Rp 0</span></p>
                        </div>
                        <div class="grid grid-cols-2 gap-6">
                            <div><label class="label-style">Booking Fee (UTJ)</label><input type="text" id="rawBooking" value="10.000.000" oninput="handleInput(this)" class="input-premium"></div>
                            <div><label class="label-style">DP (%)</label><input type="number" id="dpPct" value="10" oninput="calculate()" class="input-premium"><p id="dpNominal" class="text-[10px] font-bold text-blue-600 mt-1">Rp 0</p></div>
                        </div>
                        <div class="grid grid-cols-2 gap-6">
                            <div><label class="label-style">Tenor (Tahun)</label><input type="number" id="tenor" value="15" oninput="calculate()" class="input-premium"></div>
                            <div><label class="label-style">Bunga (% P.A)</label><input type="number" id="rate" value="4.75" step="0.01" oninput="calculate()" class="input-premium"></div>
                        </div>
                        <div><label class="label-style">Biaya Akad KPR (%)</label><input type="number" id="akadPct" value="5" oninput="calculate()" class="input-premium"><p id="akadNominal" class="text-[10px] font-bold text-slate-500 mt-1">Est: Rp 0</p></div>
                    </div>
                </div>
            </div>

            <div class="lg:col-span-7 space-y-6">
                <div class="dark-card p-10 shadow-xl relative overflow-hidden">
                    <div class="relative z-10">
                        <p class="label-style text-slate-400 mb-2 text-xs">Estimasi Angsuran / Bulan</p>
                        <h3 id="monthlyInstallment" class="text-5xl md:text-6xl font-bold tracking-tight text-white">Rp 0</h3>
                        <div class="grid grid-cols-2 gap-6 mt-10 pt-8 border-t border-white/10 text-sm">
                            <div><p class="text-[10px] uppercase opacity-50">Plafon Pinjaman</p><p id="plafon" class="text-xl font-bold highlight-gold">Rp 0</p></div>
                            <div class="text-right"><p class="text-[10px] uppercase opacity-50">Nilai Properti (Inc PPN)</p><p id="valInc" class="text-xl font-bold">Rp 0</p></div>
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="luxury-card p-6 border-t-4 border-slate-900"><p class="label-style mb-1 text-slate-400 font-bold">Legalitas (Est. 5.5%)</p><p id="resLegal" class="text-xl font-bold text-slate-800">Rp 0</p></div>
                    <div class="luxury-card p-6 border-t-4 border-slate-900"><p class="label-style mb-1 text-slate-400 font-bold">Total Biaya Akad</p><p id="resAkadTotal" class="text-xl font-bold text-slate-800">Rp 0</p></div>
                </div>
                <div class="luxury-card overflow-hidden h-[400px] flex flex-col">
                    <div class="p-6 border-b bg-slate-50 flex justify-between items-center"><p class="label-style">Tabel Amortisasi Full Tenor</p></div>
                    <div class="overflow-y-auto flex-grow"><table class="w-full text-left text-sm"><tbody id="amortTable" class="divide-y divide-slate-100"></tbody></table></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function checkAuth() {
            if(document.getElementById('passInput').value === "RuangMasbay2026") {
                document.getElementById('login-screen').classList.add('hidden');
                document.getElementById('main-app').classList.remove('hidden');
                document.getElementById('marquee').style.display = 'block'; // Aktifkan running text
                calculate();
            }
        }

        function formatNumber(n) { return n.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, "."); }
        function parseNumber(s) { return parseFloat(s.replace(/\./g, "")) || 0; }
        function formatIDR(val) { return "Rp " + new Intl.NumberFormat('id-ID', { maximumFractionDigits: 0 }).format(val); }

        function handleInput(el) {
            let cursor = el.selectionStart;
            let oldLen = el.value.length;
            el.value = formatNumber(el.value);
            let newLen = el.value.length;
            el.selectionEnd = cursor + (newLen - oldLen);
            calculate();
        }

        function calculate() {
            const priceInc = parseNumber(document.getElementById('rawPriceInc').value);
            const dpPct = parseFloat(document.getElementById('dpPct').value) || 0;
            const tenor = parseFloat(document.getElementById('tenor').value) || 0;
            const rate = parseFloat(document.getElementById('rate').value) || 0;
            const priceExc = priceInc / 1.11;
            const dpNominal = priceInc * (dpPct / 100);
            const plafon = priceInc - dpNominal;
            const r = (rate / 100) / 12;
            const n = tenor * 12;
            const monthly = r > 0 ? plafon * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1) : plafon/n;

            document.getElementById('excPPNLabel').innerText = formatIDR(priceExc);
            document.getElementById('valInc').innerText = formatIDR(priceInc);
            document.getElementById('dpNominal').innerText = "Setara: " + formatIDR(dpNominal);
            document.getElementById('monthlyInstallment').innerText = formatIDR(monthly);
            document.getElementById('plafon').innerText = formatIDR(plafon);
            document.getElementById('resLegal').innerText = formatIDR(priceExc * 0.055);
            document.getElementById('resAkadTotal').innerText = formatIDR(plafon * (document.getElementById('akadPct').value/100));

            let tableHTML = "";
            let balance = plafon;
            for(let i=1; i<=n; i++) {
                let intBln = balance * r;
                let prinBln = monthly - intBln;
                balance -= prinBln;
                tableHTML += `<tr><td class="px-6 py-3 font-bold text-slate-400 text-xs">${i}</td><td class="px-6 py-3 text-slate-600 text-xs">${formatIDR(prinBln)}</td><td class="px-6 py-3 text-right font-bold text-xs">${formatIDR(Math.max(0, balance))}</td></tr>`;
            }
            document.getElementById('amortTable').innerHTML = tableHTML;
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=2000, scrolling=True)
