const popup1 = document.getElementById('simpleModalSignup');
const popup2 = document.getElementById('simpleModalRegister');
const modalBtn = document.getElementById('modalBtn');
const back = document.getElementById('popup__area');


const closeBtn = document.getElementsByClassName('closeBtn')[0];
//const submitBtn = document.getElementsByClassName('welcome__button')[0];

const closeBtn1 = document.getElementsByClassName('closeBtn')[1];
//const submitBtn1 = document.getElementsByClassName('welcome__button')[1];

const changeBtn = document.getElementsByClassName('register')[0];
const changeBtn1 = document.getElementsByClassName('signup')[0];

modalBtn.addEventListener('click', OpenWindow);

closeBtn.addEventListener('click', CloseSignup);
//submitBtn.addEventListener('click', CloseSignup);

closeBtn1.addEventListener('click', CloseRegister);
//submitBtn1.addEventListener('click', CloseRegister);

changeBtn.addEventListener('click', CloseSignup);
changeBtn.addEventListener('click', NewWindow);

changeBtn1.addEventListener('click', CloseRegister);
changeBtn1.addEventListener('click', NewWindow1);


function OpenWindow() {
    popup1.style.transform = 'scale(1)';
}

function CloseSignup() {
    popup1.style.transform = 'scale(0)';
}

function CloseRegister() {
    popup2.style.transform = 'scale(0)';
}

function NewWindow() {
    popup2.style.transform = 'scale(1)';
}

function NewWindow1() {
    popup1.style.transform = 'scale(1)';
}


// function outsideClick(e) {
//     if (e.target == popup1) {
//         if (e.target != back) {
//             popup1.style.transform = 'scale(0)';
//         }
//     } else if (e.target == popup2) {
//         popup2.style.transform = 'scale(0)';
//     }
// }

back.addEventListener('click', () => {
    alert('hello world')
})