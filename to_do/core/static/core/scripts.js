const nav = document.querySelector('#nav')
const offcanvasToggler = document.querySelector('#offcanvas-toggler')
const offcanvasClose = document.querySelector('#offcanvas-close')

offcanvasToggler.addEventListener('click', () => {
    nav.classList.add('active')
})

offcanvasClose.addEventListener('click', () => {
    nav.classList.remove('active')
})


//dark mode
let darkMode = localStorage.getItem('darkMode') || false
const themeToggler = document.querySelector('#theme-changer')

function setDarkMode () {
    document.documentElement.setAttribute('theme', 'dark')
    themeToggler.querySelector('i').classList.remove('ri-moon-fill')
    themeToggler.querySelector('i').classList.add('ri-sun-line')
}

function setLightMode () {
    document.documentElement.removeAttribute('theme')
    themeToggler.querySelector('i').classList.remove('ri-sun-line')
    themeToggler.querySelector('i').classList.add('ri-moon-fill')
}

//if ( localStorage.getItem('darkMode') == false ) {
//    setLightMode ()
//} else {
//    setDarkMode ()
//}

themeToggler.addEventListener('click', () => {

    if ( darkMode == false ) {
        setDarkMode ()
        darkMode = true
        localStorage.setItem('darkMode', 'true')
    } else {
        setLightMode ()
        darkMode = false
        localStorage.setItem('darkMode', 'false')
    }
})






