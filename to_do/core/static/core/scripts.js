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


//add to do category
const addCategoryBtn = document.querySelector('.add-category-btn')

if(addCategoryBtn){
    addCategoryBtn.addEventListener('click', ()=> {
        const addCategoryPopup = document.querySelector('.add-category-popup-wrapper')
        addCategoryPopup.classList.add('active')

        const closeAddCategoryPopup = document.querySelector('#close-add-category-popup')
        closeAddCategoryPopup.addEventListener('click', ()=> {
            addCategoryPopup.classList.remove('active')
        })
    })
}


//to do tabs

const toDoListWrapper = document.querySelector('.to-do-list-wrapper')

if(toDoListWrapper){
    const categoriesList = document.querySelector('.categories-list')
    const firstListItem = categoriesList.querySelector('li')
    if( firstListItem ) {
        firstListItem.classList.add('active')
        const firstListItemId = firstListItem.getAttribute('data-id')
        const firstCategoryContent = toDoListWrapper.querySelector(`.to-do-list-contents > .category-content[data-id="${firstListItemId}"]`)
        if (firstCategoryContent ){
            firstCategoryContent.classList.add('active')
        }
    }

    categoriesList.addEventListener('click', e => {
        if ( e.target.tagName  === "SPAN" || e.target.tagName  === "LI" ) {
            categoriesList.querySelectorAll('li').forEach(item => {item.classList.remove('active')})

            let currentCategoryId
            if ( e.target.tagName  === "SPAN" ){
                e.target.parentElement.classList.add('active')
                currentCategoryId = e.target.parentElement.getAttribute('data-id')
            } else{
                e.target.classList.add('active')
                currentCategoryId = e.target.getAttribute('data-id')
            }

            const allCategoriesContents = toDoListWrapper.querySelectorAll('.to-do-list-contents > .category-content')
            allCategoriesContents.forEach(item => {
                item.classList.remove('active')
                if ( item.getAttribute('data-id') === currentCategoryId ){
                    item.classList.add('active')
                }
            })
        }
    })
}



//JSON TEST


//const getJson = document.querySelector('#get-json')
//
//
//if(getJson){
//    function getJsonFun(){
//        const xhr = new XMLHttpRequest();
//        xhr.open("GET", "data.json", true);
//
//        xhr.onload = () => {
//            if ( xhr.status === 200){
//              let data = JSON.parse(xhr.responseText)
//              alert(data[1].userId)
//            }
//        }
//
//        xhr.send();
//    }
//    getJson.addEventListener('click', getJsonFun)
//}

//ajax add category

$('#category-form').on('submit', function (e){
    e.preventDefault();
        console.log('seks ze starą')
    $.ajax({
        type: 'POST',
        url: '/add-category',
        data: {
            category: $('input[name=category]').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            console.log(data);
        }
    });
});

//ajax add task

$('#add-task').on('submit', function (e){
    e.preventDefault();
        console.log('seks ze starą')
    $.ajax({
        type: 'POST',
        url: '/add-task',
        data: {
            name: $('input[name=task-name]').val(),
            description: $('input[name=task-description]').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            console.log(data);
        }
    });
});