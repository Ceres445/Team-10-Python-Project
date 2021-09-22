import { URL } from './modules/constants.js';

Array.from(document.getElementsByTagName('tr')).forEach(el =>
	el.addEventListener('click', () => {
		window.location.href = `${URL}/classes/${el.id}`;
	})
);
