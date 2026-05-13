<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=0">
    <title>Summarecon Emerald Karawang | KPR Premium Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #fcfcfc; }
        .business-font { font-family: 'Inter', sans-serif; font-weight: 600; }
        .luxury-gradient { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); }
        .gold-accent { color: #c5a059; }
        .bg-gold { background-color: #c5a059; }
        
        input::-webkit-outer-spin-button,
        input::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
        
        .card-shadow { box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05); }
        
        #main-app { animation: fadeIn 0.6s ease-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .input-group label { display: block; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; color: #64748b; letter-spacing: 0.05em; margin-bottom: 4px; }
        .input-premium { width: 100%; border-bottom: 2px solid #e2e8f0; padding: 8px 0; font-size: 1.125rem; font-weight: 600; transition: all 0.3s; background: transparent; }
        .input-premium:focus { outline: none; border-color: #0f172a; }
    </style>
</head>
<body class="text-slate-900">

    <div id="login-screen" class="fixed inset-0 z-50 flex items-center justify-center luxury-gradient p-6">
        <div class="w-full max-w-md bg-white rounded-3xl p-10 shadow-2xl text-center">
            <div class="mb-8">
                <h1 class="text-2xl font-serif font-bold tracking-tight text-slate-900">PRIVATE ACCESS</h1>
                <p class="text-sm text-slate-500 mt-2">Summarecon Emerald Karawang Portfolio</p>
            </div>
            <div class="space-y-4">
                <input type="password" id="passInput" placeholder="Enter Security Code" 
                    class="w-full p-4 rounded-xl border border-slate-200 text-center text-lg focus:ring-2 focus:ring-slate-900 focus:outline-none">
                <button onclick="checkAuth()" 
                    class="w-full luxury-gradient text-white py-4 rounded-xl font-bold tracking-widest hover:opacity-90 transition transform active:scale-95">
                    UNLOCK SYSTEM
                </button>
            </div>
            <p id="errorMsg" class="text-red-500 mt-4 text-xs font-bold hidden">ACCESS DENIED. PLEASE CHECK YOUR CODE.</p>
        </div>
    </div>

    <div id="main-app" class="hidden min-h-screen pb-20">
        <nav class="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b px-6 py-4 flex justify-between items-center">
            <div>
                <span class="text-lg font-bold tracking-tighter uppercase">Summarecon <span class="font-light text-slate-400 italic">Emerald</span></span>
            </div>
            <div class="text-[10px] bg-slate-100 px-3 py-1 rounded-full font-mono font-bold text-slate-500">
                STATION: RuangMasbay2026
            </div>
        </nav>

        <div class="max-w-6xl mx-auto px-6 mt-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
                
                <div class="lg:col-span-5 space-y-8">
                    <section class="bg-white p-8 rounded-3xl card-shadow">
                        <h2 class="text-sm font-bold uppercase tracking-widest text-slate-400 mb-8 border-b pb-4">Simulasi KPR Reguler</h2>
                        
                        <div class="space-y-6">
                            <div class="input-group">
                                <label>Harga Properti (Exclude PPN)</label>
                                <div class="relative">
                                    <span class="absolute left-0 top-2 font-bold text-slate-400 text-lg">Rp</span>
                                    <input type="number" id="basePrice" value="1000000000" oninput="calculate()" class="input-premium pl-8">
                                </div>
                            </div>

                            <div class="grid grid-cols-2 gap-6">
                                <div class="input-group">
                                    <label>Booking Fee</label>
                                    <input type="number" id="bookingFee" value="10000000" oninput="calculate()" class="input-premium">
                                </div>
                                <div class="input-group">
                                    <label>Down Payment (%)</label>
                                    <input type="number" id="dpPercent" value="10" oninput="calculate()" class="input-premium">
                                </div>
                            </div>

                            <div class="grid grid-cols-2 gap-6">
                                <div class="input-group">
                                    <label>Tenor (1-30 Tahun)</label>
                                    <input type="number" id="tenor" value="15" min="1" max="30" oninput="calculate()" class="input-premium">
                                </div>
                                <div class="input-group">
                                    <label>Suku Bunga (% p.a)</label>
                                    <input type="number" id="interest" step="0.1" value="5.5" oninput="calculate()" class="input-premium">
                                </div>
                            </div>

                            <div class="input-group">
                                <label>Biaya Akad (1% - 5%)</label>
                                <input type="number" id="akadPercent" value="3" min="1" max="5" oninput="calculate()" class="input-premium">
                            </div>
                        </div>
                    </section>
                </div>

                <div class="lg:col-span-7 space-y-6">
                    <div class="luxury-gradient rounded-3xl p-10 text-white shadow-xl relative overflow-hidden">
                        <div class="relative z-10">
                            <p class="text-xs font-bold uppercase tracking-[0.2em] opacity-60 mb-2">Estimasi Angsuran / Bulan</p>
                            <h3 id="monthlyInstallment" class="text-5xl md:text-6xl font-bold tracking-tight mb-8">Rp 0</h3>
                            
                            <div class="grid grid-cols-2 gap-4 border-t border-white/10 pt-6">
                                <div>
                                    <p class="text-[10px] uppercase opacity-50">Harga (Include PPN 11%)</p>
                                    <p id="incPPN" class="text-lg font-semibold">Rp 0</p>
                                </div>
                                <div class="text-right">
                                    <p class="text-[10px] uppercase opacity-50">Total Pinjaman (Plafon)</p>
                                    <p id="plafon" class="text-lg font-semibold text-gold-accent">Rp 0</p>
                                </div>
                            </div>
                        </div>
                        <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-white/5 rounded-full blur-3xl"></div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white p-6 rounded-2xl card-shadow border-t-4 border-slate-900">
                            <h4 class="text-xs font-bold uppercase text-slate-400 mb-4">Biaya Legal & Surat</h4>
                            <div class="space-y-3 text-sm">
                                <div class="flex justify-between border-b pb-2">
                                    <span class="text-slate-500">AJB (0.5%)</span>
                                    <span id="resAJB" class="font-bold text-slate-800">Rp 0</span>
                                </div>
                                <div class="flex justify-between border-b pb-2">
                                    <span class="text-slate-500">BPHTB (5%)</span>
                                    <span id="resBPHTB" class="font-bold text-slate-800">Rp 0</span>
                                </div>
                                <div class="flex justify-between pt-1">
                                    <span class="font-bold">Total Biaya Surat</span>
                                    <span id="totalSurat" class="font-bold text-slate-900">Rp 0</span>
                                </div>
                            </div>
                        </div>

                        <div class="bg-white p-6 rounded-2xl card-shadow border-t-4 border-slate-900">
                            <h4 class="text-xs font-bold uppercase text-slate-400 mb-4">Estimasi Akad KPR</h4>
                            <div class="space-y-3 text-sm">
                                <div class="flex justify-between border-b pb-2">
                                    <span class="text-slate-500">Provisi, Admin, Asuransi</span>
                                    <span id="resAkad" class="font-bold text-slate-800">Rp 0</span>
                                </div>
                                <p class="text-[10px] text-slate-400 italic">*Biaya bersifat estimasi sesuai kebijakan bank.</p>
                            </div>
                        </div>
                    </div>

                    <div class="bg-white rounded-3xl card-shadow overflow-hidden">
                        <div class="p-6 border-b flex justify-between items-center">
                            <h4 class="text-xs font-bold uppercase tracking-widest text-slate-400">Tabel Amortisasi Bank (Tahun ke-1)</h4>
                        </div>
                        <div class="overflow-x-auto">
                            <table class="w-full text-left text-sm">
                                <thead class="bg-slate-50 text-slate-500 uppercase text-[10px] tracking-wider">
                                    <tr>
                                        <th class="px-6 py-4 font-bold">Bulan</th>
                                        <th class="px-6 py-4 font-bold">Cicilan Pokok</th>
                                        <th class="px-6 py-4 font-bold">Cicilan Bunga</th>
                                        <th class="px-6 py-4 font-bold text-right">Sisa Pinjaman</th>
                                    </tr>
                                </thead>
                                <tbody id="amortizationTable" class="divide-y divide-slate-100"></tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function checkAuth() {
            const pass = document.getElementById('passInput').value;
            if(pass === "RuangMasbay2026") {
                document.getElementById('login-screen').classList.add('hidden');
                document.getElementById('main-app').classList.remove('hidden');
                calculate();
            } else {
                document.getElementById('errorMsg').classList.remove('hidden');
            }
        }

        // Trigger login on Enter key
        document.getElementById('passInput').addEventListener('keypress', function (e) {
            if (e.key === 'Enter') checkAuth();
        });

        function formatIDR(val) {
            return new Intl.NumberFormat('id-ID', { 
                style: 'currency', 
                currency: 'IDR', 
                maximumFractionDigits: 0 
            }).format(val);
        }

        function calculate() {
            const basePrice = parseFloat(document.getElementById('basePrice').value) || 0;
            const booking = parseFloat(document.getElementById('bookingFee').value) || 0;
            const dpPct = parseFloat(document.getElementById('dpPercent').value) || 0;
            const tenorYear = parseFloat(document.getElementById('tenor').value) || 0;
            const rateYear = parseFloat(document.getElementById('interest').value) || 0;
            const akadPct = parseFloat(document.getElementById('akadPercent').value) || 0;

            const priceIncPPN = basePrice * 1.11;
            const totalDPRequired = (priceIncPPN * (dpPct/100));
            const plafon = priceIncPPN - totalDPRequired;
            const ajb = basePrice * 0.005;
            const bphtb = basePrice * 0.05;
            const akadCost = plafon * (akadPct/100);

            const r = (rateYear / 100) / 12;
            const n = tenorYear * 12;
            let monthly = 0;
            if (r > 0) {
                monthly = plafon * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1);
            } else {
                monthly = n > 0 ? plafon / n : 0;
            }

            document.getElementById('incPPN').innerText = formatIDR(priceIncPPN);
            document.getElementById('monthlyInstallment').innerText = formatIDR(monthly);
            document.getElementById('plafon').innerText = formatIDR(plafon);
            document.getElementById('resAJB').innerText = formatIDR(ajb);
            document.getElementById('resBPHTB').innerText = formatIDR(bphtb);
            document.getElementById('totalSurat').innerText = formatIDR(ajb + bphtb);
            document.getElementById('resAkad').innerText = formatIDR(akadCost);

            let tableHTML = "";
            let currentBalance = plafon;
            for(let i = 1; i <= Math.min(n, 12); i++) {
                let interestPayment = currentBalance * r;
                let principalPayment = monthly - interestPayment;
                currentBalance -= principalPayment;
                
                tableHTML += `
                    <tr class="hover:bg-slate-50 transition">
                        <td class="px-6 py-4 font-bold text-slate-400">${i}</td>
                        <td class="px-6 py-4 text-slate-700">${formatIDR(principalPayment)}</td>
                        <td class="px-6 py-4 text-slate-700">${formatIDR(interestPayment)}</td>
                        <td class="px-6 py-4 text-right font-semibold text-slate-900">${formatIDR(Math.max(0, currentBalance))}</td>
                    </tr>
                `;
            }
            document.getElementById('amortizationTable').innerHTML = tableHTML;
        }
    </script>
</body>
</html>
