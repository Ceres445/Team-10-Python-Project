import addPostToHTML from'./modules/functions.js';const tabcontent=document.querySelector('.tabcontent');const tablinks=document.getElementsByClassName('tablink');const courses=JSON.parse(document.getElementById('courses').textContent);const post_form=document.getElementById('post-form');const title=document.getElementById('title-input');const content=document.getElementById('content-input');const url=`${window.location.origin}/api/`;let active='Public';async function changeUI(name,category=false){if(name==='all'){return await changeUI('Class',true);}
const data=await fetch(category?`${url}posts?category=${name}`:`${url}posts?category=Class&class=${name}`);console.log(data);const json=await data.json();console.log(json);tabcontent.innerHTML='';json.forEach(el=>addPostToHTML(el,tabcontent));const new_active=category?name:active;if(new_active==='Class'&&active!=='Class'&&courses){tabcontent.insertAdjacentHTML('beforebegin',`<div class="selector" id="class-selection"><label>Choose a class:</label>
									<select name="class-selection-select">
									<option value="all"> all </option>
										${courses.map(el => `<option value="${el}">${el}</option>`).join('\n')}
									</select>
				</div>`);document.getElementById('class-selection').addEventListener('change',el=>changeUI(el.target.value));}
active=new_active;}
for(const i of tablinks){i.addEventListener('click',async function(){await changeUI(this.name,true);});}
document.getElementById('defaultOpen').click();async function get_category(){const categoryData=await fetch(`${url}categories`);const json=await categoryData.json();console.log(json);}
post_form.addEventListener('submit',async function(e){const data={title:title.innerText,content:content.innerText,category:await get_category(),};await fetch(`${url}posts`,{method:'POST',headers:{'Content-Type':'application/json',},body:JSON.stringify(data),});});;