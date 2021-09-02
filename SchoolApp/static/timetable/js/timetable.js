const records = JSON.parse(document.getElementById('records').textContent);

const table = document.getElementById('table');
for (const record of records) {
	table.insertAdjacentHTML(
		'beforeend',
		`<tr>
        <td>${record.day}</td>
        <td>${record.subject}</td>
        <td>${record.time}</td>
        <td><a href="${record.link}">Link</a></td>
    </tr>
  `
	);
}
// TODO: Add sorting/ filtering
