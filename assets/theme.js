/* Shared theme + mobile menu — Sagelight Studio */
(function () {
    var themes = ['dark', 'light', 'system'];
    var icons = { dark: '☾', light: '☀', system: '◑' };
    var labels = {
        dark: 'Theme: dark. Activate to switch to light theme.',
        light: 'Theme: light. Activate to switch to system theme.',
        system: 'Theme: system. Activate to switch to dark theme.'
    };
    var idx = 0;

    function systemTheme() {
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    function apply(t) {
        var resolved = t === 'system' ? systemTheme() : t;
        document.documentElement.setAttribute('data-theme', resolved);
        var iconEl = document.getElementById('themeIcon');
        if (iconEl) iconEl.textContent = icons[t];
        var btn = document.getElementById('themeToggle');
        if (btn) btn.setAttribute('aria-label', labels[t]);
        try { localStorage.setItem('sage-theme', t); } catch (e) {}
    }

    window.cycleTheme = function () {
        idx = (idx + 1) % themes.length;
        apply(themes[idx]);
    };

    window.toggleMobileMenu = function () {
        var nav = document.getElementById('navTabs') || document.getElementById('navLinks');
        if (!nav) return;
        var isOpen = nav.classList.toggle('nav__tabs--open');
        var btn = document.getElementById('mobileMenuBtn');
        if (btn) {
            btn.setAttribute('aria-expanded', String(isOpen));
            btn.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
        }
    };

    var saved;
    try { saved = localStorage.getItem('sage-theme'); } catch (e) {}
    if (saved && themes.indexOf(saved) !== -1) idx = themes.indexOf(saved);
    apply(themes[idx]);

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
        if (themes[idx] === 'system') apply('system');
    });

    document.addEventListener('click', function (e) {
        var nav = document.querySelector('.nav');
        if (nav && !nav.contains(e.target)) {
            var tabs = document.getElementById('navTabs') || document.getElementById('navLinks');
            if (tabs && tabs.classList.contains('nav__tabs--open')) {
                tabs.classList.remove('nav__tabs--open');
                var btn = document.getElementById('mobileMenuBtn');
                if (btn) {
                    btn.setAttribute('aria-expanded', 'false');
                    btn.setAttribute('aria-label', 'Open menu');
                }
            }
        }
    });
})();
