import { addPostToHTML, getCookie } from './modules/functions.js';
import { URL } from './modules/constants.js';

const tabContent = document.querySelector('.tabcontent');
const tabLinks = document.getElementsByClassName('tablink');
const courses = document.getElementById('courses')?.textContent
	? JSON.parse(document.getElementById('courses')?.textContent)
	: null;
const postForm = document.getElementById('post-form');
const selectorDiv = document.getElementById('selector-div');
const inputTitle = document.getElementById('title-input');
const inputContent = document.getElementById('content-input');

const submitBtn = document.getElementById('submit-btn');
const FormHeading = document.getElementById('submit-form-heading');

let buttonHidden = false;
const url = URL + '/api/';

function hideButton(hide = true) {
	if (!courses) {
		submitBtn.disabled = true;
		FormHeading.innerText = `Can't submit posts here`;
		buttonHidden = true;
		return false;
	}
	if (buttonHidden === hide) return;
	if (hide) {
		submitBtn.disabled = true;
		FormHeading.innerText = `Can't submit posts here`;
	} else {
		submitBtn.disabled = false;
	}
	buttonHidden = !buttonHidden;
}

const active = {
	_value: 'Public',
	set value(field) {
		this._value = field;
		for (const el of tabLinks) el.classList.remove('active');
		document.getElementsByName(field)[0].classList.add('active');
		if (field === 'Class') {
			if (!courses || courses.length === 0) hideButton();
			else if (
				document.getElementById('class-selection-select').value ===
				'all'
			) {
				hideButton();
			} else {
				FormHeading.innerText = `Posting to Class ${
					document.getElementById('class-selection-select').value
				}`;
				hideButton(false);
			}
		} else if (field in { Site: 0, Public: 0 }) {
			hideButton(true);
		} else {
			FormHeading.innerText = `Posting to ${field}`;
			hideButton(false);
		}
	},
	get value() {
		return this._value;
	},
};

async function changeUI(name, category = false) {
	if (name === 'all') {
		return await changeUI('Class', true);
	}
	const data = await fetch(
		category
			? `${url}posts?category=${name}`
			: `${url}posts?category=Class&class=${name}`
	);
	if (Math.floor(data.status / 100) !== 2) tabContent.innerHTML = 'No Posts';
	else {
		const json = await data.json();
		tabContent.innerHTML = '';
		json.forEach(el => addPostToHTML(el, tabContent));
	}
	const new_active = category ? name : active.value;
	if (new_active === 'Class' && active.value !== 'Class' && courses) {
		if (courses.length === 0)
			tabContent.innerHTML = 'Join a class to view class posts';
		else {
			selectorDiv.insertAdjacentHTML(
				'afterbegin',
				`<div class="selector" id="class-selection"><label>Choose a class:</label>
											<select id="class-selection-select">
											<option value="all"> all </option>
												${courses.map(el => `<option value="${el}"> ${el} </option>`).join('\n')}
											</select>
						</div>`
			);
			document
				.getElementById('class-selection')
				.addEventListener('change', el => changeUI(el.target.value));
		}
	}
	if (new_active !== 'Class') selectorDiv.innerText = '';
	active.value = new_active;
}

async function getCategory() {
	let get_url = `${url}categories?name=${active.value}`;
	if (active.value === 'Class') {
		if (document.getElementById('class-selection-select').value !== 'all') {
			get_url = `${url}categories?name=Class&class=${
				document.getElementById('class-selection-select').value
			}`;
		} else {
			return 'all';
		}
	}
	const categoryData = await fetch(get_url);
	// active !== 'Class'
	// 	? `${url}categories?name=${active}`
	// 	: document.getElementById('class-selection-select').value !== 'all'
	// 	? `${url}categories?name=Class&class=${
	// 			document.getElementById('class-selection-select').value
	// 	  }`
	// 	: `${url}categories?name=Class`

	const json = await categoryData.json();
	return json[0].id;
}

// Promise.all(get_category()).then(r => r + 1);

// add event listener to post form so we can get input and submit with extra variables
postForm.addEventListener('submit', async function (e) {
	e.preventDefault();
	// Format data to submit to api
	const data = {
		title: inputTitle.value,
		content: inputContent.value,
		category: await getCategory(),
	};
	// Make post request to api make a post
	const fetchResults = await fetch(`${url}posts/`, {
		method: 'POST',
		headers: {
			'X-CSRFToken': getCookie('csrftoken'),
			Accept: 'application/json',
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	});
	// Update html
	const oldHtml = postForm.innerHTML;
	inputTitle.value = '';
	inputContent.value = '';
	document.getElementsByName(active.value)[0].click(); // Switch tab to active
	if (String(fetchResults.status)[0] === '2') postForm.innerText = 'Success';
	else postForm.innerText = 'Failure';
	setTimeout(() => (postForm.innerHTML = oldHtml), 5000);
});
// Add event listeners to categories
for (const i of tabLinks) {
	i.addEventListener('click', async function () {
		await changeUI(this.name, true);
	});
}

// Open default category
document.getElementById('defaultOpen').click();
