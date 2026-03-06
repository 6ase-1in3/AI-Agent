<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>ISO 企業導入 AI 之戰略架構與實施路徑</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box }
        body { overflow: hidden; height: 100vh; font-family: 'Inter', system-ui, sans-serif }
        .presentation { width: 100vw; height: 100vh; display: flex; flex-direction: column }
        .main { flex: 1; display: flex; overflow: hidden }
        #toolbar { height: 44px; background: #1a1a2e; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; border-bottom: 1px solid rgba(255, 255, 255, .08); flex-shrink: 0 }
        #toolbar .left { display: flex; align-items: center; gap: 10px }
        #toolbar .right { display: flex; align-items: center; gap: 8px }
        #toolbar .title { color: rgba(255, 255, 255, .6); font-size: 13px }
        #toolbar button { background: rgba(255, 255, 255, .08); border: none; color: rgba(255, 255, 255, .8); padding: 5px 12px; font-size: 12px; cursor: pointer; border-radius: 4px; transition: background .2s }
        #toolbar button:hover { background: rgba(255, 255, 255, .2) }
        .nav-btn { width: 32px !important; height: 32px !important; padding: 0 !important; display: flex !important; align-items: center !important; justify-content: center !important; font-size: 16px !important }
        #toolbar .counter { color: rgba(255, 255, 255, .4); font-size: 12px; min-width: 55px; text-align: center; font-variant-numeric: tabular-nums }
        .slide-view { flex: 1; overflow: hidden; display: flex; align-items: center; justify-content: center; background: #2a2a3e }
        #slideContainer { transform-origin: center center }
        .thumbnail-nav { width: 300px; background: #1a1a2e; padding: 10px; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0 }
        .thumbnail-nav::-webkit-scrollbar { width: 4px }
        .thumbnail-nav::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, .15); border-radius: 2px }
        .thumb { aspect-ratio: 16/9; background: #252540; border: 2px solid transparent; border-radius: 6px; cursor: pointer; overflow: hidden; transition: all .15s; position: relative; flex-shrink: 0 }
        .thumb:hover { border-color: rgba(0, 217, 255, .4) }
        .thumb.active { border-color: #00d9ff; box-shadow: 0 0 8px rgba(0, 217, 255, .3) }
        .thumb-slide-wrapper { position: absolute; top: 0; left: 0; width: 1280px; height: 720px; transform: scale(0.215625); transform-origin: top left; pointer-events: none; background: #fff; }
        .thumb-overlay { position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(transparent, rgba(0, 0, 0, .65)); padding: 3px 6px; display: flex; justify-content: space-between; align-items: flex-end }
        .thumb-num { font-size: 10px; font-weight: 700; color: rgba(255, 255, 255, .8) }
        .thumb-label { font-size: 8px; color: rgba(255, 255, 255, .6); text-align: right; text-shadow: 0 1px 2px rgba(0, 0, 0, 0.8); }
        .slide { width: 1280px; height: 720px; position: relative; overflow: hidden; font-family: 'Inter', sans-serif; background: #fff; display: none }
        .slide.active { display: block }
        /* === Utility Classes === */
        .full { width: 100%; height: 100%; display: flex }
        .col { flex-direction: column }
        .center { justify-content: center; align-items: center }
        .t-xl { font-size: 64px; font-weight: 700; line-height: 1.2 }
        .t-lg { font-size: 48px; font-weight: 700 }
        .t-md { font-size: 32px; font-weight: 700; line-height: 1.3 }
        .t-sm { font-size: 20px; font-weight: 600 }
        .t-body { font-size: 16px; line-height: 1.6 }
        .t-sm2 { font-size: 14px; line-height: 1.5 }
        .c-blue { color: #00A3E0 }
        .c-orange { color: #FF6B35 }
        .c-gold { color: #D4AF37 }
        .c-dark { color: #1A2332 }
        .c-muted { color: #3D4A5C }
        .p { padding: 60px }
        .p-sm { padding: 20px }
        .p-md { padding: 40px }
        .gap { gap: 30px }
        .gap-sm { gap: 15px }
        .tag { display: inline-block; padding: 8px 16px; border: 1.5px solid #00A3E0; font-size: 13px; font-weight: 600 }
        .card { padding: 20px; border-left: 3px solid #00A3E0 }
        .box { padding: 16px; background: rgba(0, 163, 224, 0.08); border-left: 3px solid #00A3E0 }
        .line { width: 60px; height: 3px; background: linear-gradient(90deg, #00A3E0, #FF6B35) }
        .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 30px }
        .grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px }
        .grid4 { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 15px }
        .num { font-size: 48px; font-weight: 700; color: #00A3E0; opacity: 0.3 }
        .num-box { width: 36px; height: 36px; background: #00A3E0; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700 }
        .flex-1 { flex: 1 }
        .flex-60 { flex: 0 0 60% }
        .flex-40 { flex: 0 0 40% }
        .img-placeholder { background: #f0f0f0; display: flex; align-items: center; justify-content: center; color: transparent; font-size: 14px; position:relative; overflow:hidden;}
        .bg-grid { background-image: linear-gradient(transparent 24%, rgba(0, 163, 224, 0.05)25%, rgba(0, 163, 224, 0.05)26%, transparent 27%), linear-gradient(90deg, transparent 24%, rgba(0, 163, 224, 0.05)25%, rgba(0, 163, 224, 0.05)26%, transparent 27%); background-size: 60px 60px }
        .circle { width: 100px; height: 100px; border-radius: 50%; background: #00A3E0 }
        .bar { height: 8px; background: #00A3E0; border-radius: 4px }
        .corner { position: absolute; width: 40px; height: 40px; border: 2px solid #00A3E0 }
        .corner-tl { top: 30px; left: 30px; border-right: none; border-bottom: none }
        .corner-tr { top: 30px; right: 30px; border-left: none; border-bottom: none }
        .corner-bl { bottom: 30px; left: 30px; border-right: none; border-top: none }
        .corner-br { bottom: 30px; right: 30px; border-left: none; border-top: none }
        .phase { padding-top: 12px }
        .phase-label { color: #00A3E0; font-weight: 700; font-size: 20px; border-left: 4px solid #00A3E0; padding-left: 15px }
        .phase-desc { font-size: 16px; line-height: 1.6; color: #3D4A5C; padding: 4px 0 0 19px }
        .concept { display: flex; gap: 30px; align-items: flex-start; padding: 20px 25px; background: rgba(0, 163, 224, 0.04); border-left: 4px solid #00A3E0 }
        .insight { position: relative; padding: 25px; background: rgba(0, 163, 224, 0.05); border-top: 3px solid #00A3E0 }
        .insight::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: #FF6B35 }
        .icon-box { width: 60px; height: 60px; background: #f0f0f0; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0; color: #00A3E0 }
        .slide-badge { position: absolute; top: 10px; right: 15px; background: rgba(0, 163, 224, .1); color: #00A3E0; font-size: 11px; padding: 3px 10px; border-radius: 3px; font-weight: 600; letter-spacing: .5px; z-index: 5 }
    </style>
</head>

<body>
    <div class="presentation">
        <!-- Toolbar -->
        <div id="toolbar">
            <div class="left"><span class="title">📊 ISO 企業導入 AI 之戰略架構與實施路徑研究報告</span></div>
            <div style="display:flex;align-items:center;gap:6px">
                <button class="nav-btn" onclick="go(current-1)">◀</button>
                <span class="counter" id="counter">1 / 10</span>
                <button class="nav-btn" onclick="go(current+1)">▶</button>
            </div>
            <div class="right">
                <button onclick="toggleFullscreen()">⛶ 全螢幕</button>
                <button onclick="exportPDF()" id="pdfBtn">📥 下載 PDF</button>
            </div>
        </div>

        <!-- Main area -->
        <div class="main">
            <!-- Slide viewport -->
            <div class="slide-view">
                <div id="slideContainer">

                    <!-- Slide 01: 封面 -->
                    <div class="slide active" data-name="封面">
                        <div class="slide-badge" style="background:rgba(255,255,255,.15);color:rgba(255,255,255,.6)">#01 封面</div>
                        <div class="full col" style="background:#1A2332; justify-content:center; padding:0 100px; position:relative">
                            <div style="position:absolute; top:0; left:0; width:100%; height:100%; background: url('./cover_ai_governance_1771903978170.png') center/cover no-repeat; opacity: 0.35; z-index:0"></div>
                            <div style="position:absolute;top:-100px;right:-100px;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(0,163,224,0.2) 0%,transparent 70%); z-index:1"></div>
                            
                            <div class="line" style="background:linear-gradient(90deg,#FF6B35,#00A3E0); position:relative; z-index:2; height: 4px; width: 120px;"></div>
                            <h1 style="font-size:60px; font-weight:800; color:#fff; line-height:1.2; margin-top:30px; letter-spacing:-1px; position:relative; z-index:2; max-width:1080px;">
                                企業導入 AI 之<br/>戰略架構與實施路徑
                            </h1>
                            <p style="font-size:28px; font-weight:400; color:rgba(255,255,255,0.8); margin-top:25px; line-height:1.5; position:relative; z-index:2;">
                                AI 大腦與程式手腳的雙引擎協同作戰
                            </p>
                            
                            <div style="position:absolute;bottom:40px;left:100px;font-size:14px;color:rgba(255,255,255,0.6);display:flex;gap:30px; z-index:2; font-weight:500;">
                                <span> AI STRATEGY</span><span> PROCESS INTEGRATION</span>
                            </div>
                        </div>
                    </div>

                    <!-- Slide 02: 簡介 (AI 與程式系統 定義) -->
                    <div class="slide" data-name="簡介">
                        <div class="slide-badge">#02 簡介</div>
                        <div class="full" style="align-items:center">
                            <div class="flex-50 p" style="display:flex;flex-direction:column;justify-content:center; padding-right:40px; width: 50%;">
                                <div class="line"></div>
                                <h1 class="t-xl c-dark" style="margin-top:20px; font-size:48px;">AI大腦  系統手腳</h1>
                                <p class="t-md c-muted" style="margin-top:15px; font-weight:500; font-size: 24px;">雙引擎協同作戰定義</p>
                                
                                <div class="box" style="margin-top:35px; border-left:4px solid #FF6B35; background:rgba(255,107,53,0.05); padding: 25px;">
                                    <div style="font-size: 40px; margin-bottom: 10px;"></div>
                                    <h3 class="c-orange t-sm" style="margin-bottom: 5px;">AI 人工智慧 (大腦)</h3>
                                    <p class="t-body c-dark" style="font-size: 18px; line-height: 1.6;">專注於高價值的運算，將大數據進行<strong>分析、預測、決策</strong>的智慧系統。</p>
                                </div>
                            </div>
                            <div class="flex-50 p" style="display:flex;flex-direction:column;justify-content:center; padding-left:40px; background:#F8FAFC; height:100%; width: 50%;">
                                <div class="box" style="margin-top:0px; border-left:4px solid #00A3E0; background:rgba(0,163,224,0.05); padding: 25px;">
                                    <div style="font-size: 40px; margin-bottom: 10px;"></div>
                                    <h3 class="c-blue t-sm" style="margin-bottom: 5px;">程式系統 (手腳)</h3>
                                    <p class="t-body c-dark" style="font-size: 18px; line-height: 1.6;">負責自動化的體力活，將資料進行<strong>收集、整理、呈現</strong>的高效系統。</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Slide 03: 行銷部企劃案三大類型 -->
                    <div class="slide" data-name="企劃類型">
                        <div class="slide-badge">#03 企劃分類</div>
                        <div class="p bg-grid" style="height:100%">
                            <div class="line"></div>
                            <h1 class="t-lg c-dark" style="margin-top:15px">一、行銷部企劃案：三大戰略類型</h1>
                            <p class="t-sm2 c-blue" style="margin-top:10px; font-size:16px;">從被動接單到主動創造市場</p>
                            
                            <div class="grid3" style="margin-top:40px">
                                <div style="padding:30px; background:#fff; border-radius:8px; box-shadow:0 4px 20px rgba(0,0,0,0.05); border-top: 4px solid #666;">
                                    <div class="t-md c-muted" style="margin-bottom: 15px;">1. OEM</div>
                                    <div class="tag" style="background:#f0f0f0; color:#666; border:none; margin-bottom:20px;">被動配合</div>
                                    <ul style="font-size:16px; color:#3D4A5C; line-height:1.8; padding-left:20px;">
                                        <li>由<b>客戶會議</b>訂出規格與需求</li>
                                        <li>行銷部統籌資料後編輯企劃案</li>
                                        <li>搭配銷售<b>被動完成</b></li>
                                    </ul>
                                </div>
                                <div style="padding:30px; background:#fff; border-radius:8px; box-shadow:0 10px 30px rgba(0,163,224,0.1); border-top: 4px solid #00A3E0; transform: scale(1.02);">
                                    <div class="t-md c-blue" style="margin-bottom: 15px;">2. ODM</div>
                                    <div class="tag" style="background:#00A3E0; color:#fff; border:none; margin-bottom:20px;">主কত動提案</div>
                                    <ul style="font-size:16px; color:#3D4A5C; line-height:1.8; padding-left:20px;">
                                        <li>針對客戶進行<b>產品規格研究</b></li>
                                        <li>提出 <b>Sales Kit</b> 主動提案</li>
                                        <li>由行銷部統籌規劃後撰寫企劃案</li>
                                    </ul>
                                </div>
                                <div style="padding:30px; background:#fff; border-radius:8px; box-shadow:0 4px 20px rgba(0,0,0,0.05); border-top: 4px solid #FF6B35;">
                                    <div class="t-md c-orange" style="margin-bottom: 15px;">3. OBM</div>
                                    <div class="tag" style="background:#FF6B35; color:#fff; border:none; margin-bottom:20px;">引領市場</div>
                                    <ul style="font-size:16px; color:#3D4A5C; line-height:1.8; padding-left:20px;">
                                        <li>進行<b>市場缺口、趨勢研究</b></li>
                                        <li>行銷部統籌規劃後撰寫企劃案</li>
                                        <li>創造 <b>Sales Kit</b> 主動顛覆市場</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Slide 04: OEM 流程分析 -->
                    <div class="slide" data-name="OEM 流程">
                        <div class="slide-badge">#04 OEM 流程分析</div>
                        <div class="p" style="height:100%; display:flex; flex-direction:column;">
                            <div>
                                <div class="line"></div>
                                <h1 class="t-md c-dark" style="margin-top:10px">二、針對 OEM 的流程分析</h1>
                                <div style="display:flex; justify-content:space-between; align-items:center; background:#1A2332; padding:15px 30px; border-radius:8px; margin-top:20px; color:#fff; font-weight:600;">
                                    <span>開案客需表</span><span style="color:#00A3E0"></span>
                                    <span>企劃案背景</span><span style="color:#00A3E0"></span>
                                    <span>市場競品比較</span><span style="color:#00A3E0"></span>
                                    <span>成本評估</span><span style="color:#00A3E0"></span>
                                    <span>效益分析</span><span style="color:#00A3E0"></span>
                                    <span>風險評估</span>
                                </div>
                            </div>
                            
                            <div class="grid2" style="margin-top:30px; flex:1; align-items:start;">
                                <!-- 1 & 2 & 3 -->
                                <div style="display:flex; flex-direction:column; gap:20px;">
                                    <div class="card" style="border-left:4px solid #00A3E0; background:rgba(0,163,224,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">1. 開案客需表</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">從客戶mail與會議紀錄，整理規格、價格、數量</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;"> AI：</span>自動摘要文字，精煉核心規格<br/>
                                            <span style="color:#00A3E0; font-weight:bold;"> 程式：</span>自動對位寫入資料呈現表格
                                        </div>
                                    </div>
                                    <div class="card" style="border-left:4px solid #00A3E0; background:rgba(0,163,224,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">2. 企劃案背景</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">論述市場、客戶背景及營收影響</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;"> AI：</span>搜尋情報結合策略，撰寫背景草案<br/>
                                            <span style="color:#00A3E0; font-weight:bold;"> 程式：</span>排版並產生資料呈現表格
                                        </div>
                                    </div>
                                    <div class="card" style="border-left:4px solid #00A3E0; background:rgba(0,163,224,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">3. 市場競品比較</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">研究市場相對規格差異</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;"> AI：</span>深度比對產品參數，提取差異化優勢<br/>
                                            <span style="color:#00A3E0; font-weight:bold;"> 程式：</span>產出標準競品規格陣列比較表
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- 4, 5 & 6 -->
                                <div style="display:flex; flex-direction:column; gap:20px;">
                                    <div class="card" style="border-left:4px solid #FF6B35; background:rgba(255,107,53,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">4. 成本評估</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">生管資材依圖檔評估成本與設備投資</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;"> AI：</span>依據歷史手法指南訓練模型，提供估算輔助<br/>
                                            <span style="color:#00A3E0; font-weight:bold;"> 程式：</span>串接導入表單庫(如TIPTOP)
                                        </div>
                                    </div>
                                    <div class="card" style="border-left:4px solid #FF6B35; background:rgba(255,107,53,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">5. 效益分析</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">由圖估成本核算買價利潤</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#00A3E0; font-weight:bold;"> 程式：</span>接收成本數據後，自動寫入呈現效益表格
                                        </div>
                                    </div>
                                    <div class="card" style="border-left:4px solid #D4AF37; background:rgba(212,175,55,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">6. 風險評估</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">評估效益、市場衝擊之總表</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;"> AI：</span>統整數據，草擬風險指標與策略<br/>
                                            <span style="color:#00A3E0; font-weight:bold;"> 程式：</span>產出綜合風險專案儀表板
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Slide 05: ODM 前期研究 -->
                    <div class="slide" data-name="ODM 前期">
                        <div class="slide-badge">#05 ODM 流程分析</div>
                        <div class="full" style="align-items:center">
                            <div class="flex-40 center col p-sm" style="background:#1A2332; height:100%">
                                <div class="circle" style="width:120px;height:120px;background:#00A3E0;display:flex;align-items:center;justify-content:center;font-size:48px;color:#fff; margin-bottom:30px;"></div>
                                <h1 class="t-md" style="color:white; text-align:center;">三、ODM 流程分析<br/><span style="color:#00A3E0; font-size: 28px;">【前期研究階段】</span></h1>
                                <div class="line" style="margin:20px auto 30px auto; background:linear-gradient(90deg, #00A3E0, transparent)"></div>
                                <p style="color:rgba(255,255,255,0.7); text-align:center; padding: 0 40px; font-size:18px; line-height:1.6;">
                                    不再被動等待客戶規格，而是主動運用 AI 與爬蟲技術，發掘市場破口與設計痛點，以數據驅動提案。
                                </p>
                            </div>
                            <div class="flex-60 p" style="padding-right: 40px;">
                                <div style="display:flex;flex-direction:column;gap:30px;">
                                    <div class="card" style="border-left:4px solid #00A3E0; padding:25px; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#fff;">
                                        <div class="t-sm c-dark" style="font-size: 24px; margin-bottom: 10px;">1. 產品地圖分析</div>
                                        <p class="t-sm2 c-muted" style="margin-bottom: 15px;">分析客戶品牌產品缺口</p>
                                        <ul style="font-size: 16px; line-height:1.8; margin-left: 20px;">
                                            <li><span style="color:#00A3E0; font-weight:bold;"> 程式幫助：</span>爬蟲蒐集各大平台銷售資料</li>
                                            <li><span style="color:#FF6B35; font-weight:bold;"> AI 協助：</span>交叉分析數據圖表，精準得出潛在空窗結論</li>
                                        </ul>
                                    </div>
                                    
                                    <div class="card" style="border-left:4px solid #FF6B35; padding:25px; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#fff;">
                                        <div class="t-sm c-dark" style="font-size: 24px; margin-bottom: 10px;">2. 產品設計分析</div>
                                        <p class="t-sm2 c-muted" style="margin-bottom: 15px;">分析競品或客戶現有產品設計</p>
                                        <ul style="font-size: 16px; line-height:1.8; margin-left: 20px;">
                                            <li><span style="color:#00A3E0; font-weight:bold;"> 程式幫助：</span>爬蟲海量蒐集各大電商與論壇的「真實評論資料」</li>
                                            <li><span style="color:#FF6B35; font-weight:bold;"> AI 協助：</span>語意分析抽絲剝繭，找出「痛點分類」與「改善標的」</li>
                                        </ul>
                                    </div>
                                    
                                    <div class="card" style="border-left:4px solid #D4AF37; padding:25px; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#fff;">
                                        <div class="t-sm c-dark" style="font-size: 24px; margin-bottom: 10px;">3. 市場趨勢分析</div>
                                        <p class="t-sm2 c-muted" style="margin-bottom: 15px;">掌握產業脈動</p>
                                        <ul style="font-size: 16px; line-height:1.8; margin-left: 20px;">
                                            <li><span style="color:#FF6B35; font-weight:bold;"> AI 協助：</span>自動巡檢並蒐集各大專業論壇、KOL 發言，摘要出引領未來的技術發展流派</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Slide 06: ODM 推銷與企劃階段 -->
                    <div class="slide" data-name="ODM 企劃">
                        <div class="slide-badge">#06 ODM 流程分析</div>
                        <div class="p bg-grid" style="height:100%">
                            <div class="line"></div>
                            <h1 class="t-lg c-dark" style="margin-top:15px">三、ODM 推銷與企劃階段</h1>
                            <p class="t-sm2 c-blue" style="margin-top:10px; font-size:16px;">從洞察轉化為具體方案，銜接標準化流程</p>
                            
                            <div class="insight" style="margin-top:30px; background:#1A2332; border-left:none; border-top:4px solid #FF6B35; padding: 25px 35px;">
                                <h3 style="color:#fff; font-size: 24px; margin-bottom: 10px;"> 推銷階段 (Pitching)</h3>
                                <p style="color:rgba(255,255,255,0.8); font-size: 18px; line-height: 1.6;">整合前期 <strong>產品地圖、設計痛點、市場趨勢</strong> 洞察，主動向目標客戶提出先期 <strong>Sales Kit</strong> 與顛覆性概念提案，取得開發共識。</p>
                            </div>
                            
                            <div style="margin-top: 40px;">
                                <h3 class="t-sm c-dark" style="margin-bottom: 20px;"> 企劃案階段 (承襲 AI＋系統 雙引擎架構)</h3>
                                <div class="grid3" style="gap:15px;">
                                    <div class="box" style="border-left: 4px solid #00A3E0; background:#fff; box-shadow:0 2px 10px rgba(0,0,0,0.05); padding:20px;">
                                        <div style="font-size: 18px; margin-bottom: 5px;"><strong>1. 開案客需表</strong></div>
                                        <span style="font-size:14px; color:#666;">AI 彙整前沿需求 / 程式格式化</span>
                                    </div>
                                    <div class="box" style="border-left: 4px solid #00A3E0; background:#fff; box-shadow:0 2px 10px rgba(0,0,0,0.05); padding:20px;">
                                        <div style="font-size: 18px; margin-bottom: 5px;"><strong>2. 企劃案背景</strong></div>
                                        <span style="font-size:14px; color:#666;">AI 結合策略撰寫 / 程式圖表化</span>
                                    </div>
                                    <div class="box" style="border-left: 4px solid #00A3E0; background:#fff; box-shadow:0 2px 10px rgba(0,0,0,0.05); padding:20px;">
                                        <div style="font-size: 18px; margin-bottom: 5px;"><strong>3. 市場競品比較</strong></div>
                                        <span style="font-size:14px; color:#666;">AI 提取優勢 / 程式產陣列表</span>
                                    </div>
                                    <div class="box" style="border-left: 4px solid #FF6B35; background:#fff; box-shadow:0 2px 10px rgba(0,0,0,0.05); padding:20px;">
                                        <div style="font-size: 18px; margin-bottom: 5px;"><strong>4. 成本評估</strong></div>
                                        <span style="font-size:14px; color:#666;">AI 模型估算 / 程式 ERP 接接</span>
                                    </div>
                                    <div class="box" style="border-left: 4px solid #FF6B35; background:#fff; box-shadow:0 2px 10px rgba(0,0,0,0.05); padding:20px;">
                                        <div style="font-size: 18px; margin-bottom: 5px;"><strong>5. 效益分析</strong></div>
                                        <span style="font-size:14px; color:#666;">程式自動核算利潤與毛利呈現</span>
                                    </div>
                                    <div class="box" style="border-left: 4px solid #D4AF37; background:#fff; box-shadow:0 2px 10px rgba(0,0,0,0.05); padding:20px;">
                                        <div style="font-size: 18px; margin-bottom: 5px;"><strong>6. 風險評估</strong></div>
                                        <span style="font-size:14px; color:#666;">AI 草擬風險策略 / 程式建儀表板</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
</div>
            </div>

            <!-- Sidebar thumbnails -->
            <div class="thumbnail-nav" id="sidebar"></div>
        </div>
    </div>

    <script>
        const slides = document.querySelectorAll('.slide');
        const sidebar = document.getElementById('sidebar');
        let current = 0;
        const total = slides.length;

        // Build sidebar thumbnails via HTML cloning and CSS scale (instant)
        slides.forEach((s, i) => {
            const name = s.dataset.name || '';
            const div = document.createElement('div');
            div.className = 'thumb' + (i === 0 ? ' active' : '');

            const clone = s.cloneNode(true);
            clone.classList.remove('slide');
            clone.style.display = 'block';

            const wrapper = document.createElement('div');
            wrapper.className = 'thumb-slide-wrapper';
            wrapper.appendChild(clone);
            div.appendChild(wrapper);

            const overlay = document.createElement('div');
            overlay.className = 'thumb-overlay';
            overlay.innerHTML = '<span class="thumb-num">' + (i < 9 ? '0' : '') + (1 + i) + '</span><span class="thumb-label">' + name + '</span>';
            div.appendChild(overlay);

            div.onclick = () => go(i);
            sidebar.appendChild(div);
        });

        function go(n) {
            if (n < 0 || n >= total) return;
            slides[current].classList.remove('active');
            document.querySelectorAll('.thumb')[current].classList.remove('active');
            current = n;
            slides[current].classList.add('active');
            const thumbs = document.querySelectorAll('.thumb');
            thumbs[current].classList.add('active');
            thumbs[current].scrollIntoView({ block: 'nearest', behavior: 'smooth' });
            document.getElementById('counter').textContent = (current + 1) + ' / ' + total;
            fitSlide();
        }

        function fitSlide() {
            const view = document.querySelector('.slide-view');
            if(!view) return;
            const vw = view.clientWidth, vh = view.clientHeight;
            const scale = Math.min(vw / 1280, vh / 720) * 0.92;
            document.getElementById('slideContainer').style.transform = 'scale(' + scale + ')';
        }

        function toggleFullscreen() {
            if (!document.fullscreenElement) document.documentElement.requestFullscreen();
            else document.exitFullscreen();
        }

        async function exportPDF() {
            const btn = document.getElementById('pdfBtn');
            btn.textContent = '⏳ 匯出中...';
            btn.disabled = true;
            const { jsPDF } = window.jspdf;
            const pdf = new jsPDF({ orientation: 'landscape', unit: 'px', format: [1280, 720] });
            const container = document.getElementById('slideContainer');
            const savedScale = container.style.transform;
            container.style.transform = 'scale(1)';

            for (let i = 0; i < total; i++) {
                slides.forEach(s => s.classList.remove('active'));
                slides[i].classList.add('active');
                await new Promise(r => setTimeout(r, 150));
                const canvas = await html2canvas(slides[i], { scale: 2, width: 1280, height: 720, useCORS: true });
                const img = canvas.toDataURL('image/jpeg', 0.92);
                if (i > 0) pdf.addPage([1280, 720], 'landscape');
                pdf.addImage(img, 'JPEG', 0, 0, 1280, 720);
            }

            container.style.transform = savedScale;
            go(current);
            pdf.save('ISO_AI_Strategy_Presentation.pdf');
            btn.textContent = '📥 下載 PDF';
            btn.disabled = false;
        }

        document.addEventListener('keydown', e => {
            if (e.key === 'ArrowRight' || e.key === 'ArrowDown') go(current + 1);
            else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') go(current - 1);
            else if (e.key === 'f' || e.key === 'F') toggleFullscreen();
        });

        window.addEventListener('resize', fitSlide);
        fitSlide();
    </script>
</body>
</html>
