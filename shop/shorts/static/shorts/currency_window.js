function changeCurrency(currency) {
    localStorage.setItem('currency', currency)
    currency = localStorage.setItem('currency', currency)

    currency = localStorage.getItem('currency')
    document.getElementById("hat__hidden").value = currency;
}

function getCurrency() {
    currency = localStorage.getItem('currency')
    document.getElementById("hat__hidden").value = currency;
}

function changeCity(city) {
    localStorage.setItem('city', city)
    city = localStorage.setItem('city', city)

    city = localStorage.getItem('city')
    document.getElementById("modal-hidden").value = encodeURIComponent(city);
}

function getCity() {
    city = localStorage.getItem('city')
    document.getElementById("min").innerHTML = decodeURIComponent(city);
    document.getElementById("min_special").innerHTML = decodeURIComponent(city);
}



getCurrency()
getCity()