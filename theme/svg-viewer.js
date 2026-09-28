(() => {
    const content = document.querySelector('main');
    if (!content || !window.HTMLDialogElement) return;

    const dialog = document.createElement('dialog');
    dialog.className = 'svg-viewer';
    dialog.setAttribute('aria-label', '图表预览');
    dialog.innerHTML = `
        <div class="svg-viewer-toolbar">
            <span class="svg-viewer-title">图表预览</span>
            <button type="button" data-action="out" aria-label="缩小">−</button>
            <output aria-live="polite" aria-label="缩放比例"></output>
            <button type="button" data-action="in" aria-label="放大">＋</button>
            <button type="button" data-action="fit">适应窗口</button>
            <button type="button" data-action="close" autofocus>关闭</button>
        </div>
        <div class="svg-viewer-stage" tabindex="0" aria-label="图表画布：滚轮缩放，拖动平移，按加减键缩放，按 0 适应窗口">
            <div class="svg-viewer-artwork" inert></div>
        </div>
        <p class="svg-viewer-help">滚轮或 ＋ / − 缩放 · 拖动平移 · 0 适应窗口 · Esc 关闭</p>`;
    document.body.append(dialog);

    const stage = dialog.querySelector('.svg-viewer-stage');
    const artwork = dialog.querySelector('.svg-viewer-artwork');
    const output = dialog.querySelector('output');
    let active = null;
    let placeholder = null;
    let previousFocus = null;
    let width = 1;
    let height = 1;
    let scale = 1;
    let minimum = 0.1;
    let x = 0;
    let y = 0;
    let drag = null;

    function render() {
        artwork.style.transform = `translate(${x}px, ${y}px) scale(${scale})`;
        output.value = `${Math.round(scale * 100)}%`;
    }

    function fit() {
        if (!dialog.open) return;
        scale = Math.min((stage.clientWidth - 32) / width, (stage.clientHeight - 32) / height, 1);
        scale = Math.max(scale, 0.001);
        minimum = Math.min(0.1, scale);
        x = (stage.clientWidth - width * scale) / 2;
        y = (stage.clientHeight - height * scale) / 2;
        render();
    }

    function zoom(factor, px = stage.clientWidth / 2, py = stage.clientHeight / 2) {
        const next = Math.max(minimum, Math.min(8, scale * factor));
        x = px - (px - x) * next / scale;
        y = py - (py - y) * next / scale;
        scale = next;
        render();
    }

    function open(source) {
        if (active) return;
        const bounds = source.getBoundingClientRect();
        const viewBox = source.viewBox?.baseVal;
        width = viewBox?.width || source.naturalWidth || bounds.width;
        height = viewBox?.height || source.naturalHeight || bounds.height;
        if (width <= 0 || height <= 0) return;

        previousFocus = source;
        active = source;
        // Move the original SVG to preserve Mermaid styles, markers and unique IDs.
        // A sized placeholder keeps the document and its scroll position stable.
        placeholder = document.createElement('span');
        placeholder.style.cssText = `display:inline-block;width:${bounds.width}px;height:${bounds.height}px`;
        placeholder.setAttribute('aria-hidden', 'true');
        const style = getComputedStyle(source);
        artwork.style.fontFamily = style.fontFamily;
        artwork.style.fontSize = style.fontSize;
        artwork.style.width = `${width}px`;
        artwork.style.height = `${height}px`;
        source.replaceWith(placeholder);
        artwork.append(source);
        dialog.showModal();
        document.documentElement.classList.add('svg-viewer-open');
        fit();
    }

    dialog.addEventListener('close', () => {
        placeholder?.replaceWith(active);
        active = null;
        placeholder = null;
        drag = null;
        stage.classList.remove('is-dragging');
        document.documentElement.classList.remove('svg-viewer-open');
        previousFocus?.focus({ preventScroll: true });
    });

    dialog.addEventListener('click', event => {
        const action = event.target.closest('button')?.dataset.action;
        if (action === 'in') zoom(1.25);
        if (action === 'out') zoom(1 / 1.25);
        if (action === 'fit') fit();
        if (action === 'close') dialog.close();
        if (event.target === dialog) {
            const bounds = dialog.getBoundingClientRect();
            if (event.clientX < bounds.left || event.clientX > bounds.right ||
                event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
        }
    });

    dialog.addEventListener('keydown', event => {
        // Keep mdBook shortcuts from changing chapters behind the modal.
        event.stopPropagation();
        if (event.key === '+' || event.key === '=') { event.preventDefault(); zoom(1.25); }
        if (event.key === '-') { event.preventDefault(); zoom(1 / 1.25); }
        if (event.key === '0') { event.preventDefault(); fit(); }
    });

    stage.addEventListener('wheel', event => {
        event.preventDefault();
        const bounds = stage.getBoundingClientRect();
        const delta = event.deltaY * (event.deltaMode === 1 ? 16 : event.deltaMode === 2 ? stage.clientHeight : 1);
        zoom(Math.exp(-Math.max(-200, Math.min(200, delta)) * 0.002),
            event.clientX - bounds.left, event.clientY - bounds.top);
    }, { passive: false });

    stage.addEventListener('pointerdown', event => {
        if (event.button !== 0 || !event.isPrimary) return;
        stage.focus({ preventScroll: true });
        drag = { id: event.pointerId, x: event.clientX, y: event.clientY };
        stage.setPointerCapture(event.pointerId);
        stage.classList.add('is-dragging');
    });
    stage.addEventListener('pointermove', event => {
        if (!drag || drag.id !== event.pointerId) return;
        x += event.clientX - drag.x;
        y += event.clientY - drag.y;
        drag.x = event.clientX;
        drag.y = event.clientY;
        render();
    });
    for (const type of ['pointerup', 'pointercancel', 'lostpointercapture']) {
        stage.addEventListener(type, event => {
            if (drag?.id !== event.pointerId) return;
            drag = null;
            stage.classList.remove('is-dragging');
            if (stage.hasPointerCapture(event.pointerId)) stage.releasePointerCapture(event.pointerId);
        });
    }
    window.addEventListener('resize', fit);

    function enhance() {
        for (const source of content.querySelectorAll('svg, img')) {
            if (source.closest('a, button') || source.classList.contains('svg-zoomable')) continue;
            if (source instanceof HTMLImageElement &&
                !/\.svg(?:[?#]|$)|^data:image\/svg\+xml/i.test(source.currentSrc || source.src)) continue;
            source.classList.add('svg-zoomable');
            source.setAttribute('tabindex', '0');
            source.setAttribute('role', 'button');
            const label = source.getAttribute('aria-label') || source.getAttribute('alt') ||
                source.querySelector('title')?.textContent || '图表';
            source.setAttribute('aria-label', `${label}，点击放大查看`);
            source.setAttribute('aria-haspopup', 'dialog');
        }
    }
    content.addEventListener('click', event => {
        if (event.target.closest('a, button')) return;
        const source = event.target.closest('.svg-zoomable');
        if (source) open(source);
    });
    content.addEventListener('keydown', event => {
        if ((event.key === 'Enter' || event.key === ' ') && event.target.matches('.svg-zoomable')) {
            event.preventDefault();
            event.stopPropagation();
            open(event.target);
        }
    });
    // Mermaid inserts SVGs asynchronously after the page has loaded.
    new MutationObserver(enhance).observe(content, { childList: true, subtree: true });
    enhance();
})();
