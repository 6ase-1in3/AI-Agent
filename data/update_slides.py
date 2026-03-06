import re

html_file = r"d:\OneDrive\Python_File\報告_AI導入\ISO_AI_Strategy_Presentation.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

new_slides = """
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
                                <span>● AI STRATEGY</span><span>● PROCESS INTEGRATION</span>
                            </div>
                        </div>
                    </div>

                    <!-- Slide 02: 簡介 (AI 與程式系統 定義) -->
                    <div class="slide" data-name="簡介">
                        <div class="slide-badge">#02 簡介</div>
                        <div class="full" style="align-items:center">
                            <div class="flex-50 p" style="display:flex;flex-direction:column;justify-content:center; padding-right:80px; width: 50%;">
                                <div class="line"></div>
                                <h1 class="t-xl c-dark" style="margin-top:20px; font-size:48px;">AI大腦 ╳ 系統手腳</h1>
                                <p class="t-md c-muted" style="margin-top:15px; font-weight:500; font-size: 24px;">雙引擎協同作戰定義</p>
                                
                                <div class="box" style="margin-top:35px; border-left:4px solid #00A3E0; background:rgba(0,163,224,0.05); padding: 25px;">
                                    <div style="font-size: 40px; margin-bottom: 10px;">🧠</div>
                                    <h3 class="c-blue t-sm" style="margin-bottom: 5px;">AI 人工智慧 (大腦)</h3>
                                    <p class="t-body c-dark" style="font-size: 18px; line-height: 1.6;">專注於高價值的運算，將大數據進行<strong>分析、預測、決策</strong>的智慧系統。</p>
                                </div>
                            </div>
                            <div class="flex-50 p" style="display:flex;flex-direction:column;justify-content:center; padding: 0 60px; background:#F8FAFC; height:100%; width: 50%;">
                                <div class="box" style="margin-top:0px; border-left:4px solid #FF6B35; background:rgba(255,107,53,0.05); padding: 25px;">
                                    <div style="font-size: 40px; margin-bottom: 10px;">⚙️</div>
                                    <h3 class="c-orange t-sm" style="margin-bottom: 5px;">程式系統 (手腳)</h3>
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
                                    <ul style="font-size:16px; color:#3D4A5C; line-height:1.8; padding-left:20px; list-style-type: disc;">
                                        <li>由<b>客戶會議</b>訂出規格與需求</li>
                                        <li>行銷部統籌資料後編輯企劃案</li>
                                        <li>搭配銷售<b>被動完成</b></li>
                                    </ul>
                                </div>
                                <div style="padding:30px; background:#fff; border-radius:8px; box-shadow:0 10px 30px rgba(0,163,224,0.1); border-top: 4px solid #00A3E0; transform: scale(1.02);">
                                    <div class="t-md c-blue" style="margin-bottom: 15px;">2. ODM</div>
                                    <div class="tag" style="background:#00A3E0; color:#fff; border:none; margin-bottom:20px;">主動提案</div>
                                    <ul style="font-size:16px; color:#3D4A5C; line-height:1.8; padding-left:20px; list-style-type: disc;">
                                        <li>針對客戶進行<b>產品規格研究</b></li>
                                        <li>提出 <b>Sales Kit</b> 主動提案</li>
                                        <li>由行銷部統籌規劃後撰寫企劃案</li>
                                    </ul>
                                </div>
                                <div style="padding:30px; background:#fff; border-radius:8px; box-shadow:0 4px 20px rgba(0,0,0,0.05); border-top: 4px solid #FF6B35;">
                                    <div class="t-md c-orange" style="margin-bottom: 15px;">3. OBM</div>
                                    <div class="tag" style="background:#FF6B35; color:#fff; border:none; margin-bottom:20px;">引領市場</div>
                                    <ul style="font-size:16px; color:#3D4A5C; line-height:1.8; padding-left:20px; list-style-type: disc;">
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
                                <h1 class="t-md c-dark" style="margin-top:10px; font-size: 36px;">二、針對 OEM 的流程分析</h1>
                                <div style="display:flex; justify-content:space-between; align-items:center; background:#1A2332; padding:15px 30px; border-radius:8px; margin-top:20px; color:#fff; font-weight:600; font-size: 14px;">
                                    <span>開案客需表</span><span style="color:#00A3E0">➔</span>
                                    <span>企劃案背景</span><span style="color:#00A3E0">➔</span>
                                    <span>市場競品比較</span><span style="color:#00A3E0">➔</span>
                                    <span>成本評估</span><span style="color:#00A3E0">➔</span>
                                    <span>效益分析</span><span style="color:#00A3E0">➔</span>
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
                                            <span style="color:#FF6B35; font-weight:bold;">🤖 AI：</span>自動摘要文字，精煉核心規格<br/>
                                            <span style="color:#00A3E0; font-weight:bold;">💻 程式：</span>自動對位寫入資料呈現表格
                                        </div>
                                    </div>
                                    <div class="card" style="border-left:4px solid #00A3E0; background:rgba(0,163,224,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">2. 企劃案背景</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">論述市場、客戶背景及營收影響</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;">🤖 AI：</span>搜尋情報結合策略，撰寫背景草案<br/>
                                            <span style="color:#00A3E0; font-weight:bold;">💻 程式：</span>排版並產生資料呈現表格
                                        </div>
                                    </div>
                                    <div class="card" style="border-left:4px solid #00A3E0; background:rgba(0,163,224,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">3. 市場競品比較</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">研究市場相對規格差異</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;">🤖 AI：</span>深度比對產品參數，提取差異化優勢<br/>
                                            <span style="color:#00A3E0; font-weight:bold;">💻 程式：</span>產出標準競品規格陣列比較表
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- 4, 5 & 6 -->
                                <div style="display:flex; flex-direction:column; gap:20px;">
                                    <div class="card" style="border-left:4px solid #FF6B35; background:rgba(255,107,53,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">4. 成本評估</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">生管資材依圖檔評估成本與設備投資</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;">🤖 AI：</span>依據歷史手法指南訓練模型，提供估算輔助<br/>
                                            <span style="color:#00A3E0; font-weight:bold;">💻 程式：</span>串接導入表單庫(如TIPTOP)
                                        </div>
                                    </div>
                                    <div class="card" style="border-left:4px solid #FF6B35; background:rgba(255,107,53,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">5. 效益分析</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">由圖估成本核算買價利潤</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#00A3E0; font-weight:bold;">💻 程式：</span>接收成本數據後，自動寫入呈現效益表格
                                        </div>
                                    </div>
                                    <div class="card" style="border-left:4px solid #D4AF37; background:rgba(212,175,55,0.02); padding: 15px;">
                                        <div class="t-sm c-dark">6. 風險評估</div>
                                        <p class="t-sm2 c-muted" style="margin:4px 0 10px 0;">評估效益、市場衝擊之總表</p>
                                        <div style="font-size:14px; background:#fff; padding:10px; border-radius:4px; border:1px solid #eee; line-height: 1.6;">
                                            <span style="color:#FF6B35; font-weight:bold;">🤖 AI：</span>統整數據，草擬風險指標與策略<br/>
                                            <span style="color:#00A3E0; font-weight:bold;">💻 程式：</span>產出綜合風險專案儀表板
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
                                <div class="circle" style="width:120px;height:120px;background:#00A3E0;display:flex;align-items:center;justify-content:center;font-size:48px;color:#fff; margin-bottom:30px;">🔍</div>
                                <h1 class="t-md" style="color:white; text-align:center;">三、針對現階段<br/>ODM 流程分析<br/><span style="color:#00A3E0; font-size: 28px;">【前期研究階段】</span></h1>
                                <div class="line" style="margin:20px auto 30px auto; background:linear-gradient(90deg, #00A3E0, transparent)"></div>
                                <p style="color:rgba(255,255,255,0.7); text-align:center; padding: 0 40px; font-size:18px; line-height:1.6;">
                                    不再被動等待客戶規格，而是主動運用 AI 與爬蟲技術，發掘市場破口與設計痛點，以數據驅動提案。
                                </p>
                            </div>
                            <div class="flex-60 p" style="padding-left: 60px; padding-right: 40px;">
                                <div style="display:flex;flex-direction:column;gap:30px;">
                                    <div class="card" style="border-left:4px solid #00A3E0; padding:25px; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#fff;">
                                        <div class="t-sm c-dark" style="font-size: 24px; margin-bottom: 10px;">1. 產品地圖分析</div>
                                        <p class="t-sm2 c-muted" style="margin-bottom: 15px;">分析客戶品牌產品缺口</p>
                                        <ul style="font-size: 16px; line-height:1.8; margin-left: 20px; list-style-type: none;">
                                            <li><span style="color:#00A3E0; font-weight:bold;">💻 程式幫助：</span>爬蟲蒐集各大平台銷售資料</li>
                                            <li><span style="color:#FF6B35; font-weight:bold;">🤖 AI 協助：</span>交叉分析數據圖表，精準得出結論</li>
                                        </ul>
                                    </div>
                                    
                                    <div class="card" style="border-left:4px solid #FF6B35; padding:25px; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#fff;">
                                        <div class="t-sm c-dark" style="font-size: 24px; margin-bottom: 10px;">2. 產品設計分析</div>
                                        <p class="t-sm2 c-muted" style="margin-bottom: 15px;">分析競品或客戶現有產品設計</p>
                                        <ul style="font-size: 16px; line-height:1.8; margin-left: 20px; list-style-type: none;">
                                            <li><span style="color:#00A3E0; font-weight:bold;">💻 程式幫助：</span>爬蟲海量蒐集各大電商與論壇的評論資料</li>
                                            <li><span style="color:#FF6B35; font-weight:bold;">🤖 AI 協助：</span>語意分析客戶痛點與對接比較</li>
                                        </ul>
                                    </div>
                                    
                                    <div class="card" style="border-left:4px solid #D4AF37; padding:25px; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#fff;">
                                        <div class="t-sm c-dark" style="font-size: 24px; margin-bottom: 10px;">3. 市場趨勢分析</div>
                                        <p class="t-sm2 c-muted" style="margin-bottom: 15px;">掌握產業脈動與趨勢</p>
                                        <ul style="font-size: 16px; line-height:1.8; margin-left: 20px; list-style-type: none;">
                                            <li><span style="color:#FF6B35; font-weight:bold;">🤖 AI 協助：</span>自動分析並蒐集各大專業論壇、KOL 在專業領域的引導趨勢發展</li>
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
                                <h3 style="color:#fff; font-size: 24px; margin-bottom: 10px;">🤝 推銷階段 (Pitching)</h3>
                                <p style="color:rgba(255,255,255,0.8); font-size: 18px; line-height: 1.6;">整合前期 <strong>產品地圖、設計分析、趨勢研究</strong> 洞察，主動向目標客戶提出概念提案，取得開發共識。</p>
                            </div>
                            
                            <div style="margin-top: 40px;">
                                <h3 class="t-sm c-dark" style="margin-bottom: 20px;">📋 企劃案階段</h3>
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
"""

new_content = re.sub(
    r'<div id="slideContainer">.*?(?=</div>\s*</div>\s*<!-- Sidebar thumbnails -->)', 
    f'<div id="slideContainer">\n{new_slides}', 
    content, 
    flags=re.DOTALL
)

with open(r"d:\OneDrive\Python_File\報告_AI導入\ISO_AI_Strategy_Presentation.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done")
