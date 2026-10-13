(() => {
  'use strict';

  try {
    const current = new URL(window.location.href);

    // Do nothing on normal page loads. This marker is only added by a
    // deliberate LinkRouter rule that launches a PWA on an in-scope URL.
    if (current.searchParams.get('__lr_pwa_handoff') !== '1') return;

    // LinkRouter puts the original destination after the first # so the
    // destination's own query string does not corrupt the bridge URL.
    const rawTarget = current.hash.slice(1);
    if (!rawTarget) return;

    const target = new URL(rawTarget);
    if (target.protocol !== 'https:' && target.protocol !== 'http:') return;
    if (target.username || target.password) return;
    if (target.href === current.href) return;

    // Replace the bridge page in this web contents with the requested URL.
    window.location.replace(target.href);
  } catch (_) {
    // Ignore normal visits or malformed handoff URLs.
  }
})();
