import { URL } from './modules/constants.js';
import { getCookie } from './modules/functions.js';

const post_pk = JSON.parse(document.getElementById('post_pk').textContent);
let comment_length = JSON.parse(
	document.getElementById('comment_length').textContent
);

const comment_new = document.getElementById('comment-new');
const comments_container =
	document.getElementsByClassName('comments-container')[0];
const comment_head = document.getElementById('comment-head');
const url = URL + '/api/comments/';
// const post_title = document.querySelector('.post-title');
// const post_content = document.querySelector('.post-content');
// const comments_container = document.querySelector('.comments-container');
// // const post_loader = document.querySelector('#post-loader');  // TODO: make loader
// (async function () {
// 	const postData = await fetch(
// 		window.location.origin + `/api/posts/${post_pk}`
// 	);
// 	const postJson = await postData.json();
// 	post_title.innerHTML = postJson.title;
// 	post_content.innerHTML = postJson.content;
// 	const commentsData = await fetch(
// 		window.location.origin + `/api/comments?post=${post_pk}`
// 	);
// 	const commentsJson = await commentsData.json();
// 	commentsJson.sort((a, b) => a.created_at < b.created_at);
// 	comments_container.innerHTML = ``;
// 	for (const comment of commentsJson) {
// 		const html = `<div class="comment-container">
// 	        <p class="'comment-author">${comment.author}</p>
// 	      <p class="comment-body">${comment.body}</p>
// 	      <p class="timestamp">${comment.created_at}</p>`;
// 		comments_container.insertAdjacentHTML('afterbegin', html);
// 	}
// })();

document
	.getElementById('submit-comment')
	.addEventListener('click', async function (e) {
		e.preventDefault();
		const data = {
			body: comment_new.value,
			post: post_pk,
		};
		// Make post request to api make a comment
		const fetchResults = await fetch(url, {
			method: 'POST',
			headers: {
				'X-CSRFToken': getCookie('csrftoken'),
				Accept: 'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		});
		const object = await fetchResults.json();
		// Update html
		comment_new.value = '';
		// if (String(fetchResults.status)[0] === '2')
		// 	submitForm.innerText = 'Success';
		// else submitForm.innerText = 'Failure';
		// setTimeout(() => (submitForm.innerHTML = oldHtml), 5000);
		// TODO: add a success message/ error message
		comment_length++;
		comment_head.innerHTML = `Comments (${comment_length})`;
		const time = new Date(object.created_at);
		comments_container.insertAdjacentHTML(
			'beforeend',
			`<div class="comment-container">
          <p class="comment-header"><a href="${URL}/profile/${object.author}">${
				object.author
			} </a>
      <span class="inactive"> at ${time.toDateString()} ${time.toLocaleTimeString()}</span></p>
      <p class="comment-body">${object.body}</p>
      </div>`
		);
	});
