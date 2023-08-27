function changeImage(short) {
    document.getElementById("photo__main_" + short).style.display = "none";
    document.getElementById("photo__replace_" + short).style.display = "block";
}

function returnImage(short) {
    document.getElementById("photo__main_" + short).style.display = "block";
    document.getElementById("photo__replace_" + short).style.display = "none";
}