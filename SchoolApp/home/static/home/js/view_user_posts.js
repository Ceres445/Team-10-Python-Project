import addPostToHTML from './utils/functions.js';

const user_pk = JSON.parse(document.getElementById('user_pk').textContent);

const container = document.querySelector('.posts');
// const post_loader = document.querySelector('#post-loader');  // TODO: make loader
(async function () {
	const postsData = await fetch(
		window.location.origin + `/api/posts?author=${user_pk}`
	);
	const postsJson = await postsData.json();
	postsJson.forEach(el => addPostToHTML(el, container));
})();
