/* ============================================================
   Sagelight Studio — Cookie Consent (Google Consent Mode v2 — Advanced)
   Loaded on every page after gtag is initialized in <head>.
   Implements granular advertising / analytics consent per GDPR Art. 7.
   ============================================================ */
(function () {
    'use strict';

    var STORAGE_KEY = 'sage-consent-v2';
    // Map our two user-facing categories onto Google's four signals.
    var SIGNAL_GROUPS = {
        advertising: ['ad_storage', 'ad_user_data', 'ad_personalization'],
        analytics:   ['analytics_storage']
    };

    function gtag() {
        if (typeof window.gtag === 'function') {
            window.gtag.apply(window, arguments);
        }
    }

    function readChoice() {
        try {
            var raw = localStorage.getItem(STORAGE_KEY);
            if (!raw) return null;
            var parsed = JSON.parse(raw);
            // Backward compat with v1 single-toggle storage:
            if (parsed && typeof parsed.analytics === 'undefined' && typeof parsed.advertising === 'boolean') {
                parsed.analytics = parsed.advertising;
            }
            return parsed;
        } catch (e) { return null; }
    }

    function saveChoice(choice) {
        try { localStorage.setItem(STORAGE_KEY, JSON.stringify(choice)); } catch (e) {}
    }

    function applyChoice(choice) {
        var update = {};
        Object.keys(SIGNAL_GROUPS).forEach(function (group) {
            var state = choice[group] ? 'granted' : 'denied';
            SIGNAL_GROUPS[group].forEach(function (s) { update[s] = state; });
        });
        gtag('consent', 'update', update);
    }

    // ---------- DOM helper ----------
    function el(tag, attrs, children) {
        var node = document.createElement(tag);
        if (attrs) {
            Object.keys(attrs).forEach(function (k) {
                var v = attrs[k];
                if (v == null) return;
                if (k === 'class') node.className = v;
                else node.setAttribute(k, v);
            });
        }
        if (children) {
            (Array.isArray(children) ? children : [children]).forEach(function (c) {
                if (c == null) return;
                if (typeof c === 'string') node.appendChild(document.createTextNode(c));
                else node.appendChild(c);
            });
        }
        return node;
    }

    function link(href, text) { return el('a', { href: href }, text); }

    function toggleRow(prefKey, title, desc, ariaLabel) {
        return el('div', { 'class': 'consent-row' }, [
            el('div', { 'class': 'consent-row__text' }, [
                el('div', { 'class': 'consent-row__title' }, title),
                el('div', { 'class': 'consent-row__desc' }, desc)
            ]),
            el('label', { 'class': 'consent-toggle' }, [
                el('input', { type: 'checkbox', 'data-pref': prefKey }),
                el('span', { 'class': 'consent-toggle__track', 'aria-hidden': 'true' }, [
                    el('span', { 'class': 'consent-toggle__knob' })
                ]),
                el('span', { 'class': 'visually-hidden' }, ariaLabel)
            ])
        ]);
    }

    // ---------- Banner construction ----------
    function buildBanner() {
        var wrap = el('div', {
            'class': 'consent-banner',
            'role': 'dialog',
            'aria-modal': 'false',
            'aria-labelledby': 'consent-title',
            'aria-describedby': 'consent-body'
        });

        // === Main view ===
        var mainView = el('div', { 'class': 'consent-banner__inner', 'data-view': 'main' }, [
            el('div', { 'class': 'consent-banner__head' }, [
                el('span', { 'class': 'consent-banner__icon material-symbols-outlined', 'aria-hidden': 'true' }, 'cookie'),
                el('h2', { id: 'consent-title', 'class': 'consent-banner__title' }, 'Cookies, briefly.')
            ]),
            el('p', { id: 'consent-body', 'class': 'consent-banner__body' }, [
                'We load one Google Ads tag to measure clicks from our paid campaigns. It’s off by default. Choose what to allow — you can change this any time via ',
                el('strong', null, 'Cookie preferences'),
                ' in the footer.'
            ]),
            el('p', { 'class': 'consent-banner__legal' }, [
                'Read the full ',
                link('privacy-policy.html#p11', 'privacy policy'),
                ' · ',
                link('gdpr.html#g6', 'GDPR disclosure'),
                '.'
            ]),
            el('div', { 'class': 'consent-banner__actions' }, [
                el('button', { type: 'button', 'class': 'consent-btn consent-btn--ghost', 'data-action': 'reject' }, 'Reject all'),
                el('button', { type: 'button', 'class': 'consent-btn consent-btn--ghost', 'data-action': 'customize' }, 'Customize'),
                el('button', { type: 'button', 'class': 'consent-btn consent-btn--primary', 'data-action': 'accept' }, 'Accept all')
            ])
        ]);

        // === Preferences view ===
        var prefsView = el('div', {
            'class': 'consent-banner__inner consent-banner__inner--hidden',
            'data-view': 'prefs'
        }, [
            el('div', { 'class': 'consent-banner__head' }, [
                el('span', { 'class': 'consent-banner__icon material-symbols-outlined', 'aria-hidden': 'true' }, 'tune'),
                el('h2', { 'class': 'consent-banner__title' }, 'Preferences')
            ]),

            el('div', { 'class': 'consent-row' }, [
                el('div', { 'class': 'consent-row__text' }, [
                    el('div', { 'class': 'consent-row__title' }, 'Essential'),
                    el('div', { 'class': 'consent-row__desc' }, 'Required for the site to function (theme, navigation, the consent banner itself). Stored only in your browser. No data sent off-device.')
                ]),
                el('div', { 'class': 'consent-row__status consent-row__status--on' }, 'Always on')
            ]),

            toggleRow(
                'advertising',
                'Advertising measurement',
                'Google Ads conversion tag (AW-17758801825). Sends ad_storage, ad_user_data and ad_personalization signals so we can see which paid ads bring people to the App Store. Cookieless and redacted until you opt in.',
                'Toggle advertising measurement'
            ),

            toggleRow(
                'analytics',
                'Analytics',
                'Reserved for future site analytics (e.g. anonymized page-view counts). Currently unused — no analytics tag is loaded today. Toggling has no effect right now but is recorded for when we add one.',
                'Toggle analytics'
            ),

            el('div', { 'class': 'consent-banner__actions' }, [
                el('button', { type: 'button', 'class': 'consent-btn consent-btn--ghost', 'data-action': 'back' }, 'Back'),
                el('button', { type: 'button', 'class': 'consent-btn consent-btn--primary', 'data-action': 'save' }, 'Save preferences')
            ])
        ]);

        wrap.appendChild(mainView);
        wrap.appendChild(prefsView);
        return wrap;
    }

    // ---------- View management ----------
    var bannerEl = null;
    var lastFocused = null;

    function showView(view) {
        if (!bannerEl) return;
        bannerEl.querySelectorAll('.consent-banner__inner').forEach(function (n) {
            n.classList.toggle('consent-banner__inner--hidden', n.getAttribute('data-view') !== view);
        });
        var focusable = bannerEl.querySelector(
            '[data-view="' + view + '"] button[data-action="accept"], ' +
            '[data-view="' + view + '"] button[data-action="save"]'
        );
        if (focusable) setTimeout(function () { focusable.focus(); }, 30);
    }

    function openBanner() {
        if (bannerEl) {
            bannerEl.classList.add('consent-banner--visible');
            return;
        }
        lastFocused = document.activeElement;
        bannerEl = buildBanner();
        document.body.appendChild(bannerEl);

        requestAnimationFrame(function () {
            bannerEl.classList.add('consent-banner--visible');
        });

        bannerEl.addEventListener('click', function (e) {
            var btn = e.target.closest('[data-action]');
            if (!btn) return;
            var action = btn.getAttribute('data-action');
            if (action === 'reject') finish({ advertising: false, analytics: false });
            else if (action === 'accept') finish({ advertising: true, analytics: true });
            else if (action === 'customize') {
                var stored = readChoice() || { advertising: false, analytics: false };
                var ad = bannerEl.querySelector('[data-pref="advertising"]');
                var an = bannerEl.querySelector('[data-pref="analytics"]');
                if (ad) ad.checked = !!stored.advertising;
                if (an) an.checked = !!stored.analytics;
                showView('prefs');
            }
            else if (action === 'back') showView('main');
            else if (action === 'save') {
                var ad2 = bannerEl.querySelector('[data-pref="advertising"]');
                var an2 = bannerEl.querySelector('[data-pref="analytics"]');
                finish({
                    advertising: !!(ad2 && ad2.checked),
                    analytics:   !!(an2 && an2.checked)
                });
            }
        });

        document.addEventListener('keydown', escHandler);
    }

    function escHandler(e) {
        if (e.key === 'Escape' && bannerEl && bannerEl.classList.contains('consent-banner--visible')) {
            if (!readChoice()) finish({ advertising: false, analytics: false });
            else closeBanner();
        }
    }

    function finish(choice) {
        saveChoice(choice);
        applyChoice(choice);
        closeBanner();
    }

    function closeBanner() {
        if (!bannerEl) return;
        bannerEl.classList.remove('consent-banner--visible');
        document.removeEventListener('keydown', escHandler);
        setTimeout(function () {
            if (bannerEl && bannerEl.parentNode) bannerEl.parentNode.removeChild(bannerEl);
            bannerEl = null;
            if (lastFocused && lastFocused.focus) lastFocused.focus();
        }, 280);
    }

    // ---------- Public reopen hook ----------
    window.sageConsentOpen = function () {
        openBanner();
        showView('main');
    };

    // ---------- Init ----------
    function init() {
        var stored = readChoice();
        if (stored) {
            applyChoice(stored);
        } else {
            openBanner();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
