(function() {
  var PASS_HASH = '1693c3'; // simple hash of '0223'
  function simpleHash(s) {
    for (var h = 0, i = 0; i < s.length; i++)
      h = ((h << 5) - h + s.charCodeAt(i)) | 0;
    return (h >>> 0).toString(16);
  }
  if (sessionStorage.getItem('domo_auth') === PASS_HASH) return;
  document.body.style.display = 'none';
  var overlay = document.createElement('div');
  overlay.id = 'auth-gate';
  overlay.innerHTML =
    '<div style="position:fixed;inset:0;background:#0a0a0a;z-index:99999;display:flex;align-items:center;justify-content:center;font-family:sans-serif">' +
    '<div style="text-align:center;max-width:360px;padding:24px">' +
    '<div style="font-size:2rem;font-weight:900;margin-bottom:8px;background:linear-gradient(135deg,#A8D00E,#00E647);-webkit-background-clip:text;-webkit-text-fill-color:transparent">DOMO</div>' +
    '<p style="color:#888;margin-bottom:24px;font-size:0.9rem">このページは保護されています。<br>パスワードを入力してください。</p>' +
    '<input id="auth-pw" type="password" placeholder="パスワード" style="width:100%;padding:14px 18px;border-radius:10px;border:1px solid #333;background:#1a1a1a;color:#f0f0f0;font-size:1rem;text-align:center;outline:none" autofocus>' +
    '<p id="auth-err" style="color:#f5576c;font-size:0.8rem;margin-top:10px;display:none">パスワードが違います</p>' +
    '</div></div>';
  document.documentElement.appendChild(overlay);
  var input = document.getElementById('auth-pw');
  input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
      if (simpleHash(input.value) === PASS_HASH) {
        sessionStorage.setItem('domo_auth', PASS_HASH);
        overlay.remove();
        document.body.style.display = '';
      } else {
        document.getElementById('auth-err').style.display = 'block';
        input.value = '';
      }
    }
  });
})();
