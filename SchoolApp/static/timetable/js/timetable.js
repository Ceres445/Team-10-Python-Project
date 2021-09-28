const records = JSON.parse(document.getElementById('records').textContent);

const table_element = document.getElementById('table');
const table_body = table_element.getElementsByTagName('tbody')[0];
const table_head = table_element.getElementsByTagName('thead')[0];
const order = {
	day: ['day', 'subject', 'time', 'link'],
	subject: ['subject', 'day', 'time', 'link'],
};

function render_html(map, field) {
	table_head.innerHTML = '';
	table_head.insertRow(0).innerHTML = `<td>
${order[field].map(capitalize).join('</td><td>')}</td>`;
	table_body.innerHTML = '';
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

function groupby(list, field) {
	const map = new Map();
	list.forEach(item => {
		const key = item[field];
		const collection = map.get(key);
		const { [field]: _, ...test } = item;
		if (!collection) {
			map.set(key, [test]);
		} else {
			collection.push(test);
		}
	});
	return map;
}

const grouped = groupby(records, 'day');
render_html(grouped, 'day');

Array.from(document.getElementsByClassName('groupby')).forEach(el =>
	el.addEventListener('click', () => {
		render_html(groupby(records, el.name), el.name);
	})
);

// TODO: Add sorting/ filtering

function capitalize(s) {
	return s[0].toUpperCase() + s.slice(1);
}
