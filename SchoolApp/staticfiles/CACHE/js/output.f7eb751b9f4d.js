const post_pk=JSON.parse(document.getElementById('post_pk').textContent);const post_title=document.querySelector('.post-title');const post_content=document.querySelector('.post-content');const comments_container=document.querySelector('.comments-container');(async function(){const postData=await fetch(window.location.origin+`/api/posts/${post_pk}`);const postJson=await postData.json();post_title.innerHTML=postJson.title;post_content.innerHTML=postJson.content;const commentsData=await fetch(window.location.origin+`/api/comments?post=${post_pk}`);const commentsJson=await commentsData.json();commentsJson.sort((a,b)=>a.created_at<b.created_at);comments_container.innerHTML=``;for(const comment of commentsJson){const html=`<div class="comment-container">
	        <p class="'comment-author">${comment.author}</p>
	      <p class="comment-body">${comment.body}</p>
	      <p class="timestamp">${comment.created_at}</p>`;comments_container.insertAdjacentHTML('afterbegin',html);}})();;