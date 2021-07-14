export default function addPostToHTML(el, container) {
	const html = `<div class='post'>
													<h1>${el.title}</h1>
													<p>${el.content}</p>
													<div class = 'footer'>${el.author}</div>
											</div>`;
	container.insertAdjacentHTML('beforeend', html);
}
