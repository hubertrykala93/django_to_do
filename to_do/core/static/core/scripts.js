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

//lists component

//add category to DOM and close popup
function addCategoryToDOM(categoryName){
    console.log(categoryName)
    const categoriesList = document.querySelector('.categories-list')
    const newListItem = document.createElement('li')
    newListItem.innerHTML = `
        <span>${categoryName}</span>

        <div class="buttons">

            <button class="remove-category" data-cid="{{ category.id }}">
                <i class="ri-delete-bin-line"></i>
            </button>

            <button class="edit-category" data-cid="{{ category.id }}">
                <i class="ri-edit-line"></i>
            </button>

        </div>
    `

    categoriesList.prepend(newListItem)
}

//ajax add category
function addCategoryAjax(){
$('#category-form').on('submit', function (e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/add-category',
        data: {
            category: $('input[name=category]').val()
        },
        success: function(data){
            if( data.valid ){
                addCategoryToDOM($('input[name=category]').val())
                document.querySelector('.lists-popup-wrapper').remove()
            } else {
                const formError = document.querySelector('.error')
                formError.classList.add('active')
                if(formError){
                    formError.innerHTML = data.message
                }
            }
        }
    });
});
}

//popup remove
function removeListPopup(){
    const closeAddListsPopup = document.querySelector('#close-lists-popup')
    closeAddListsPopup.addEventListener('click', ()=> {
        document.querySelector('.lists-popup-wrapper').remove()
    })
}

//popup constructor
function createListPopup(wrapperClass, formClass, formId, method, action, inputId, inputName, inputPlaceholder, btnClass){

    const addListsPopup = document.createElement('div')
        addListsPopup.classList.add(wrapperClass)
        addListsPopup.classList.add('lists-popup-wrapper')
        addListsPopup.innerHTML = `
            <div class="lists-popup-container">
                <div id="close-lists-popup">
                    <i class="ri-close-line"></i>
                </div>

                <form class="${formClass}" id="${formId}" method="${method}" action="${action}">
                    <input type="text" id="${inputId}" name="${inputName}" placeholder="${inputPlaceholder}">
                    <div class="error"></div>
                    <button class="btn ${btnClass}" type="submit">
                        <i class="ri-add-box-line"></i>
                        Add Category
                    </button>
                </form>
            </div>
        `
        document.body.append(addListsPopup)

        removeListPopup()
}

//add category btn listener
const addCategoryBtn = document.querySelector('.add-category-btn')
if(addCategoryBtn){
    addCategoryBtn.addEventListener('click', ()=> {
        createListPopup('add-category-popup-wrapper', 'add-to-category-form', 'category-form', 'post', '/add-category', 'add-category-name', 'category', 'Category name', 'add-new-category-btn')
        addCategoryAjax()
    })
}


//to do categories list behaviour
function categoriesFunction() {
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
}
categoriesFunction()


//toggle add task form
function toggleTaskForm(){
    const listsContents = document.querySelector('.to-do-list-contents')
    listsContents.addEventListener('click', e => {
        const target = e.target
        if ( target.classList.contains('toggle-task-form') ){

            if ( target.nextElementSibling.classList.contains('visible') ){
                target.nextElementSibling.style.maxHeight = "0px"
                target.nextElementSibling.classList.remove('visible')
                return
            }
            const contentHeight = target.nextElementSibling.scrollHeight
            target.nextElementSibling.style.maxHeight = contentHeight + "px"
            target.nextElementSibling.classList.add('visible')
        }
    })
}
toggleTaskForm()


