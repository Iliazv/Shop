function showCommentaries() {
    document.querySelector(".page__comment:nth-child(1n+4)").style.display = 'block';
    document.getElementsByClassName('page__comment_more')[0].style.display = 'none';
    document.getElementsByClassName('page__comment_remove')[0].style.display = 'inline-block';
}

function hideCommentaries() {
    document.querySelector(".page__comment:nth-child(1n+4)").style.display = 'none';
    document.getElementsByClassName('page__comment_more')[0].style.display = 'inline-block';
    document.getElementsByClassName('page__comment_remove')[0].style.display = 'none';
}