const tabcontent = document.getElementsByClassName('tabcontent');
const tablinks = document.getElementsByClassName('tablink');
function openPage(pageName, elmnt, color) {
	for (const i of tabcontent) {
		i.style.display = 'none';
	}
	for (const i of tablinks) {
		i.style.backgroundColor = '';
	}
	document.getElementById(pageName).style.display = 'block';
	elmnt.style.backgroundColor = color;
}

// document.getElementsByClassName('tablinks').addEventListener('click', function ())
for (const i of tablinks) {
	i.addEventListener('click', function (e) {
		console.log(e, this.name);
	});
}
document.getElementById('defaultOpen').click();
