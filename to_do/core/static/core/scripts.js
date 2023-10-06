/**
   * HEADER
    */

//offcanvas menu toggle
const nav = document.querySelector('#nav')
const offcanvasToggler = document.querySelector('#offcanvas-toggler')
const offcanvasClose = document.querySelector('#offcanvas-close')

offcanvasToggler.addEventListener('click', () => {
    nav.classList.add('active')
})

offcanvasClose.addEventListener('click', () => {
    nav.classList.remove('active')
})

//header user menu toggle
const headerUserElement = document.getElementById('header-user')

if(headerUserElement){
    const headerUserWrapper = headerUserElement.querySelector('.header-user-wrapper')
    const headerUserMenuToggler = headerUserElement.querySelector('#header-user-toggler')

    headerUserMenuToggler.addEventListener('click', () => {
        headerUserWrapper.classList.toggle('active')

        window.addEventListener('click', (e) => {
            if ( e.target.id ==! 'header-user-toggler' && !e.target.closest('#header-user') ) {
                headerUserWrapper.classList.remove('active')
            }
        })
    })
}


/**
   * DARK MODE
    */

let darkMode = JSON.parse(localStorage.getItem('darkMode'))
const themeToggler = document.querySelector('#theme-changer')

if ( darkMode == 'false' ) {
    setLightMode ()
} else {
    setDarkMode ()
}

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

themeToggler.addEventListener('click', () => {
    let darkMode = JSON.parse(localStorage.getItem('darkMode'))
    if ( darkMode == 'false' ) {
        setDarkMode ()
        darkMode = true
        localStorage.setItem('darkMode', JSON.stringify('true'))
    } else {
        setLightMode ()
        darkMode = false
        localStorage.setItem('darkMode', JSON.stringify('false'))
    }
})

/**
   * MESSAGE POPUPS
    */

//remove message popup
const removeMessagePopup = () => {
    const messagePopup = document.querySelector('.message-popup')
    if (messagePopup) {
        setTimeout(()=>{
            messagePopup.classList.remove('active')
            setTimeout(()=>{
                messagePopup.remove()
            }, 300)
        }, 5000)
    }
}

//message popup animation when backend generates it
const messagePopup = document.querySelector('.message-popup')
if (messagePopup) {
    setTimeout(()=>{
        messagePopup.classList.add('active')
        removeMessagePopup()
    }, 700)
}

//show custom message
const createMessagePopup = (message, role) => {
    const messagePopup = document.createElement('div')
    messagePopup.classList.add('message-popup')
    messagePopup.classList.add(role)
    messagePopup.textContent = message
    document.querySelector('main').prepend(messagePopup)

    setTimeout(()=>{
        messagePopup.classList.add('active')
        removeMessagePopup()
    }, 700)
}