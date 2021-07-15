function addPostToHTML(el, container) {
	const html = `<div class='post'>
													<h1>${el.title}</h1>
													<p>${el.content}</p>
													<div class = 'footer'>${el.author}</div>
											</div>`;
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

export { addPostToHTML, getCookie };
