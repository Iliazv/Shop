const openMod = document.querySelectorAll('[data-modal-target]')
//const crossButton = document.querySelectorAll('[data-close-button]')

const crossButton = document.getElementById('cross_button3')
const overlayChange = document.getElementById('overlay_change')


openMod.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})

crossButton.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal_change.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal_change.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

overlayChange.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal_change')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

closeModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('.modal_change')
        closeModal(modal)
    })
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
    overlayChange.classList.add('enable')
}