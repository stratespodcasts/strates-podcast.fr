---
title: "STRATES"
featured_image: ""
description: "Les Ecoutes de la Profondeur"
---

<p class="home-intro">Des podcasts. Une exigence. Tout explorer, ne rien figer.</p>

<div class="strates-player">
<p class="strates-player-title">Ecouter le label</p>
<div class="sp-player" id="strates-player">
<div class="sp-current">
<button class="sp-play-btn" id="sp-play" onclick="spToggle()">
<svg class="sp-play-icon" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
<svg class="sp-pause-icon" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
</button>
<img class="sp-cover" id="sp-cover" src="/images/goodmorning.png" alt="">
<div class="sp-info">
<div class="sp-show-name" id="sp-show">Chargement...</div>
<div class="sp-ep-title" id="sp-title">Chargement des episodes</div>
<div class="sp-duration" id="sp-dur"></div>
</div>
</div>
<div class="sp-waveform" onclick="spSeek(event)">
<div class="sp-progress" id="sp-prog"></div>
</div>
<div class="sp-time-row">
<span id="sp-cur">0:00</span>
<span id="sp-tot">0:00</span>
</div>
<div class="sp-list" id="sp-list">
<div class="sp-loading">Chargement des emissions...</div>
</div>

<div class="sp-subscribe-bar">
<button class="sp-subscribe-btn" onclick="spToggleSubscribe(event)">
<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" style="margin-right:6px;vertical-align:middle"><path d="M12 1a9 9 0 0 1 9 9c0 4.97-7.22 12.08-8.55 13.28a.65.65 0 0 1-.9 0C10.22 22.08 3 14.97 3 10a9 9 0 0 1 9-9zm0 6a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"/></svg>
S'abonner au label
</button>

<div class="sp-subscribe-panel" id="sp-subscribe-panel">
<p class="sp-subscribe-title">S'abonner au flux STRATES</p>
<a class="sp-subscribe-app" href="pcast://strates-podcast.fr/feed.xml" target="_blank">
<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/></svg>
Podcast Addict
</a>
<a class="sp-subscribe-app" href="https://podcasts.apple.com/podcast/id?feedUrl=https%3A%2F%2Fstrates-podcast.fr%2Ffeed.xml" target="_blank">
<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
Apple Podcasts
</a>
<button class="sp-subscribe-app sp-copy-btn" onclick="spCopyFeed()">
<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
<span id="sp-copy-label">Copier l'URL du flux</span>
</button>
</div>
</div>

</div>
</div>

{{ partial "newsletter-form.html" . }}
<p class="podcasts-section-title">Nos emissions</p>

<div class="podcasts-grid">
<a href="/podcasts/good-morning-la-galaxie/" class="podcast-card">
<img src="/images/goodmorning.png" alt="Good Morning la Galaxie">
<div class="podcast-card-body">
<p class="podcast-card-title">Good Morning la Galaxie</p>
<p class="podcast-card-desc">6 bonnes actus de la semaine et des decouvertes musicales Bandcamp.</p>
<span class="podcast-card-status status-live">En ligne</span>
</div>
</a>
<a href="/podcasts/candide-en-vers/" class="podcast-card">
<img src="/images/candide.png" alt="Candide en Vers">
<div class="podcast-card-body">
<p class="podcast-card-title">Candide en Vers</p>
<p class="podcast-card-desc">La poesie francaise expliquee aux curieux. Un theme, des voix, une emotion.</p>
<span class="podcast-card-status status-live">En ligne</span>
</div>
</a>
<a href="/podcasts/le-temoin/" class="podcast-card">
<img src="/images/letemoin.png" alt="Le Temoin">
<div class="podcast-card-body">
<p class="podcast-card-title">Le Temoin</p>
<p class="podcast-card-desc">Des monologues de temoins inattendus de moments pop culture.</p>
<span class="podcast-card-status status-soon">Juillet 2026</span>
</div>
</a>
<a href="/podcasts/juste-avant/" class="podcast-card">
<img src="/images/justavant.png" alt="Juste Avant">
<div class="podcast-card-body">
<p class="podcast-card-title">Juste Avant</p>
<p class="podcast-card-desc">Fiction anthologique horreur et SF. La Voix de Controle. Neuf episodes.</p>
<span class="podcast-card-status status-tbd">Janvier 2027</span>
</div>
</a>
<a href="/podcasts/dispatch/" class="podcast-card">
<img src="/images/dispatch.png" alt="Dispatch">
<div class="podcast-card-body">
<p class="podcast-card-title">Dispatch</p>
<p class="podcast-card-desc">Un pere et sa fille. Une agence qui n existe pas. Des missions qui changent tout.</p>
<span class="podcast-card-status status-tbd">Bientot</span>
</div>
</a>
</div>

<style>
.sp-subscribe-bar {
  position: relative;
  padding: 10px 16px 12px;
  border-top: 1px solid rgba(177,115,55,0.2);
  text-align: center;
}
.sp-subscribe-btn {
  background: none;
  border: 1px solid rgba(177,115,55,0.5);
  color: #C4934A;
  font-family: 'Cinzel', serif;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 7px 18px;
  border-radius: 2px;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s;
}
.sp-subscribe-btn:hover {
  border-color: #C4934A;
  color: #D4A460;
}
.sp-subscribe-panel {
  display: none;
  position: absolute;
  bottom: calc(100% + 6px);
  left: 50%;
  transform: translateX(-50%);
  background: #1e1e1e;
  border: 1px solid rgba(177,115,55,0.3);
  border-radius: 4px;
  padding: 14px 16px;
  min-width: 240px;
  z-index: 100;
  box-shadow: 0 4px 20px rgba(0,0,0,0.6);
}
.sp-subscribe-panel.open {
  display: block;
}
.sp-subscribe-title {
  font-family: 'Cinzel', serif;
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #C4934A;
  margin: 0 0 12px;
}
.sp-subscribe-app {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  padding: 8px 10px;
  margin-bottom: 6px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 3px;
  color: #F5F0E5;
  font-family: 'Cormorant Garamond', serif;
  font-size: 0.95rem;
  text-decoration: none;
  cursor: pointer;
  transition: background 0.15s, border-color 0.15s;
  box-sizing: border-box;
}
.sp-subscribe-app:hover {
  background: rgba(177,115,55,0.12);
  border-color: rgba(177,115,55,0.4);
  color: #F5F0E5;
}
.sp-subscribe-app:last-child {
  margin-bottom: 0;
}
.sp-copy-btn {
  background: rgba(255,255,255,0.04) !important;
}
</style>

<script>
var spAudio = new Audio();
var spEpisodes = [];
var spCurrent = 0;

function spFmt(s) {
  s = Math.floor(s);
  var m = Math.floor(s/60);
  var sec = s%60;
  return m+':'+(sec<10?'0':'')+sec;
}

function spLoad(idx) {
  var ep = spEpisodes[idx];
  spCurrent = idx;
  document.getElementById('sp-title').textContent = ep.title;
  document.getElementById('sp-show').textContent = ep.show;
  var coverEl = document.getElementById('sp-cover');
  coverEl.src = ep.cover;
  coverEl.onerror = function() {
    this.src = ep.cover_fallback || '/images/goodmorning.png';
  };
  document.getElementById('sp-dur').textContent = ep.duration;
  spAudio.src = ep.url;
  document.querySelectorAll('.sp-episode').forEach(function(el, i) {
    el.classList.toggle('active', i === idx);
  });
}

function spToggle() {
  if (spAudio.paused) {
    spAudio.play();
    document.getElementById('strates-player').classList.add('sp-playing');
  } else {
    spAudio.pause();
    document.getElementById('strates-player').classList.remove('sp-playing');
  }
}

function spSeek(e) {
  var bar = e.currentTarget;
  var ratio = e.offsetX / bar.offsetWidth;
  spAudio.currentTime = ratio * spAudio.duration;
}

function spToggleSubscribe(e) {
  e.stopPropagation();
  var panel = document.getElementById('sp-subscribe-panel');
  panel.classList.toggle('open');
}

function spCopyFeed() {
  var url = 'https://strates-podcast.fr/feed.xml';
  navigator.clipboard.writeText(url).then(function() {
    var label = document.getElementById('sp-copy-label');
    label.textContent = 'Copie !';
    setTimeout(function() { label.textContent = "Copier l'URL du flux"; }, 2000);
  });
}

document.addEventListener('click', function(e) {
  var panel = document.getElementById('sp-subscribe-panel');
  if (panel && panel.classList.contains('open')) {
    if (!panel.contains(e.target) && !e.target.closest('.sp-subscribe-btn')) {
      panel.classList.remove('open');
    }
  }
});

spAudio.addEventListener('timeupdate', function() {
  if (spAudio.duration) {
    var pct = (spAudio.currentTime / spAudio.duration) * 100;
    document.getElementById('sp-prog').style.width = pct+'%';
    document.getElementById('sp-cur').textContent = spFmt(spAudio.currentTime);
    document.getElementById('sp-tot').textContent = spFmt(spAudio.duration);
  }
});

spAudio.addEventListener('ended', function() {
  document.getElementById('strates-player').classList.remove('sp-playing');
  if (spCurrent < spEpisodes.length - 1) {
    spLoad(spCurrent + 1);
    spAudio.play();
    document.getElementById('strates-player').classList.add('sp-playing');
  }
});

async function spFetch() {
  var slot = document.getElementById('hero-player-slot');
  var player = document.getElementById('strates-player').parentElement;
  if (slot && player) slot.appendChild(player);

  var list = document.getElementById('sp-list');
  try {
    var resp = await fetch('/episodes.json');
    var eps = await resp.json();
    spEpisodes = eps;
    if (eps.length === 0) {
      list.innerHTML = '<div class="sp-loading">Aucun episode disponible</div>';
      return;
    }
    list.innerHTML = '';
    eps.forEach(function(ep, i) {
      var div = document.createElement('div');
      div.className = 'sp-episode' + (i===0?' active':'');
      var img = new Image();
      img.className = 'sp-ep-cover';
      img.alt = '';
      img.src = ep.cover;
      img.onerror = function() { this.src = ep.cover_fallback || '/images/goodmorning.png'; };
      var info = document.createElement('div');
      info.className = 'sp-ep-info';
      info.innerHTML =
        '<div class="sp-ep-show">'+ep.show+'</div>' +
        '<div class="sp-ep-name">'+ep.title+'</div>';
      var dur = document.createElement('div');
      dur.className = 'sp-ep-dur';
      dur.textContent = ep.duration;
      div.appendChild(img);
      div.appendChild(info);
      div.appendChild(dur);
      div.onclick = function() {
        spLoad(i);
        spAudio.play();
        document.getElementById('strates-player').classList.add('sp-playing');
      };
      list.appendChild(div);
    });
    spLoad(0);
  } catch(e) {
    list.innerHTML = '<div class="sp-loading">Erreur de chargement</div>';
    console.error(e);
  }
}
spFetch();
</script>
