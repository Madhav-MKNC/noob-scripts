(() => {
	const VERSION = "v1";
	let id = location.href.match(/\?list=([a-zA-Z0-9-_]+)($|&)/)[1];
	let title = document.getElementById('text-displayed').innerText;
	let created_at = Date.now();
	let videos = [];
	document.querySelectorAll('ytd-playlist-video-renderer').forEach(e => {
		videos.push({
			title: e.querySelector('#video-title').innerText,
			id: e.querySelector('a').href.match(/\?v=([a-zA-Z0-9-_]+)($|&)/)[1],
			channel: e.querySelector('#channel-name').innerText
		});
	});
	let data = {
		version: VERSION,
		title: title,
		id: id,
		created_at: created_at,
		videos: videos
	};
	let a = document.createElement('a');
	a.href = URL.createObjectURL(new Blob([JSON.stringify(data)], {type: 'text/plain'}));
	a.download = 'playlist_' + id + '.json';
	a.click();
})();