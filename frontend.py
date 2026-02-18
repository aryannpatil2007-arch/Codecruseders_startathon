<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Offroad Segmentation — Project Overview</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:        #0b0e12;
    --surface:   #111620;
    --card:      #161d2b;
    --border:    #1f2d45;
    --accent:    #3dffa2;
    --accent2:   #38b6ff;
    --accent3:   #ff6b35;
    --text:      #e2eaf5;
    --muted:     #7a8fa8;
    --tag-bg:    #0d2030;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* ── GRID NOISE BACKGROUND ── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(61,255,162,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(61,255,162,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  /* ── HERO ── */
  .hero {
    position: relative;
    padding: 80px 60px 60px;
    border-bottom: 1px solid var(--border);
    overflow: hidden;
    z-index: 1;
  }

  .hero-glow {
    position: absolute;
    top: -120px; left: -80px;
    width: 700px; height: 500px;
    background: radial-gradient(ellipse, rgba(61,255,162,0.08) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero-glow2 {
    position: absolute;
    bottom: -200px; right: -100px;
    width: 600px; height: 600px;
    background: radial-gradient(ellipse, rgba(56,182,255,0.06) 0%, transparent 70%);
    pointer-events: none;
  }

  .tag {
    display: inline-block;
    background: var(--tag-bg);
    color: var(--accent);
    border: 1px solid rgba(61,255,162,0.3);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 4px;
    margin-bottom: 24px;
  }

  .hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(36px, 5vw, 64px);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    max-width: 720px;
  }

  .hero h1 span { color: var(--accent); }

  .hero-sub {
    margin-top: 20px;
    color: var(--muted);
    font-size: 16px;
    max-width: 580px;
    font-weight: 300;
  }

  .hero-meta {
    display: flex;
    gap: 40px;
    margin-top: 40px;
    flex-wrap: wrap;
  }

  .meta-item { display: flex; flex-direction: column; gap: 4px; }
  .meta-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
  }
  .meta-value {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: var(--accent2);
  }

  /* ── LAYOUT ── */
  .container {
    max-width: 1300px;
    margin: 0 auto;
    padding: 0 60px;
    position: relative;
    z-index: 1;
  }

  .section {
    padding: 64px 0 20px;
    border-bottom: 1px solid var(--border);
  }

  .section:last-child { border-bottom: none; }

  .section-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 40px;
  }

  .section-num {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    opacity: 0.6;
    width: 28px;
    flex-shrink: 0;
  }

  .section-title {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.02em;
  }

  .section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, var(--border), transparent);
  }

  /* ── CARDS ── */
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
  .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }

  .card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 28px;
    transition: border-color 0.2s, transform 0.2s;
  }

  .card:hover {
    border-color: rgba(61,255,162,0.25);
    transform: translateY(-2px);
  }

  .card-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 12px;
  }

  .card-title {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
    color: var(--text);
  }

  .card-body {
    color: var(--muted);
    font-size: 13.5px;
    line-height: 1.65;
  }

  /* ── ARCHITECTURE DIAGRAM ── */
  .arch-flow {
    display: flex;
    align-items: center;
    gap: 0;
    overflow-x: auto;
    padding: 32px 0 16px;
    flex-wrap: nowrap;
  }

  .arch-node {
    flex-shrink: 0;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 24px;
    text-align: center;
    min-width: 150px;
    position: relative;
    transition: border-color 0.2s;
  }

  .arch-node:hover { border-color: var(--accent2); }

  .arch-node.highlight { border-color: rgba(61,255,162,0.5); background: rgba(61,255,162,0.04); }

  .arch-node-icon {
    font-size: 28px;
    margin-bottom: 8px;
    display: block;
  }

  .arch-node-title {
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 4px;
  }

  .arch-node-sub {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  .arch-arrow {
    flex-shrink: 0;
    width: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--muted);
    font-size: 20px;
    position: relative;
  }

  .arch-arrow::before {
    content: '';
    position: absolute;
    height: 1px;
    width: 100%;
    background: linear-gradient(to right, var(--border), var(--accent2), var(--border));
    opacity: 0.5;
  }

  .arch-arrow span { background: var(--bg); padding: 0 4px; z-index: 1; }

  /* ── CLASS TABLE ── */
  .class-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-bottom: 20px;
  }

  .class-chip {
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    border: 1px solid var(--border);
    transition: transform 0.2s;
  }

  .class-chip:hover { transform: scale(1.03); }

  .class-dot {
    width: 14px; height: 14px;
    border-radius: 3px;
    flex-shrink: 0;
  }

  .class-name {
    font-size: 12.5px;
    font-weight: 500;
    color: var(--text);
    line-height: 1.2;
  }

  .class-id {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--muted);
  }

  /* ── CODE BLOCK ── */
  .code-block {
    background: #0a0e16;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 20px;
    font-family: 'DM Mono', monospace;
  }

  .code-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 18px;
    background: #0f141e;
    border-bottom: 1px solid var(--border);
  }

  .code-dots { display: flex; gap: 6px; }
  .code-dot { width: 10px; height: 10px; border-radius: 50%; }
  .code-dot.r { background: #ff5f57; }
  .code-dot.y { background: #febc2e; }
  .code-dot.g { background: #28c840; }
  .code-filename { font-size: 11px; color: var(--muted); letter-spacing: 0.05em; }

  pre {
    padding: 20px 22px;
    overflow-x: auto;
    font-size: 12.5px;
    line-height: 1.75;
    color: #c8d6e8;
    white-space: pre;
  }

  .kw  { color: #7dd3fc; }
  .fn  { color: #86efac; }
  .str { color: #fcd34d; }
  .cm  { color: #4a5e74; font-style: italic; }
  .num { color: #fb923c; }
  .cls { color: #a78bfa; }

  /* ── METRIC CARDS ── */
  .metric-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    text-align: center;
  }

  .metric-name {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 12px;
  }

  .metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 36px;
    font-weight: 800;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 8px;
  }

  .metric-desc { color: var(--muted); font-size: 12px; }

  /* ── FILE TREE ── */
  .file-tree {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px 28px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  .tree-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 6px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    cursor: default;
    transition: color 0.15s;
  }

  .tree-item:last-child { border-bottom: none; }
  .tree-item:hover { color: var(--accent); }

  .tree-icon { font-size: 14px; flex-shrink: 0; width: 20px; text-align: center; }
  .tree-name { flex: 1; color: var(--text); }
  .tree-desc { color: var(--muted); font-size: 11px; }

  .tree-indent { padding-left: 24px; }

  /* ── STEP FLOW ── */
  .steps { display: flex; flex-direction: column; gap: 0; }

  .step {
    display: grid;
    grid-template-columns: 64px 1fr;
    gap: 20px;
    position: relative;
  }

  .step:not(:last-child) .step-line {
    position: absolute;
    left: 31px;
    top: 48px;
    bottom: 0;
    width: 2px;
    background: linear-gradient(to bottom, var(--accent2), transparent);
    opacity: 0.3;
  }

  .step-num {
    width: 40px; height: 40px;
    border-radius: 50%;
    background: var(--card);
    border: 2px solid var(--accent2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 14px;
    color: var(--accent2);
    flex-shrink: 0;
    margin-top: 4px;
  }

  .step-content { padding-bottom: 40px; }
  .step-title {
    font-family: 'Syne', sans-serif;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 8px;
  }

  .step-body { color: var(--muted); font-size: 13.5px; }

  /* ── PILLS ── */
  .pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }

  .pill {
    background: var(--tag-bg);
    border: 1px solid var(--border);
    color: var(--muted);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    padding: 4px 12px;
    border-radius: 20px;
    letter-spacing: 0.05em;
  }

  .pill.green { border-color: rgba(61,255,162,0.3); color: var(--accent); }
  .pill.blue  { border-color: rgba(56,182,255,0.3); color: var(--accent2); }
  .pill.orange{ border-color: rgba(255,107,53,0.3); color: var(--accent3); }

  /* ── IMPROVEMENTS TABLE ── */
  .improvement-item {
    display: grid;
    grid-template-columns: 28px 1fr auto;
    align-items: start;
    gap: 14px;
    padding: 20px 0;
    border-bottom: 1px solid var(--border);
  }

  .improvement-item:last-child { border-bottom: none; }

  .imp-icon { font-size: 18px; margin-top: 2px; }

  .imp-title {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 6px;
  }

  .imp-body { color: var(--muted); font-size: 13px; }

  .priority {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 3px 10px;
    border-radius: 4px;
    white-space: nowrap;
    margin-top: 2px;
  }

  .priority.high   { background: rgba(255,107,53,0.15); color: var(--accent3); border: 1px solid rgba(255,107,53,0.3); }
  .priority.medium { background: rgba(56,182,255,0.12); color: var(--accent2); border: 1px solid rgba(56,182,255,0.3); }
  .priority.low    { background: rgba(61,255,162,0.1);  color: var(--accent);  border: 1px solid rgba(61,255,162,0.3); }

  /* ── MINI BAR CHART ── */
  .bar-chart { display: flex; flex-direction: column; gap: 10px; margin-top: 8px; }
  .bar-row { display: flex; align-items: center; gap: 12px; }
  .bar-label { font-size: 12px; color: var(--muted); width: 110px; flex-shrink: 0; font-family: 'DM Mono', monospace; }
  .bar-track { flex: 1; height: 8px; background: rgba(255,255,255,0.05); border-radius: 4px; overflow: hidden; }
  .bar-fill  { height: 100%; border-radius: 4px; transition: width 1s ease; }
  .bar-val   { font-family: 'DM Mono', monospace; font-size: 11px; color: var(--text); width: 40px; text-align: right; }

  /* ── SCROLLBAR ── */
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

  /* ── ANIMATE IN ── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .hero h1, .hero .hero-sub, .hero .hero-meta {
    animation: fadeUp 0.7s ease both;
  }
  .hero .hero-sub  { animation-delay: 0.1s; }
  .hero .hero-meta { animation-delay: 0.2s; }

  @media (max-width: 900px) {
    .hero  { padding: 50px 24px 40px; }
    .container { padding: 0 24px; }
    .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
    .class-grid { grid-template-columns: repeat(2,1fr); }
    .arch-flow { flex-direction: column; align-items: flex-start; }
    .arch-arrow { transform: rotate(90deg); }
  }
</style>
</head>
<body>

<!-- ═══════════════════════════════════════════════════
     HERO
═══════════════════════════════════════════════════ -->
<div class="hero">
  <div class="hero-glow"></div>
  <div class="hero-glow2"></div>
  <div class="tag">ML Project Documentation</div>
  <h1>Offroad <span>Segmentation</span><br>System</h1>
  <p class="hero-sub">
    Semantic segmentation for off-road environments using a frozen DINOv2 ViT backbone
    with a lightweight ConvNeXt-style segmentation head — trained to classify 10 terrain classes.
  </p>
  <div class="hero-meta">
    <div class="meta-item">
      <span class="meta-label">Backbone</span>
      <span class="meta-value">DINOv2-S</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Architecture</span>
      <span class="meta-value">ViT-S/14</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Classes</span>
      <span class="meta-value">10</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Framework</span>
      <span class="meta-value">PyTorch</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Input Resolution</span>
      <span class="meta-value">462 × 476</span>
    </div>
  </div>
</div>

<div class="container">

<!-- ═══════════════════════════════════════════════════
     SECTION 1 — PROJECT STRUCTURE
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">01</span>
    <h2 class="section-title">Project Structure</h2>
    <div class="section-line"></div>
  </div>

  <div class="grid-2">
    <div class="file-tree">
      <div class="tree-item">
        <span class="tree-icon">📁</span>
        <span class="tree-name">Offroad_Segmentation_Scripts/</span>
        <span class="tree-desc">root</span>
      </div>
      <div class="tree-item tree-indent">
        <span class="tree-icon">🐍</span>
        <span class="tree-name">train_segmentation.py</span>
        <span class="tree-desc">main trainer</span>
      </div>
      <div class="tree-item tree-indent">
        <span class="tree-icon">🐍</span>
        <span class="tree-name">test_segmentation.py</span>
        <span class="tree-desc">inference + eval</span>
      </div>
      <div class="tree-item tree-indent">
        <span class="tree-icon">🐍</span>
        <span class="tree-name">visualize.py</span>
        <span class="tree-desc">mask colorizer</span>
      </div>
      <div class="tree-item tree-indent">
        <span class="tree-icon">📁</span>
        <span class="tree-name">ENV_SETUP/</span>
        <span class="tree-desc">conda scripts</span>
      </div>
      <div class="tree-item tree-indent" style="padding-left:48px">
        <span class="tree-icon">🦇</span>
        <span class="tree-name">create_env.bat</span>
        <span class="tree-desc">env creation</span>
      </div>
      <div class="tree-item tree-indent" style="padding-left:48px">
        <span class="tree-icon">🦇</span>
        <span class="tree-name">install_packages.bat</span>
        <span class="tree-desc">deps install</span>
      </div>
      <div class="tree-item tree-indent" style="padding-left:48px">
        <span class="tree-icon">🦇</span>
        <span class="tree-name">setup_env.bat</span>
        <span class="tree-desc">activation</span>
      </div>
    </div>

    <div class="file-tree">
      <div class="tree-item">
        <span class="tree-icon">📁</span>
        <span class="tree-name">Offroad_Segmentation_Training_Dataset/</span>
        <span class="tree-desc">expected sibling</span>
      </div>
      <div class="tree-item tree-indent">
        <span class="tree-icon">📁</span>
        <span class="tree-name">train/</span>
        <span class="tree-desc"></span>
      </div>
      <div class="tree-item tree-indent" style="padding-left:48px">
        <span class="tree-icon">🖼️</span>
        <span class="tree-name">Color_Images/</span>
        <span class="tree-desc">RGB .png</span>
      </div>
      <div class="tree-item tree-indent" style="padding-left:48px">
        <span class="tree-icon">🎭</span>
        <span class="tree-name">Segmentation/</span>
        <span class="tree-desc">grayscale masks</span>
      </div>
      <div class="tree-item tree-indent">
        <span class="tree-icon">📁</span>
        <span class="tree-name">val/</span>
        <span class="tree-desc">(same structure)</span>
      </div>
      <div class="tree-item">
        <span class="tree-icon">📁</span>
        <span class="tree-name">Offroad_Segmentation_testImages/</span>
        <span class="tree-desc">inference input</span>
      </div>
      <div class="tree-item">
        <span class="tree-icon">🏋️</span>
        <span class="tree-name">segmentation_head.pth</span>
        <span class="tree-desc">saved weights (output)</span>
      </div>
      <div class="tree-item">
        <span class="tree-icon">📊</span>
        <span class="tree-name">train_stats/</span>
        <span class="tree-desc">plots + metrics (output)</span>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 2 — MODEL ARCHITECTURE
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">02</span>
    <h2 class="section-title">Model Architecture</h2>
    <div class="section-line"></div>
  </div>

  <div class="arch-flow">
    <div class="arch-node">
      <span class="arch-node-icon">🖼️</span>
      <div class="arch-node-title">Input Image</div>
      <div class="arch-node-sub">462 × 476 × 3</div>
    </div>
    <div class="arch-arrow"><span>→</span></div>
    <div class="arch-node">
      <span class="arch-node-icon">🧊</span>
      <div class="arch-node-title">Normalize</div>
      <div class="arch-node-sub">ImageNet stats</div>
    </div>
    <div class="arch-arrow"><span>→</span></div>
    <div class="arch-node highlight">
      <span class="arch-node-icon">🦕</span>
      <div class="arch-node-title">DINOv2 ViT-S/14</div>
      <div class="arch-node-sub">frozen backbone</div>
    </div>
    <div class="arch-arrow"><span>→</span></div>
    <div class="arch-node">
      <span class="arch-node-icon">📦</span>
      <div class="arch-node-title">Patch Tokens</div>
      <div class="arch-node-sub">33×34 × 384</div>
    </div>
    <div class="arch-arrow"><span>→</span></div>
    <div class="arch-node highlight">
      <span class="arch-node-icon">🧩</span>
      <div class="arch-node-title">ConvNeXt Head</div>
      <div class="arch-node-sub">trainable</div>
    </div>
    <div class="arch-arrow"><span>→</span></div>
    <div class="arch-node">
      <span class="arch-node-icon">↕️</span>
      <div class="arch-node-title">Bilinear Upsample</div>
      <div class="arch-node-sub">to 462 × 476</div>
    </div>
    <div class="arch-arrow"><span>→</span></div>
    <div class="arch-node">
      <span class="arch-node-icon">🗺️</span>
      <div class="arch-node-title">Segmentation Map</div>
      <div class="arch-node-sub">10 classes</div>
    </div>
  </div>

  <div class="grid-2" style="margin-top:32px;">
    <div class="card">
      <div class="card-label">DINOv2 Backbone (Frozen)</div>
      <div class="card-title">dinov2_vits14</div>
      <div class="card-body">
        Pre-trained Vision Transformer (Small) with patch size 14. The backbone is loaded from
        <code style="color:var(--accent);font-family:'DM Mono',monospace">facebookresearch/dinov2</code> via
        <code style="color:var(--accent);font-family:'DM Mono',monospace">torch.hub</code> and <strong>frozen</strong>
        during training — only patch tokens (<code style="color:var(--accent2);font-family:'DM Mono',monospace">x_norm_patchtokens</code>)
        are extracted. Embedding dim: <strong>384</strong>.
      </div>
      <div class="pills" style="margin-top:16px;">
        <span class="pill green">384-dim embeddings</span>
        <span class="pill blue">No grad</span>
        <span class="pill">14×14 patches</span>
      </div>
    </div>

    <div class="card">
      <div class="card-label">Segmentation Head (Trainable)</div>
      <div class="card-title">SegmentationHeadConvNeXt</div>
      <div class="card-body">
        A lightweight ConvNeXt-inspired head. Patch tokens are reshaped into a 2D spatial grid,
        then processed through a <strong>stem</strong> (384→128, k=7) and a <strong>depthwise block</strong>
        (k=7 DW conv + pointwise + GELU). Final 1×1 conv maps to 10 class logits.
      </div>
      <div class="bar-chart" style="margin-top:16px;">
        <div class="bar-row">
          <span class="bar-label">Stem Conv</span>
          <div class="bar-track"><div class="bar-fill" style="width:60%;background:linear-gradient(to right,var(--accent),var(--accent2))"></div></div>
          <span class="bar-val">384→128</span>
        </div>
        <div class="bar-row">
          <span class="bar-label">DW Conv Block</span>
          <div class="bar-track"><div class="bar-fill" style="width:40%;background:linear-gradient(to right,var(--accent2),#a78bfa)"></div></div>
          <span class="bar-val">128→128</span>
        </div>
        <div class="bar-row">
          <span class="bar-label">Classifier</span>
          <div class="bar-track"><div class="bar-fill" style="width:15%;background:linear-gradient(to right,#a78bfa,var(--accent3))"></div></div>
          <span class="bar-val">128→10</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 3 — SEGMENTATION CLASSES
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">03</span>
    <h2 class="section-title">Segmentation Classes</h2>
    <div class="section-line"></div>
  </div>

  <p style="color:var(--muted);margin-bottom:28px;max-width:620px;">
    Grayscale masks use raw pixel values which are remapped to class IDs 0–9 at dataset load time via a
    <code style="color:var(--accent);font-family:'DM Mono',monospace">value_map</code> conversion.
  </p>

  <div class="class-grid">
    <div class="class-chip" style="background:rgba(0,0,0,0.3);">
      <div class="class-dot" style="background:#000;border:1px solid #444"></div>
      <div><div class="class-name">Background</div><div class="class-id">ID 0 · val 0</div></div>
    </div>
    <div class="class-chip" style="background:rgba(34,139,34,0.1);">
      <div class="class-dot" style="background:#228b22"></div>
      <div><div class="class-name">Trees</div><div class="class-id">ID 1 · val 100</div></div>
    </div>
    <div class="class-chip" style="background:rgba(0,255,0,0.08);">
      <div class="class-dot" style="background:#00ff00"></div>
      <div><div class="class-name">Lush Bushes</div><div class="class-id">ID 2 · val 200</div></div>
    </div>
    <div class="class-chip" style="background:rgba(210,180,140,0.1);">
      <div class="class-dot" style="background:#d2b48c"></div>
      <div><div class="class-name">Dry Grass</div><div class="class-id">ID 3 · val 300</div></div>
    </div>
    <div class="class-chip" style="background:rgba(139,90,43,0.12);">
      <div class="class-dot" style="background:#8b5a2b"></div>
      <div><div class="class-name">Dry Bushes</div><div class="class-id">ID 4 · val 500</div></div>
    </div>
    <div class="class-chip" style="background:rgba(128,128,0,0.12);">
      <div class="class-dot" style="background:#808000"></div>
      <div><div class="class-name">Ground Clutter</div><div class="class-id">ID 5 · val 550</div></div>
    </div>
    <div class="class-chip" style="background:rgba(139,69,19,0.12);">
      <div class="class-dot" style="background:#8b4513"></div>
      <div><div class="class-name">Logs</div><div class="class-id">ID 6 · val 700</div></div>
    </div>
    <div class="class-chip" style="background:rgba(128,128,128,0.12);">
      <div class="class-dot" style="background:#808080"></div>
      <div><div class="class-name">Rocks</div><div class="class-id">ID 7 · val 800</div></div>
    </div>
    <div class="class-chip" style="background:rgba(160,82,45,0.12);">
      <div class="class-dot" style="background:#a0522d"></div>
      <div><div class="class-name">Landscape</div><div class="class-id">ID 8 · val 7100</div></div>
    </div>
    <div class="class-chip" style="background:rgba(135,206,235,0.1);">
      <div class="class-dot" style="background:#87ceeb"></div>
      <div><div class="class-name">Sky</div><div class="class-id">ID 9 · val 10000</div></div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 4 — TRAINING CONFIGURATION
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">04</span>
    <h2 class="section-title">Training Configuration</h2>
    <div class="section-line"></div>
  </div>

  <div class="grid-4" style="margin-bottom:28px;">
    <div class="metric-card">
      <div class="metric-name">Batch Size</div>
      <div class="metric-value">2</div>
      <div class="metric-desc">GPU memory friendly</div>
    </div>
    <div class="metric-card">
      <div class="metric-name">Learning Rate</div>
      <div class="metric-value">1e-4</div>
      <div class="metric-desc">SGD + momentum 0.9</div>
    </div>
    <div class="metric-card">
      <div class="metric-name">Default Epochs</div>
      <div class="metric-value">10</div>
      <div class="metric-desc">configurable in main()</div>
    </div>
    <div class="metric-card">
      <div class="metric-name">Input Size</div>
      <div class="metric-value">462×476</div>
      <div class="metric-desc">patch-aligned (÷14)</div>
    </div>
  </div>

  <div class="code-block">
    <div class="code-header">
      <div class="code-dots"><div class="code-dot r"></div><div class="code-dot y"></div><div class="code-dot g"></div></div>
      <span class="code-filename">train_segmentation.py — Hyperparameters</span>
    </div>
    <pre><span class="cm"># Input resolution — snapped to multiples of 14 (patch size)</span>
w = <span class="fn">int</span>(((960 / 2) // 14) * 14)   <span class="cm"># → 476</span>
h = <span class="fn">int</span>(((540 / 2) // 14) * 14)   <span class="cm"># → 462 (height first!)</span>

<span class="cm"># Optimizer — SGD with momentum</span>
optimizer = optim.<span class="fn">SGD</span>(classifier.parameters(), lr=<span class="num">1e-4</span>, momentum=<span class="num">0.9</span>)

<span class="cm"># Loss — standard cross-entropy over 10 classes</span>
loss_fct = torch.nn.<span class="fn">CrossEntropyLoss</span>()

<span class="cm"># Backbone frozen — no gradient flows back</span>
<span class="kw">with</span> torch.no_grad():
    output = backbone_model.<span class="fn">forward_features</span>(imgs)[<span class="str">"x_norm_patchtokens"</span>]</pre>
  </div>

  <div class="code-block">
    <div class="code-header">
      <div class="code-dots"><div class="code-dot r"></div><div class="code-dot y"></div><div class="code-dot g"></div></div>
      <span class="code-filename">train_segmentation.py — Data Transforms</span>
    </div>
    <pre>transform = transforms.<span class="fn">Compose</span>([
    transforms.<span class="fn">Resize</span>((h, w)),
    transforms.<span class="fn">ToTensor</span>(),
    transforms.<span class="fn">Normalize</span>(mean=[<span class="num">0.485</span>, <span class="num">0.456</span>, <span class="num">0.406</span>],   <span class="cm"># ImageNet mean</span>
                           std =[<span class="num">0.229</span>, <span class="num">0.224</span>, <span class="num">0.225</span>])  <span class="cm"># ImageNet std</span>
])

mask_transform = transforms.<span class="fn">Compose</span>([
    transforms.<span class="fn">Resize</span>((h, w)),
    transforms.<span class="fn">ToTensor</span>(),      <span class="cm"># [0,1] float</span>
])
<span class="cm"># Mask is scaled back: mask * 255 → class IDs 0–9</span></pre>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 5 — METRICS
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">05</span>
    <h2 class="section-title">Evaluation Metrics</h2>
    <div class="section-line"></div>
  </div>

  <div class="grid-3">
    <div class="card">
      <div class="card-label">Primary Metric</div>
      <div class="card-title">Mean IoU (mIoU)</div>
      <div class="card-body">
        Intersection-over-Union averaged across all 10 classes.
        NaN classes (absent from a batch) are excluded using <code style="color:var(--accent);font-family:'DM Mono',monospace">np.nanmean</code>.
        This is the main benchmark metric for semantic segmentation quality.
      </div>
      <div class="pills">
        <span class="pill green">nanmean across classes</span>
        <span class="pill">ignore_index=255</span>
      </div>
    </div>
    <div class="card">
      <div class="card-label">Secondary Metric</div>
      <div class="card-title">Dice Score (F1)</div>
      <div class="card-body">
        2 × Intersection / (Pred + GT + ε). Computed per class and averaged.
        Smooth factor ε = 1e-6 prevents division by zero.
        Particularly useful for class-imbalanced datasets like off-road terrain.
      </div>
      <div class="pills">
        <span class="pill blue">smooth = 1e-6</span>
        <span class="pill">mean over classes</span>
      </div>
    </div>
    <div class="card">
      <div class="card-label">Tertiary Metric</div>
      <div class="card-title">Pixel Accuracy</div>
      <div class="card-body">
        Fraction of correctly classified pixels across the entire image.
        Computed as
        <code style="color:var(--accent);font-family:'DM Mono',monospace">(argmax(logits) == labels).mean()</code>.
        Fast to compute; a good sanity check but can be misleading with class imbalance.
      </div>
      <div class="pills">
        <span class="pill orange">per-pixel</span>
        <span class="pill">global average</span>
      </div>
    </div>
  </div>

  <div style="margin-top:28px;">
    <div class="code-block">
      <div class="code-header">
        <div class="code-dots"><div class="code-dot r"></div><div class="code-dot y"></div><div class="code-dot g"></div></div>
        <span class="code-filename">train_segmentation.py — compute_iou()</span>
      </div>
      <pre><span class="kw">def</span> <span class="fn">compute_iou</span>(pred, target, num_classes=<span class="num">10</span>, ignore_index=<span class="num">255</span>):
    pred = torch.<span class="fn">argmax</span>(pred, dim=<span class="num">1</span>)          <span class="cm"># (B, H, W) class indices</span>
    pred, target = pred.<span class="fn">view</span>(-<span class="num">1</span>), target.<span class="fn">view</span>(-<span class="num">1</span>)  <span class="cm"># flatten</span>

    iou_per_class = []
    <span class="kw">for</span> class_id <span class="kw">in</span> <span class="fn">range</span>(num_classes):
        pred_inds   = pred   == class_id
        target_inds = target == class_id
        intersection = (pred_inds & target_inds).<span class="fn">sum</span>().<span class="fn">float</span>()
        union        = (pred_inds | target_inds).<span class="fn">sum</span>().<span class="fn">float</span>()
        <span class="kw">if</span> union == <span class="num">0</span>: iou_per_class.<span class="fn">append</span>(<span class="fn">float</span>(<span class="str">'nan'</span>))
        <span class="kw">else</span>: iou_per_class.<span class="fn">append</span>((intersection / union).<span class="fn">cpu</span>().<span class="fn">numpy</span>())

    <span class="kw">return</span> np.<span class="fn">nanmean</span>(iou_per_class)</pre>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 6 — TRAINING WORKFLOW
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">06</span>
    <h2 class="section-title">Training Workflow</h2>
    <div class="section-line"></div>
  </div>

  <div class="steps">
    <div class="step">
      <div class="step-line"></div>
      <div class="step-num">1</div>
      <div class="step-content">
        <div class="step-title">Environment Setup</div>
        <div class="step-body">
          Run <code style="color:var(--accent);font-family:'DM Mono',monospace">ENV_SETUP/create_env.bat</code> to create the Conda <em>EDU</em> environment,
          then <code style="color:var(--accent);font-family:'DM Mono',monospace">install_packages.bat</code> to install
          PyTorch + CUDA 11.8, Torchvision, Ultralytics, OpenCV, and tqdm.
        </div>
        <div class="pills">
          <span class="pill">conda env: EDU</span>
          <span class="pill blue">CUDA 11.8</span>
          <span class="pill">opencv-contrib-python</span>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-line"></div>
      <div class="step-num">2</div>
      <div class="step-content">
        <div class="step-title">Prepare Dataset</div>
        <div class="step-body">
          Ensure <code style="color:var(--accent2);font-family:'DM Mono',monospace">../Offroad_Segmentation_Training_Dataset/train/</code>
          and <code style="color:var(--accent2);font-family:'DM Mono',monospace">../val/</code> directories exist,
          each containing <code style="color:var(--accent);font-family:'DM Mono',monospace">Color_Images/</code>
          and <code style="color:var(--accent);font-family:'DM Mono',monospace">Segmentation/</code> subdirectories
          with matching filenames.
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-line"></div>
      <div class="step-num">3</div>
      <div class="step-content">
        <div class="step-title">Run Training</div>
        <div class="step-body">
          <code style="color:var(--accent);font-family:'DM Mono',monospace">python train_segmentation.py</code> —
          DINOv2 backbone auto-downloads on first run. Training loops over <em>n_epochs</em>,
          evaluating full IoU/Dice/Accuracy on both train and val after each epoch.
        </div>
        <div class="pills">
          <span class="pill green">tqdm progress bars</span>
          <span class="pill">auto model download</span>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-line"></div>
      <div class="step-num">4</div>
      <div class="step-content">
        <div class="step-title">Outputs Saved</div>
        <div class="step-body">
          Model weights → <code style="color:var(--accent);font-family:'DM Mono',monospace">segmentation_head.pth</code>.
          Training plots → <code style="color:var(--accent);font-family:'DM Mono',monospace">train_stats/</code>
          (loss, IoU, Dice, pixel accuracy curves + combined). Metrics log →
          <code style="color:var(--accent);font-family:'DM Mono',monospace">train_stats/evaluation_metrics.txt</code>.
        </div>
        <div class="pills">
          <span class="pill orange">training_curves.png</span>
          <span class="pill orange">iou_curves.png</span>
          <span class="pill orange">dice_curves.png</span>
          <span class="pill orange">all_metrics_curves.png</span>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-num">5</div>
      <div class="step-content">
        <div class="step-title">Run Inference / Test</div>
        <div class="step-body">
          <code style="color:var(--accent);font-family:'DM Mono',monospace">python test_segmentation.py [--model_path ...] [--data_dir ...] [--num_samples N]</code> —
          Loads trained weights, runs inference on all test images, saves raw masks, colored overlays,
          side-by-side comparisons, and a per-class IoU bar chart.
        </div>
        <div class="pills">
          <span class="pill blue">masks/</span>
          <span class="pill blue">masks_color/</span>
          <span class="pill blue">comparisons/</span>
          <span class="pill blue">per_class_metrics.png</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 7 — OUTPUTS PRODUCED
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">07</span>
    <h2 class="section-title">Script Outputs at a Glance</h2>
    <div class="section-line"></div>
  </div>

  <div class="grid-3">
    <div class="card">
      <div class="card-label">train_segmentation.py</div>
      <div class="card-title">Training Outputs</div>
      <div class="card-body">
        After training completes, produces model weights and four matplotlib plots saved under
        <code style="color:var(--accent);font-family:'DM Mono',monospace">train_stats/</code>.
        Also writes a structured per-epoch metrics table to
        <code style="color:var(--accent);font-family:'DM Mono',monospace">evaluation_metrics.txt</code>
        with best-epoch tracking for val IoU, Dice, and accuracy.
      </div>
    </div>
    <div class="card">
      <div class="card-label">test_segmentation.py</div>
      <div class="card-title">Inference Outputs</div>
      <div class="card-body">
        For <strong>every</strong> image: raw class-ID mask (0–9) and an RGB-colorized mask.
        For the first <code style="color:var(--accent2);font-family:'DM Mono',monospace">--num_samples</code> images:
        a 3-panel comparison (Input | Ground Truth | Prediction).
        Saves a per-class IoU bar chart. All backed by argparse CLI.
      </div>
    </div>
    <div class="card">
      <div class="card-label">visualize.py</div>
      <div class="card-title">Standalone Colorizer</div>
      <div class="card-body">
        Independent utility. Set <code style="color:var(--accent);font-family:'DM Mono',monospace">input_folder</code>
        to any directory of mask images. Assigns consistent random colors to each unique pixel value
        across all files (shared <code style="color:var(--accent);font-family:'DM Mono',monospace">color_map</code>)
        and saves to a <code style="color:var(--accent);font-family:'DM Mono',monospace">colorized/</code>
        subfolder.
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 8 — ISSUES & IMPROVEMENTS
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">08</span>
    <h2 class="section-title">Issues & Suggested Improvements</h2>
    <div class="section-line"></div>
  </div>

  <div class="card" style="margin-bottom:0;">
    <div class="improvement-item">
      <div class="imp-icon">⚠️</div>
      <div>
        <div class="imp-title">Double Metric Eval on Train Set Each Epoch</div>
        <div class="imp-body">
          After each epoch <code style="color:var(--accent);font-family:'DM Mono',monospace">evaluate_metrics()</code> runs a full
          forward pass over the <em>entire train loader</em> (in addition to the train loop itself).
          For large datasets this roughly <strong>doubles</strong> epoch time. Consider tracking train loss
          only during the loop and running full evaluation at a lower frequency (e.g., every 5 epochs).
        </div>
      </div>
      <div class="priority high">HIGH</div>
    </div>

    <div class="improvement-item">
      <div class="imp-icon">🔧</div>
      <div>
        <div class="imp-title">No Learning Rate Scheduler</div>
        <div class="imp-body">
          The optimizer uses a fixed LR of 1e-4. Adding a
          <code style="color:var(--accent2);font-family:'DM Mono',monospace">CosineAnnealingLR</code> or
          <code style="color:var(--accent2);font-family:'DM Mono',monospace">ReduceLROnPlateau</code> scheduler
          could meaningfully improve convergence, especially with the frozen backbone.
        </div>
      </div>
      <div class="priority high">HIGH</div>
    </div>

    <div class="improvement-item">
      <div class="imp-icon">💾</div>
      <div>
        <div class="imp-title">No Best-Model Checkpointing</div>
        <div class="imp-body">
          The model is only saved once at the end of training. If training diverges or overfits late,
          the saved weights may be suboptimal. Add early stopping + save the checkpoint with the best
          <code style="color:var(--accent);font-family:'DM Mono',monospace">val_iou</code>.
        </div>
      </div>
      <div class="priority high">HIGH</div>
    </div>

    <div class="improvement-item">
      <div class="imp-icon">⚖️</div>
      <div>
        <div class="imp-title">Class Imbalance Not Addressed</div>
        <div class="imp-body">
          Off-road scenes are heavily skewed (Sky & Landscape dominate). Using
          <code style="color:var(--accent);font-family:'DM Mono',monospace">CrossEntropyLoss(weight=class_weights)</code>
          or adding a <strong>focal loss</strong> component would help rare classes like Logs and Rocks.
        </div>
      </div>
      <div class="priority high">HIGH</div>
    </div>

    <div class="improvement-item">
      <div class="imp-icon">🎲</div>
      <div>
        <div class="imp-title">No Data Augmentation</div>
        <div class="imp-body">
          Training transforms only resize and normalize. Adding random horizontal flips, color jitter,
          and random crops (applied consistently to image + mask) can significantly boost generalization
          for off-road imagery.
        </div>
      </div>
      <div class="priority medium">MEDIUM</div>
    </div>

    <div class="improvement-item">
      <div class="imp-icon">🏷️</div>
      <div>
        <div class="imp-title">Hardcoded Paths in visualize.py</div>
        <div class="imp-body">
          <code style="color:var(--accent);font-family:'DM Mono',monospace">input_folder = " "</code> (a space) will cause a silent crash.
          Migrate to <code style="color:var(--accent2);font-family:'DM Mono',monospace">argparse</code> for consistency with the other scripts.
        </div>
      </div>
      <div class="priority medium">MEDIUM</div>
    </div>

    <div class="improvement-item">
      <div class="imp-icon">🔁</div>
      <div>
        <div class="imp-title">No Resume / Epoch Continuation</div>
        <div class="imp-body">
          Training always starts from scratch. Saving optimizer state alongside model weights and
          accepting a <code style="color:var(--accent);font-family:'DM Mono',monospace">--resume</code> flag would allow interrupted runs to continue.
        </div>
      </div>
      <div class="priority low">LOW</div>
    </div>

    <div class="improvement-item" style="border-bottom:none;">
      <div class="imp-icon">🧪</div>
      <div>
        <div class="imp-title">Code Duplication Between Scripts</div>
        <div class="imp-body">
          <code style="color:var(--accent);font-family:'DM Mono',monospace">MaskDataset</code>,
          <code style="color:var(--accent);font-family:'DM Mono',monospace">SegmentationHeadConvNeXt</code>,
          <code style="color:var(--accent);font-family:'DM Mono',monospace">value_map</code>, and metric functions are copy-pasted between
          train and test scripts. Extract into a shared
          <code style="color:var(--accent2);font-family:'DM Mono',monospace">model.py</code> /
          <code style="color:var(--accent2);font-family:'DM Mono',monospace">dataset.py</code> /
          <code style="color:var(--accent2);font-family:'DM Mono',monospace">metrics.py</code> module set.
        </div>
      </div>
      <div class="priority low">LOW</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SECTION 9 — QUICK START
═══════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">09</span>
    <h2 class="section-title">Quick Start Commands</h2>
    <div class="section-line"></div>
  </div>

  <div class="code-block">
    <div class="code-header">
      <div class="code-dots"><div class="code-dot r"></div><div class="code-dot y"></div><div class="code-dot g"></div></div>
      <span class="code-filename">shell — Setup → Train → Test</span>
    </div>
    <pre><span class="cm"># 1. Create & activate conda environment (Windows)</span>
ENV_SETUP\create_env.bat
ENV_SETUP\install_packages.bat
conda activate EDU

<span class="cm"># 2. Train (outputs: segmentation_head.pth + train_stats/)</span>
python train_segmentation.py

<span class="cm"># 3. Inference on test images</span>
python test_segmentation.py \
    --model_path segmentation_head.pth \
    --data_dir ../Offroad_Segmentation_testImages \
    --output_dir ./predictions \
    --num_samples 10

<span class="cm"># 4. Colorize arbitrary mask folder</span>
<span class="cm"># Edit visualize.py → set input_folder, then:</span>
python visualize.py</pre>
  </div>
</div>

</div><!-- /container -->

<div style="text-align:center;padding:48px 24px;color:var(--muted);font-family:'DM Mono',monospace;font-size:11px;border-top:1px solid var(--border);margin-top:40px;position:relative;z-index:1;">
  OFFROAD SEGMENTATION · DINOV2 + CONVNEXT HEAD · PYTORCH · AUTO-GENERATED DOCUMENTATION
</div>

</body>
</html>