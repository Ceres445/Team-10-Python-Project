import { escapeHtml } from '../../home/js/modules/functions.js';

const records = JSON.parse(document.getElementById('records').textContent);

const table_element = document.getElementById('table');
const table_body = table_element.getElementsByTagName('tbody')[0];
const table_head = table_element.getElementsByTagName('thead')[0];
const filterby_checklist = document.querySelector('.filterby-checklists');
const filterby_support = document.querySelector('.filterby-support');

const order = {
	day: ['day', 'subject', 'time', 'link'],
	subject: ['subject', 'day', 'time', 'link'],
};
let _groupby = 'day'; // Default filter and group by day
let _filterby = 'day';
function render_html() {
	const map = groupby(filterby(records)); // get the filtered and grouped map
	table_head.innerHTML = ''; // Rewrite the table headers
	table_head.insertRow(0).innerHTML = `<td>
${order[_groupby].map(capitalize).join('</td><td>')}</td>`;
	table_body.innerHTML = ''; // Rewrite the table body with the map
	for (const [grouped_field, list] of map) {
		list.forEach((record, i) => {
			let string = '';
			for (const key of order['day']) {
				if (Object.prototype.hasOwnProperty.call(record, key))
					if (key === 'link')
						string += `<td><a href="${record[key]}" target="_blank">Link</a> </td>`;
					else string += `<td>${record[key]}</td>`;
			}
			const row = table_body.insertRow();
			if (i === 0) {
				row.innerHTML = `
               <td rowspan="${list.length}" class="span">${grouped_field}</td>
							${string}
				`;
			} else row.innerHTML = string;
		});
	}
}
function filterby(records) {
	// get filters and filter our records
	const filters = document.getElementsByClassName('filterby');
	if (filters.length !== 0) {
		const checked = [];
		for (const i of filters) {
			if (i.checked) {
				checked.push(i.name);
			}
		}
		return records.filter(el => checked.includes(el[_filterby]));
	} else return records;
}

function groupby(list) {
	// get group field and group our records
	const map = new Map();
	list.forEach(item => {
		const key = item[_groupby];
		const collection = map.get(key);
		const { [_groupby]: _, ...test } = item;
		if (!collection) {
			map.set(key, [test]);
		} else {
			collection.push(test);
		}
	});
	return map;
}

Array.from(document.getElementsByClassName('filterbutton')).forEach(el =>
	el.addEventListener('click', () => {
		_filterby = el.name;
		filterby_checklist.innerHTML = '';
		[...new Set(records.map(el => el[_filterby]))].forEach(el => {
			filterby_checklist.insertAdjacentHTML(
				'beforeend',
				`<label class="checkbox">
									<input type="checkbox" class="filterby load" name="${escapeHtml(
										el
									)}">${escapeHtml(el)}
								</label>`
			);
		});
		mount_handler();
		filterby_support.classList.remove('hide');
	})
);
// event listeners for groupby buttons
Array.from(document.getElementsByClassName('groupby')).forEach(el =>
	el.addEventListener('click', () => {
		_groupby = el.name;
	})
);

// Event listeners for filterby buttons that give the menus
Array.from(document.getElementsByClassName('filterby-support-button')).forEach(
	el =>
		el.addEventListener('click', () => {
			switch (el.name) {
				case 'all':
					document
						.querySelectorAll('.filterby')
						.forEach(el => (el.checked = true));
					render_html();
					break;
				case 'clear':
					document
						.querySelectorAll('.filterby')
						.forEach(el => (el.checked = false));
					render_html();
					break;
				case 'remove':
					document
						.querySelectorAll('.filterby')
						.forEach(el => (el.checked = false));
					filterby_support.classList.add('hide');
					filterby_checklist.innerHTML = '';
					render_html();
					break;
			}
		})
);

// mount render_html onto all buttons and inputs
function mount_handler() {
	document.querySelectorAll('.load').forEach(el => {
		if (el.hasAttribute('listener')) {
			return;
		}
		switch (el.tagName) {
			case 'INPUT':
				el.setAttribute('listener', 'true');
				el.addEventListener('change', () => render_html());
				break;
			case 'BUTTON':
				el.setAttribute('listener', 'true');
				el.addEventListener('click', () => render_html());
		}
	});
}
// TODO: Add sorting

function capitalize(s) {
	return s[0].toUpperCase() + s.slice(1);
}

render_html(); // load html in the begin
