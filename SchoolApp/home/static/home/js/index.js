import addPostToHTML from './utils/functions';

const tabcontent = document.querySelector('.tabcontent');
const tablinks = document.getElementsByClassName('tablink');

for (const i of tablinks) {
	i.addEventListener('click', async function () {
		const data = await fetch(
			window.location.href + `api/posts?category=${this.name}`
		);
		const json = await data.json();
		tabcontent.innerHTML = '';
		json.forEach(el => addPostToHTML(el, tabcontent));
	});
}
document.getElementById('defaultOpen').click();

// TODO: implement posting posts and timer for posting
// TODO: Add filter by class for Class category
