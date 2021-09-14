const records = JSON.parse(document.getElementById('records').textContent);

const table_element = document.getElementById('table');
const table_body = table_element.getElementsByTagName('tbody')[0];
function render_html(map, field) {
	for (const [grouped_field, list] of map) {
		list.forEach((record, i) => {
			let string = '';
			for (const key in record) {
				if (Object.prototype.hasOwnProperty.call(record, key))
					if (key === 'link')
						string += `<td><a href="${record[key]}">Link</a> </td>`;
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
		delete item[field];
		if (!collection) {
			map.set(key, [item]);
		} else {
			collection.push(item);
		}
	});
	return map;
}
const grouped = groupby(records, 'day');
render_html(grouped, 'day');
// TODO: Add sorting/ filtering
