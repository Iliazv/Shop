function showForm() {
    document.getElementsByClassName('page__comments_list')[0].style.display = 'block';
    document.getElementsByClassName('page__comment_show')[0].style.display = 'none';
}

function hideForm() {
    document.getElementsByClassName('page__comments_list')[0].style.display = 'none';
    document.getElementsByClassName('page__comment_show')[0].style.display = 'inline-block';
}