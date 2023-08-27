const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons = document.querySelectorAll('[data-close-button]')

const crossButtonUsa = document.getElementById('cross_button1')
const crossButtonChina = document.getElementById('cross_button2')
const overlay = document.getElementById('overlay')

const changeCountryRussia = document.getElementsByClassName('modal_russia')[0]
const changeCountryUsa = document.getElementsByClassName('modal_usa')[0]
const changeCountryChina = document.getElementsByClassName('modal_china')[0]
const changeCountryRussia1 = document.getElementsByClassName('modal_russia')[1]
const changeCountryUsa1 = document.getElementsByClassName('modal_usa')[1]
const changeCountryChina1 = document.getElementsByClassName('modal_china')[1]
const changeCountryRussia2 = document.getElementsByClassName('modal_russia')[2]
const changeCountryUsa2 = document.getElementsByClassName('modal_usa')[2]
const changeCountryChina2 = document.getElementsByClassName('modal_china')[2]

openModalButtons.forEach(button => {
    const modals = document.querySelectorAll('.modal1.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})

overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 = document.querySelectorAll('.modal_1.active')
    const modals2 = document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
})

crossButtonUsa.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal_1.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

closeModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('.modal')
        closeModal(modal)
    })
})

crossButtonChina.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

changeCountryUsa.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    const newModal = document.getElementsByClassName('modal_1')[0]
    openModal(newModal)
})
changeCountryChina.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    const newModal = document.getElementsByClassName('modal_2')[0]
    openModal(newModal)
})
changeCountryRussia.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    condition = 0
    const newModal = document.getElementsByClassName('modal')[0]
    openModal(newModal)
})

changeCountryUsa1.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    const newModal = document.getElementsByClassName('modal_1')[0]
    openModal(newModal)
})
changeCountryChina1.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    const newModal = document.getElementsByClassName('modal_2')[0]
    openModal(newModal)
})
changeCountryRussia1.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    condition = 0
    const newModal = document.getElementsByClassName('modal')[0]
    openModal(newModal)
})

changeCountryUsa2.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    const newModal = document.getElementsByClassName('modal_1')[0]
    openModal(newModal)
})
changeCountryChina2.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    const newModal = document.getElementsByClassName('modal_2')[0]
    openModal(newModal)
})
changeCountryRussia2.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    const modals1 =document.querySelectorAll('.modal_1.active')
    const modals2 =document.querySelectorAll('.modal_2.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
    modals1.forEach(modal => {
        closeModal(modal)
    })
    modals2.forEach(modal => {
        closeModal(modal)
    })
    condition = 0
    const newModal = document.getElementsByClassName('modal')[0]
    openModal(newModal)
})


function openModal(modal) {
    if (modal == null) return
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal(modal) {
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}

function showPassword(target, id) {
    if (id === 1) {
        var input = document.getElementById('password-input-1');
    } else {
        var input = document.getElementById('password-input-2');
    }
	if (input.getAttribute('type') == 'password') {
		target.classList.add('view');
		input.setAttribute('type', 'text');
	} else {
		target.classList.remove('view');
		input.setAttribute('type', 'password');
	}
	return false;
}