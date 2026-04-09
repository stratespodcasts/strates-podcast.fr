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
</div>
</div>

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

<script>
var spAudio = new Audio();
var spEpisodes = [];
var spCurrent = 0;
var spFeeds = [
  {url: 'https://feed.ausha.co/BD34s8Q9XL4b', show: 'Good Morning la Galaxie', cover: '/images/goodmorning.png'},
  {url: 'https://feed.ausha.co/owE9IqM4EWgb', show: 'Candide en Vers', cover: '/images/candide.png'}
];

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
  document.getElementById('sp-cover').src = ep.cover;
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

async function spFetchOne(f) {
  var proxies = [
    function(u) { return 'https://api.allorigins.win/raw?url=' + encodeURIComponent(u); },
    function(u) { return 'https://corsproxy.io/?' + encodeURIComponent(u); },
    function(u) { return 'https://api.codetabs.com/v1/proxy?quest=' + encodeURIComponent(u); }
  ];
  for (var i = 0; i < proxies.length; i++) {
    var controller = new AbortController();
    var timeout = setTimeout(function() { controller.abort(); }, 8000);
    try {
      var resp = await fetch(proxies[i](f.url), { signal: controller.signal });
      clearTimeout(timeout);
      if (!resp.ok) continue;
      var text = await resp.text();
      if (!text || !text.includes('<item>')) continue;
      var parser = new DOMParser();
      var xml = parser.parseFromString(text, 'text/xml');
      var items = xml.querySelectorAll('item');
      var eps = [];
      items.forEach(function(item) {
        var enc = item.querySelector('enclosure');
        var dur = item.querySelector('duration');
        var pubDate = item.querySelector('pubDate');
        if (enc) {
          eps.push({
            title: item.querySelector('title').textContent,
            show: f.show,
            url: enc.getAttribute('url'),
            cover: f.cover,
            duration: dur ? dur.textContent : '',
            date: new Date(pubDate ? pubDate.textContent : 0)
          });
        }
      });
      if (eps.length > 0) return eps;
    } catch(e) {
      clearTimeout(timeout);
      console.warn('Proxy ' + i + ' echoue pour ' + f.show + ':', e.message);
    }
  }
  console.warn('Tous les proxies ont echoue pour :', f.show);
  return [];
}

async function spFetch() {
  var slot = document.getElementById('hero-player-slot');
  var player = document.getElementById('strates-player').parentElement;
  if (slot && player) slot.appendChild(player);

  var list = document.getElementById('sp-list');

  var results = await Promise.all(spFeeds.map(spFetchOne));
  var allEps = results.flat();

  allEps.sort(function(a,b) { return b.date - a.date; });
  spEpisodes = allEps;

  if (allEps.length === 0) {
    list.innerHTML = '<div class="sp-loading">Aucun episode disponible</div>';
    return;
  }
  list.innerHTML = '';
  allEps.forEach(function(ep, i) {
    var div = document.createElement('div');
    div.className = 'sp-episode' + (i===0?' active':'');
    div.innerHTML =
      '<img class="sp-ep-cover" src="'+ep.cover+'" alt="">' +
      '<div class="sp-ep-info">' +
        '<div class="sp-ep-show">'+ep.show+'</div>' +
        '<div class="sp-ep-name">'+ep.title+'</div>' +
      '</div>' +
      '<div class="sp-ep-dur">'+ep.duration+'</div>';
    div.onclick = function() {
      spLoad(i);
      spAudio.play();
      document.getElementById('strates-player').classList.add('sp-playing');
    };
    list.appendChild(div);
  });
  spLoad(0);
}
spFetch();
</script>
