# ★このサービスの独自コンテキスト（品質向上のため必ず参照）:
# 解決する問題: 用途（通勤・サイクリング・買い物）・予算・走行距離から最適な電動自転車タイプを診
# 対象ユーザー: 効率化・最適化を求める日本のユーザー
# キーワード: 電動自転車
TITLE = '電動自転車選び診断【無料】無料診断・アドバイス'
DESCRIPTION = '用途（通勤・サイクリング・買い物）・予算・走行距離から最適な電動自転車タイプを診断。登録不要・完全無料でご利用いただけます。'
DESCRIPTION_SHORT = '用途（通勤・サイクリング・買い物）・予算・走行距離から最適な電動自転車タイプ...'
COLOR1 = '#E0E7FF'
COLOR2 = '#F0F4FF'
COLOR_BTN = '#6366F1'
FOOTER_LINKS = [('https://appadaycreator.com/cycling-cost-calculator/', '自転車通勤コスト計算ツール'), ('https://appadaycreator.com/commute-cost-optimizer/', '通勤コスト最適化診断'), ('https://appadaycreator.com/bike-cost-advisor/', 'バイク・原付購入維持費診断')]

CUSTOM_CSS = """"""

# MAIN_HTML≤100行 / 色=#6366F1 / class="card"でUI / id="result"で結果隠し
MAIN_HTML = """<div class="card" id="quiz-start">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:12px;">🚲 電動自転車診断</h2>
  <p style="color:#666;font-size:14px;margin-bottom:8px;">用途・予算・環境から最適な電動アシスト自転車タイプを診断</p>
  <ul style="font-size:13px;color:#94a3b8;margin:0 0 16px 16px;"><li>質問数：5問</li><li>所要時間：約1分</li></ul>
  <button class="btn" onclick="startQuiz()">診断スタート →</button>
</div>
<div id="quiz-area" style="display:none;">
  <div style="font-size:12px;color:#999;margin-bottom:8px;">質問 <span id="q-num">1</span> / <span id="q-total">5</span></div>
  <div id="q-progress" style="height:4px;background:#e5e7eb;border-radius:2px;margin-bottom:16px;">
    <div id="q-bar" style="height:100%;background:#6366F1;border-radius:2px;transition:width .3s;width:20%;"></div>
  </div>
  <p id="q-text" style="font-size:16px;font-weight:600;margin-bottom:16px;"></p>
  <div id="q-options"></div>
</div>
<div class="result" id="result">
  <div class="card">
    <h3 id="r-title" style="font-size:18px;font-weight:700;margin-bottom:8px;color:#6366F1;"></h3>
    <p id="r-desc" style="color:#444;font-size:14px;line-height:1.7;"></p>
    <button class="btn" style="margin-top:16px;" onclick="location.reload()">もう一度診断</button>
  </div>
</div>"""

# JS: スタブの TODO コメント箇所を実装してください（骨格は変えないこと）
JS_CODE = """const QUESTIONS = [
  { text:'Q1. 主な用途は？', opts:['通勤・通学（毎日使用）','子供の送迎（チャイルドシート）','買い物・近所の移動','サイクリング・レクリエーション'] },
  { text:'Q2. 1日の走行距離の目安は？', opts:['5km未満（駅や近所だけ）','5〜15km（片道10km以内）','15〜30km（中距離）','30km以上（ロングライド）'] },
  { text:'Q3. 坂道・勾配の状況は？', opts:['ほぼ平坦（坂がほとんどない）','少し起伏がある','かなり坂が多い','急坂・山道あり'] },
  { text:'Q4. 予算の目安は？', opts:['10万円未満','10〜20万円','20〜35万円','35万円以上'] },
  { text:'Q5. 主な保管場所は？', opts:['屋内（室内・ガレージ）','屋外・屋根あり（駐輪場）','屋外・雨ざらし','共用駐輪場（盗難対策優先）'] },
];
const RESULTS = [
  { title:'🏃 シティコミュータータイプ — ブリヂストン・パナソニックの定番', desc:'毎日の通勤・通学に最適な電動アシスト自転車です。ブリヂストン「TB1e」（13万円〜）・パナソニック「ビビDX」（11万円〜）が定番。バッテリー持続距離60〜100km、内装変速機で駐輪場での取り回しも楽。防錠機能・ライト・泥除けが標準装備でコスパ最高。通勤距離10km未満なら十分すぎる性能です。' },
  { title:'👶 ファミリーモデル — ヤマハ・パナソニックの電動アシスト', desc:'チャイルドシートに対応した電動アシスト自転車です。ヤマハ「PAS babby un SP」（16万円〜）・ブリヂストン「ビッケモブdd」（19万円〜）が人気。低床フレームで子供の乗せ降ろしが楽、強力アシストで坂道もスイスイ。前後チャイルドシート対応・駐輪スタンドの安定性も重要なチェックポイントです。' },
  { title:'🏔️ スポーツE-Bike — ヤマハCROSS CORE・メリダ', desc:'走行性能と長距離対応を両立したスポーツ系E-Bikeです。ヤマハ「WABASH RT」・メリダ「eBIG.SEVEN」・BESV「PSA1」などが選択肢。油圧ディスクブレーキ・太めのタイヤで悪路も対応、バッテリー航続距離100km以上の機種も。速度制限（24km/h）が日本の法律ですが、ペダリングのサポートで長距離が快適になります。' },
  { title:'⚡ ハイパフォーマンスE-Bike — Specialized・Trekなど', desc:'本格的なサイクリングを楽しむためのハイエンドE-Bikeです。Specialized「Turbo Vado」・Trek「Verve+」などが代表格（25〜50万円）。Bosch・Shimano STEPS搭載の高性能モーターで坂道も楽々、スマートフォン連携でナビ・ケイデンス管理も。防水性能・高耐久パーツで屋外保管にも対応できる機種が多いです。' },
];
function getResult(answers) {
  const total = answers.reduce((s,a) => s+a.idx, 0);
  const max = (QUESTIONS.length * 3);
  const idx = Math.min(Math.floor(total / max * RESULTS.length), RESULTS.length-1);
  return RESULTS[idx];
}
const BTN='#6366F1'; let cur=0; const ans=[];
document.addEventListener('DOMContentLoaded',()=>{ document.getElementById('q-total').textContent=QUESTIONS.length; });
function startQuiz(){ cur=0;ans.length=0; document.getElementById('quiz-start').style.display='none'; document.getElementById('quiz-area').style.display='block'; document.getElementById('result').classList.remove('show'); renderQ(); }
function renderQ(){
  const q=QUESTIONS[cur];
  document.getElementById('q-num').textContent=cur+1;
  document.getElementById('q-bar').style.width=((cur+1)/QUESTIONS.length*100)+'%';
  document.getElementById('q-text').textContent=q.text;
  document.getElementById('q-options').innerHTML=q.opts.map((o,i)=>`<button onclick="answer(${i})" style="width:100%;padding:12px;margin-bottom:8px;border:2px solid #e5e7eb;border-radius:10px;font-size:14px;cursor:pointer;background:#fff;text-align:left;">${o}</button>`).join('');
}
function answer(idx){ ans.push({idx}); cur++; if(cur>=QUESTIONS.length) showResult(); else renderQ(); }
function showResult(){
  document.getElementById('quiz-area').style.display='none';
  const r=getResult(ans);
  document.getElementById('r-title').textContent=r.title;
  document.getElementById('r-desc').textContent=r.desc;
  document.getElementById('result').classList.add('show');
}"""

FAQ = [
    ("電動自転車選び診断は無料で使えますか？", "はい、完全無料でご利用いただけます。登録・ログイン・アプリのインストールも不要です。"),
    ("何回でも診断できますか？", "はい、何度でもご利用いただけます。条件を変えて繰り返し診断してみてください。"),
    ("スマートフォンでも使えますか？", "はい、スマートフォン・タブレット・PCすべてのデバイスに対応しています。"),
    ("診断結果は保存されますか？", "結果はブラウザには保存されません。スクリーンショットやSNSシェアでご記録ください。"),
    ("入力したデータはサーバーに送信されますか？", "いいえ。すべての処理はブラウザ内で完結し、個人情報・入力データのサーバー送信は行いません。"),
]

HOW_TO = [
    "ページを開き、診断の説明を確認する",
    "スタートボタンをクリックして診断を開始する",
    "表示される質問に順番に回答する（約1〜2分）",
    "すべて回答すると診断結果が自動表示される",
    "結果のアドバイスを確認してSNSでシェアする",
]

