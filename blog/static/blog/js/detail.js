function actionTableOfContents () {
    const button = document.getElementsByClassName("reduceButton")[0];
    if (button.classList.contains("reduce")) {
        reduceTableOfContents();
    }
    else if (button.classList.contains("expand")) {
        expandTableOfContents();
    }
}



function reduceTableOfContents () {
    const tableOfContents = document.getElementsByClassName("tableOfContentsWrapper")[0];
    const button = document.getElementsByClassName("reduceButton")[0];

    tableOfContents.style.opacity ="0%";
    setTimeout(()=>{
        tableOfContents.style.width = '0px';
        tableOfContents.style.height = '0px';
        button.style.transform = 'rotate(180deg)';
        button.classList.toggle("reduce");
        button.classList.toggle("expand");
    },100)
    // setTimeout(()=>{
    //     tableOfContents.style.display = 'none';
    // },1100)

    // button.onclick = expandTableOfContents();
}

function expandTableOfContents() {
    const tableOfContents = document.getElementsByClassName("tableOfContentsWrapper")[0];
    const button = document.getElementsByClassName("reduceButton")[0];

    // tableOfContents.style.display = 'block';
    tableOfContents.style.width = '300px';
    button.style.transform = 'rotate(0deg)';
    setTimeout(()=>{
        tableOfContents.style.height = '70vh';
    },500);
    setTimeout(()=>{
        tableOfContents.style.opacity = "100%";
        button.classList.toggle("reduce");
        button.classList.toggle("expand");        
    },900);

    // button.onclick = reduceTableOfContents();
}


function reply (comment_id) {
    if (document.getElementsByClassName("commentReplyText"+comment_id).length == 0) {
    
    const form = document.getElementById("reply"+comment_id);

    const comment_text = document.createElement('textarea');
    comment_text.name = "comment_text";
    comment_text.placeholder = "Enter your reply here...";
    comment_text.classList.add('commentInputText');
    comment_text.classList.add("commentReplyText"+comment_id);
    comment_text.required = true;
    
    // input type 'hidden' contenant l'identifiant du commentaire parent
    const comment_parent = document.createElement('input');
    comment_parent.type='hidden';
    comment_parent.value=comment_id;
    comment_parent.name = "comment_parent";

    const comment_submit = document.createElement('input');
    comment_submit.type = 'submit';
    comment_submit.value = "Post Reply";
    comment_submit.classList.add("commentSubmit");
 
    form.appendChild(comment_text);
    form.appendChild(comment_parent);
    form.appendChild(comment_submit);

    }

}

function deleteComment(comment_id, article_id) {

    if (confirm("Do you really want to delete this comment?")) {
        const form = document.getElementById("deleteForm"+comment_id);
        // form.method = 'post';
        // form.action = document.getElementById("urlDeleteComment").value;
        // form.innerHTML='{% csrf token %}'
        
        const commentId = document.createElement('input');
        commentId.type='hidden';
        commentId.value = comment_id;
        commentId.name = 'commentId';

        const articleId = document.createElement('input');
        articleId.type='hidden';
        articleId.value = article_id;
        articleId.name = 'articleId';

        // document.body.appendChild(form);
        form.appendChild(commentId);
        form.appendChild(articleId);
        form.submit();
    }

}


window.addEventListener('scroll', (event)=>{
    // on fixe la limite d'apparition du bandeau du titre
    // on veut que celui-ci apparaisse lorsque l'on a dépassé le titre en scrollant
    const limit = document.getElementsByClassName("articleAbstract")[0].getBoundingClientRect().bottom;
    const wrapper = document.getElementsByClassName("titleBannerWrapper")[0];
    const tableOfContents = document.getElementsByClassName("tableOfContents")[0];
    const titleBanner = document.getElementsByClassName("titleBanner")[0];
    
    if (document.body.scrollTop>limit) {

        // console.log(window.getComputedStyle(wrapper).getPropertyValue("opacity"));
        
        if (window.getComputedStyle(wrapper).getPropertyValue("opacity")==0) {
            wrapper.style.height = "70px";
            wrapper.style.opacity = "100%";
            tableOfContents.style.top = "131px";
        }
    }

    else {
        if (window.getComputedStyle(wrapper).getPropertyValue("opacity")==1) {

            wrapper.style.opacity = "0%";
            setTimeout(()=>{
                tableOfContents.style.top="81px";
                wrapper.style.height = "0px";
            },500);

        }
    }

});