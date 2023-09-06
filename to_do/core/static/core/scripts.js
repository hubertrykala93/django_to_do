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


//dark mode
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

//message popup
const messagePopup = document.querySelector('.message-popup')

if (messagePopup) {
    setTimeout(()=>{
        messagePopup.classList.add('active')

        setTimeout(()=>{
            messagePopup.classList.remove('active')
            messagePopup.remove()
        }, 5000)
    }, 700)
}

//tabs component
const tabsElement = document.querySelector('.tabs-wrapper')

if(tabsElement){
    const tabsNavItems = tabsElement.querySelectorAll('.tabs-nav li')
    const tabsContentItems = tabsElement.querySelectorAll('.tabs-contents .tab-content')

    tabsContentItems[0].classList.add('active')
    tabsNavItems[0].classList.add('active')

    tabsNavItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            tabsContentItems.forEach((content) => {
                content.classList.remove('active')
            })
            tabsContentItems[index].classList.add('active')

            tabsNavItems.forEach(item =>{item.classList.remove('active')})
            tabsNavItems[index].classList.add('active')
        })
    })
}

