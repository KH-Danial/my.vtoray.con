<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>V2Ray Config Hub | داشبورد مدیریت کانفیگ</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: system-ui, 'Segoe UI', 'Inter', -apple-system, sans-serif;
        }

        :root {
            --bg-start: #f8fafc;
            --bg-end: #e2e8f0;
            --card-bg: rgba(255, 255, 255, 0.75);
            --card-border: rgba(255, 255, 255, 0.5);
            --text-primary: #0f172a;
            --text-secondary: #334155;
            --text-muted: #64748b;
            --shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
            --accent: #4f46e5;
            --success: #10b981;
            --danger: #ef4444;
            --header-blur: rgba(255, 255, 255, 0.85);
            --border-light: rgba(0, 0, 0, 0.08);
        }

        body.dark {
            --bg-start: #0f172a;
            --bg-end: #020617;
            --card-bg: rgba(30, 41, 59, 0.75);
            --card-border: rgba(255, 255, 255, 0.1);
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            --header-blur: rgba(15, 23, 42, 0.85);
            --border-light: rgba(255, 255, 255, 0.1);
        }

        body {
            background: linear-gradient(135deg, var(--bg-start), var(--bg-end));
            min-height: 100vh;
            padding: 2rem 1rem;
            transition: all 0.3s ease;
            color: var(--text-primary);
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            width: 100%;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 2rem;
            padding: 1rem 1.5rem;
            background: var(--header-blur);
            backdrop-filter: blur(12px);
            border-radius: 1.5rem;
            border: 1px solid var(--card-border);
            box-shadow: var(--shadow);
        }

        .title-section h1 {
            font-size: 1.6rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent), #a855f7);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
        }

        .title-section p {
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        .theme-toggle {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 2rem;
            padding: 0.5rem 1rem;
            cursor: pointer;
            font-weight: 500;
            color: var(--text-primary);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1.2rem;
            margin-bottom: 2.5rem;
        }

        .stat-card {
            background: var(--card-bg);
            backdrop-filter: blur(8px);
            border: 1px solid var(--card-border);
            border-radius: 1.2rem;
            padding: 1rem 1.2rem;
            transition: transform 0.2s;
            box-shadow: var(--shadow);
        }

        .stat-card:hover { transform: translateY(-3px); }
        .stat-icon { font-size: 1.8rem; color: var(--accent); margin-bottom: 0.5rem; }
        .stat-value { font-size: 1.8rem; font-weight: 800; line-height: 1.2; }
        .stat-label { font-size: 0.75rem; color: var(--text-muted); }

        /* کارت آخرین بروزرسانی: فونت کوچک‌تر و دو خطی */
        .stat-card-lastupdate .stat-value {
            font-size: 1rem;
            font-weight: 500;
            line-height: 1.4;
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
        }
        .stat-card-lastupdate .stat-value span:first-child {
            font-size: 0.9rem;
            font-weight: 600;
        }
        .stat-card-lastupdate .stat-value span:last-child {
            font-size: 0.85rem;
            font-weight: normal;
            color: var(--text-muted);
        }

        .protocols-section { margin-bottom: 2rem; }
        
        .section-title {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1.2rem;
            display: flex;
            align-items: baseline;
            flex-wrap: wrap;
            gap: 0.5rem 1rem;
            border-right: 3px solid var(--accent);
            padding-right: 0.8rem;
        }
        .section-title .main-title {
            font-size: 1.3rem;
            font-weight: 600;
        }
        .section-subnote {
            font-size: 0.65rem;
            font-weight: normal;
            color: var(--text-muted);
            background: rgba(0,0,0,0.05);
            padding: 0.2rem 0.6rem;
            border-radius: 2rem;
            white-space: nowrap;
        }
        @media (max-width: 640px) {
            .section-subnote {
                white-space: normal;
                font-size: 0.6rem;
            }
        }

        .protocols-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 1.5rem;
        }

        .protocol-card {
            background: var(--card-bg);
            backdrop-filter: blur(8px);
            border: 1px solid var(--card-border);
            border-radius: 1.2rem;
            overflow: visible;
            box-shadow: var(--shadow);
            transition: all 0.2s;
        }

        .protocol-header {
            padding: 1rem 1.2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.8rem;
            cursor: pointer;
            border-bottom: 1px solid var(--border-light);
            background: inherit;
            border-radius: 1.2rem 1.2rem 0 0;
        }

        .protocol-name {
            font-size: 1.1rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .protocol-name i { color: var(--accent); width: 1.5rem; }

        .protocol-stats {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            font-size: 0.75rem;
        }
        .protocol-stats span {
            background: rgba(0,0,0,0.15);
            padding: 0.2rem 0.5rem;
            border-radius: 1rem;
        }

        .protocol-body {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .protocol-card.open .protocol-body {
            max-height: 2000px;
            overflow-y: auto;
        }

        .file-list {
            padding: 0.8rem 1rem 1rem;
            display: flex;
            flex-direction: column;
            gap: 0.7rem;
        }

        .file-item {
            background: rgba(255,255,255,0.05);
            border-radius: 0.9rem;
            padding: 0.7rem 0.9rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.5rem;
            transition: all 0.15s;
            border: 1px solid transparent;
        }
        .file-item:hover { border-color: var(--accent); }

        .file-info {
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
            flex: 2;
            min-width: 140px;
        }
        .file-name {
            font-weight: 600;
            font-size: 0.85rem;
            font-family: monospace;
            word-break: break-word;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        .online-status {
            font-size: 0.7rem;
            display: inline-flex;
            align-items: center;
            gap: 0.2rem;
            background: rgba(0,0,0,0.2);
            padding: 0.1rem 0.4rem;
            border-radius: 1rem;
        }
        .online-status .online { color: var(--success); }
        .online-status .offline { color: var(--danger); }

        .file-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
            font-size: 0.65rem;
            color: var(--text-muted);
        }

        .download-btn {
            background: var(--accent);
            color: white;
            border-radius: 2rem;
            padding: 0.3rem 0.9rem;
            font-size: 0.7rem;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: 0.2s;
        }
        .download-btn:hover { opacity: 0.85; transform: scale(0.98); }

        .chart-container {
            background: var(--card-bg);
            backdrop-filter: blur(8px);
            border-radius: 1.2rem;
            padding: 1rem;
            border: 1px solid var(--card-border);
            margin-top: 1.5rem;
            position: relative;
            z-index: 1;
        }

        footer {
            text-align: center;
            margin-top: 2rem;
            padding: 1rem;
            color: var(--text-muted);
            font-size: 0.75rem;
            border-top: 1px solid var(--border-light);
        }

        .loading, .error-message {
            text-align: center;
            padding: 2rem;
            background: var(--card-bg);
            border-radius: 1.2rem;
            grid-column: 1 / -1;
        }

        @keyframes spin { to { transform: rotate(360deg); } }
        .fa-spinner { animation: spin 1s linear infinite; }

        @media (max-width: 640px) {
            body { padding: 1rem 0.8rem; }
            .protocols-grid { grid-template-columns: 1fr; }
            .file-item { flex-direction: column; align-items: stretch; }
            .download-btn { align-self: flex-start; }
            .stat-value { font-size: 1.4rem; }
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <div class="title-section">
            <h1><i class="fas fa-network-wired"></i> V2Ray Config Hub</h1>
            <p>مدیریت پویای کانفیگ‌ها | بروزرسانی لحظه‌ای</p>
        </div>
        <button class="theme-toggle" id="themeToggle"><i class="fas fa-moon"></i> تم شب</button>
    </div>

    <div class="stats-grid" id="statsPanel">
        <div class="stat-card"><div class="stat-icon"><i class="fas fa-chart-line"></i></div><div class="stat-value" id="totalConfigs">-</div><div class="stat-label">مجموع کانفیگ‌ها</div></div>
        <div class="stat-card"><div class="stat-icon"><i class="fas fa-code-branch"></i></div><div class="stat-value" id="totalFiles">-</div><div class="stat-label">فایل‌های پیکربندی</div></div>
        <div class="stat-card"><div class="stat-icon"><i class="fas fa-database"></i></div><div class="stat-value" id="totalSize">-</div><div class="stat-label">حجم کل (MB)</div></div>
        <div class="stat-card stat-card-lastupdate">
            <div class="stat-icon"><i class="fas fa-clock"></i></div>
            <div class="stat-value" id="lastUpdate"></div>
            <div class="stat-label">آخرین بروزرسانی</div>
        </div>
    </div>

    <div class="protocols-section">
        <div class="section-title">
            <span class="main-title"><i class="fas fa-cubes"></i> پروتکل‌های فعال</span>
            <span class="section-subnote">تمامی پروتکل‌ها و تمامی فایل‌ها هر 6 ساعت بروزرسانی می‌شوند.</span>
        </div>
        <div id="protocolsGrid" class="protocols-grid"><div class="loading"><i class="fas fa-spinner fa-pulse"></i> بارگذاری...</div></div>
    </div>

    <div class="chart-container">
        <canvas id="healthChart"></canvas>
    </div>
    <footer><i class="fas fa-sync-alt"></i> به‌روزرسانی خودکار با GitHub Actions | وضعیت آنلاین فایل‌ها بررسی می‌شود.</footer>
</div>

<script>
    let healthChart = null;
    const onlineCache = new Map();

    // Theme
    const themeToggle = document.getElementById('themeToggle');
    if (localStorage.getItem('v2ray_theme') === 'dark') {
        document.body.classList.add('dark');
        themeToggle.innerHTML = '<i class="fas fa-sun"></i> تم روز';
    } else {
        themeToggle.innerHTML = '<i class="fas fa-moon"></i> تم شب';
    }
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark');
        const isDark = document.body.classList.contains('dark');
        localStorage.setItem('v2ray_theme', isDark ? 'dark' : 'light');
        themeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i> تم روز' : '<i class="fas fa-moon"></i> تم شب';
        if (healthChart) healthChart.update();
    });

    function formatBytes(bytes) {
        if (bytes === 0) return '0 B';
        return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
    }

    // تبدیل تاریخ به دو خط: خط اول تاریخ شمسی، خط دوم ساعت
    function formatLastUpdate(isoString) {
        if (!isoString) return '<span>نامشخص</span><span></span>';
        const date = new Date(isoString);
        const full = date.toLocaleString('fa-IR', { dateStyle: 'medium', timeStyle: 'short' });
        const parts = full.split('،');
        if (parts.length === 2) {
            return `<span>${parts[0].trim()}</span><span>${parts[1].trim()}</span>`;
        }
        const dateOnly = date.toLocaleDateString('fa-IR');
        const timeOnly = date.toLocaleTimeString('fa-IR', { hour: '2-digit', minute: '2-digit' });
        return `<span>${dateOnly}</span><span>${timeOnly}</span>`;
    }

    async function checkFileStatus(url) {
        if (onlineCache.has(url)) return onlineCache.get(url);
        try {
            const controller = new AbortController();
            const timeout = setTimeout(() => controller.abort(), 3000);
            const res = await fetch(url, { method: 'HEAD', signal: controller.signal });
            clearTimeout(timeout);
            onlineCache.set(url, res.ok);
            return res.ok;
        } catch {
            onlineCache.set(url, false);
            return false;
        }
    }

    // تابع کمکی برای دریافت درصد سلامت با در نظر گرفتن نگاشت ss <-> shadowsocks
    function getHealthPercent(proto, stats) {
        // اگر پروتکل 'ss' است، در stats با کلید 'shadowsocks' ذخیره شده
        let key = proto;
        if (proto === 'ss') key = 'shadowsocks';
        const healthValue = stats[key]?.health_sample?.percent || 0;
        return parseFloat(healthValue).toFixed(1);
    }

    async function loadDashboard() {
        const grid = document.getElementById('protocolsGrid');
        try {
            const [metadataRes, statsRes] = await Promise.all([
                fetch('config/metadata.json?t=' + Date.now()),
                fetch('stats.json?t=' + Date.now())
            ]);
            if (!metadataRes.ok || !statsRes.ok) throw new Error('خطا در دریافت داده');
            const metadata = await metadataRes.json();
            const stats = await statsRes.json();

            // آمار کلی
            const totalConfigs = stats.summary?.total_configs || 
                                 Object.values(stats).reduce((acc, p) => acc + (p.raw_count || 0), 0);
            const totalFiles = Object.values(metadata.protocols).reduce((acc, p) => acc + (p.files?.length || 0), 0);
            const totalSizeBytes = Object.values(metadata.protocols).reduce((acc, p) => acc + (p.total_size_bytes || 0), 0);

            document.getElementById('totalConfigs').innerText = totalConfigs.toLocaleString();
            document.getElementById('totalFiles').innerText = totalFiles;
            document.getElementById('totalSize').innerText = formatBytes(totalSizeBytes);
            document.getElementById('lastUpdate').innerHTML = formatLastUpdate(metadata.last_update);

            const protocols = Object.entries(metadata.protocols);
            if (!protocols.length) {
                grid.innerHTML = '<div class="error-message">هیچ پروتکلی یافت نشد</div>';
                return;
            }

            let html = '';
            for (const [proto, data] of protocols) {
                const files = data.files || [];
                const totalConfigsProto = data.total_configs || files.reduce((s,f)=> s + (f.config_count || 0), 0);
                // دریافت درصد سلامت با استفاده از تابع کمکی
                let health = getHealthPercent(proto, stats);
                const healthNum = parseFloat(health);
                const healthColor = healthNum >= 60 ? '#10b981' : (healthNum >= 30 ? '#f59e0b' : '#ef4444');

                // نام نمایشی: برای ss همان "ss" باقی می‌ماند
                let displayName = proto.toUpperCase();
                if (proto === 'shadowsocks') displayName = 'SS';
                else if (proto === 'ss') displayName = 'SS';

                let filesHtml = '';
                for (const file of files) {
                    const fileUrl = file.path;
                    filesHtml += `
                        <div class="file-item" data-file-url="${fileUrl}">
                            <div class="file-info">
                                <div class="file-name">
                                    <i class="fas fa-file-alt"></i> ${file.name}
                                    <span class="online-status" id="status-${file.name.replace(/[^a-zA-Z0-9]/g,'-')}"><i class="fas fa-spinner fa-pulse"></i> بررسی...</span>
                                </div>
                                <div class="file-meta">
                                    <span><i class="fas fa-weight-hanging"></i> ${formatBytes(file.size_bytes)}</span>
                                    <span><i class="fas fa-hashtag"></i> ${file.config_count || 0} کانفیگ</span>
                                    ${file.parts > 1 ? `<span><i class="fas fa-layer-group"></i> بخش ${file.parts}</span>` : ''}
                                </div>
                            </div>
                            <a href="${fileUrl}" class="download-btn" download><i class="fas fa-download"></i> دریافت</a>
                        </div>
                    `;
                }

                html += `
                    <div class="protocol-card">
                        <div class="protocol-header" onclick="this.closest('.protocol-card').classList.toggle('open')">
                            <div class="protocol-name"><i class="fas fa-shield-alt"></i> ${displayName}</div>
                            <div class="protocol-stats">
                                <span><i class="fas fa-database"></i> ${totalConfigsProto.toLocaleString()}</span>
                                <span><i class="fas fa-file"></i> ${files.length}</span>
                                <span style="color:${healthColor}; background:rgba(0,0,0,0.15); padding:0.2rem 0.5rem; border-radius:1rem;">
                                    <i class="fas fa-heartbeat"></i> ${health}%
                                </span>
                            </div>
                        </div>
                        <div class="protocol-body"><div class="file-list">${filesHtml || '<div class="file-item">فاقد فایل</div>'}</div></div>
                    </div>
                `;
            }
            grid.innerHTML = html;

            // بررسی وضعیت آنلاین فایل‌ها
            const fileItems = document.querySelectorAll('.file-item');
            for (const item of fileItems) {
                const url = item.getAttribute('data-file-url');
                if (!url) continue;
                const statusSpan = item.querySelector('.online-status');
                if (!statusSpan) continue;
                const isOnline = await checkFileStatus(url);
                statusSpan.innerHTML = isOnline ? '<i class="fas fa-check-circle online"></i> قابل دسترس' : '<i class="fas fa-times-circle offline"></i> غیرقابل دسترس';
            }

            // رسم نمودار سلامت با یک رقم اعشار (با نگاشت صحیح)
            const ctx = document.getElementById('healthChart').getContext('2d');
            const labels = [];
            const healthData = [];
            // برای هر پروتکل موجود در metadata، درصد را از stats می‌گیریم (با نگاشت)
            for (const [proto, data] of protocols) {
                let key = proto;
                if (proto === 'ss') key = 'shadowsocks';
                if (stats[key]?.health_sample) {
                    labels.push(proto === 'ss' ? 'SS' : proto.toUpperCase());
                    healthData.push(parseFloat(stats[key].health_sample.percent).toFixed(1));
                }
            }
            if (healthChart) healthChart.destroy();
            healthChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'نرخ سلامت کانفیگ‌ها (%)',
                        data: healthData,
                        backgroundColor: 'rgba(79, 70, 229, 0.7)',
                        borderRadius: 8
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    plugins: {
                        legend: { position: 'top', labels: { color: getComputedStyle(document.body).getPropertyValue('--text-primary') } },
                        tooltip: { callbacks: { label: (ctx) => `${ctx.raw}% کانفیگ فعال` } }
                    },
                    scales: {
                        y: { beginAtZero: true, max: 100, title: { display: true, text: 'درصد سلامت', color: '#94a3b8' }, ticks: { callback: (val) => val + '%' } }
                    }
                }
            });
        } catch (err) {
            console.error(err);
            grid.innerHTML = `<div class="error-message"><i class="fas fa-exclamation-triangle"></i> خطا: ${err.message}</div>`;
        }
    }

    new MutationObserver(() => { if (healthChart) healthChart.update(); }).observe(document.body, { attributes: true, attributeFilter: ['class'] });
    loadDashboard();
</script>
</body>
</html>
