const nav = document.querySelector('#nav')
const offcanvasToggler = document.querySelector('#offcanvas-toggler')
const offcanvasClose = document.querySelector('#offcanvas-close')

offcanvasToggler.addEventListener('click', () => {
    nav.classList.add('active')
})

offcanvasClose.addEventListener('click', () => {
    nav.classList.remove('active')
})


//theme change
const themeToggler = document.querySelector('#theme-changer')

themeToggler.addEventListener('click', () => {
    if ( document.documentElement.getAttribute('theme') === 'dark' ){
        document.documentElement.removeAttribute('theme')
        themeToggler.querySelector('i').classList.remove('ri-sun-line')
        themeToggler.querySelector('i').classList.add('ri-moon-fill')
    }else {
        document.documentElement.setAttribute('theme', 'dark')
        themeToggler.querySelector('i').classList.remove('ri-moon-fill')
        themeToggler.querySelector('i').classList.add('ri-sun-line')
    }
})