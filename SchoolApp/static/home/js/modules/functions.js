import { COMMENT, URL } from './constants.js';

function addPostToHTML(el, container) {
	//<div class="post-header">Posted by <a href="/profile/${el.author}">
	// ${el.author}</a></div>

	const html = `<a href="${URL}/posts/${escapeHtml(el.id)}" class="no-hover">
									<div class="post">
									<div class="content">
												<h3 class="post-content">${escapeHtml(el.title)}</h3>
												<p class="post-content post-body" style="color: #afafaf;">${escapeHtml(
													el.content
												)}</p>
									</div>
														
									<div class = "comment-footer"> ${COMMENT} ${
		el.comments?.length ?? 0
	} Comments</div>
								</div></a>`;
	container.insertAdjacentHTML('beforeend', html);
}

function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + '=') {
				cookieValue = decodeURIComponent(
					cookie.substring(name.length + 1)
				);
				break;
			}
		}
	}
	return cookieValue;
}
function escapeHtml(unsafe) {
	return unsafe
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;')
		.replace(/'/g, '&#039;');
}

export { addPostToHTML, getCookie, escapeHtml };
