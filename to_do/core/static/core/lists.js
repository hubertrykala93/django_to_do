/**
   * FUNCTIONS DECLARATIONS
    */

const setFirstPositionActive = () => {
    const categoriesList = document.querySelector('.categories-list')
    const listItems = categoriesList.querySelectorAll('li')

    if( listItems.length ){
        listItems.forEach((item, index) =>{
            if(index === 0){item.classList.add('active')} 
            else{item.classList.remove('active')}
        })

        const categoryContents = document.querySelectorAll('.to-do-list-contents .category-content')
        if ( categoryContents.length ){
            categoryContents.forEach((item, index) =>{
                if(index === 0){item.classList.add('active')} 
                else{item.classList.remove('active')}
            })
        }
    }
}

const listItemsNavigation = (e) => {
    categoriesList.querySelectorAll('li').forEach(item => {item.classList.remove('active')})

    let currentCategoryId
    if ( e.target.tagName  === "SPAN" ){
        e.target.parentElement.classList.add('active')
        currentCategoryId = e.target.parentElement.getAttribute('data-id')
    } else{
        e.target.classList.add('active')
        currentCategoryId = e.target.getAttribute('data-id')
    }

    const allCategoriesContents = document.querySelectorAll('.to-do-list-contents > .category-content')
    if( allCategoriesContents.length ){
        allCategoriesContents.forEach(item => {
            item.classList.remove('active')
            if ( item.getAttribute('data-id') === currentCategoryId ){
                item.classList.add('active')
            }
        })
    }
}

function removeListPopup(){
    window.addEventListener('click', (e)=> {
        if( e.target.classList.contains('lists-popup-wrapper') || e.target.id === 'close-lists-popup' || e.target.parentElement.id === 'close-lists-popup' ){
            if ( document.querySelector('.lists-popup-wrapper') ){
                document.querySelector('.lists-popup-wrapper').remove()
            }
        }
    })
}

const showListPopupError = (message) => {
    const formError = document.querySelector('.lists-popup-wrapper form .error')
    if(formError){
        formError.classList.add('active')
        formError.innerHTML = message
    }
}

const createListPopup = (wrapperClass, formClass, formId, method, action, inputId, inputName, inputPlaceholder, btnClass, btnIcon, btnText) =>{
    const addListsPopup = document.createElement('div')
        addListsPopup.classList.add(wrapperClass)
        addListsPopup.classList.add('lists-popup-wrapper')
        addListsPopup.innerHTML = `
            <div class="lists-popup-container">
                <div id="close-lists-popup">
                    <i class="ri-close-line"></i>
                </div>

                <form class="${formClass}" id="${formId}" method="${method}" action="${action}">
                    <div class="form-row">
                        <div class="input-wrapper">
                            <input type="text" id="${inputId}" name="${inputName}" placeholder="${inputPlaceholder}">
                            <div class="error"></div>
                        </div>
                    </div>
                    <div class="submit-row">
                        <button class="btn ${btnClass}" type="submit">
                            <i class="${btnIcon}"></i>
                            ${btnText}
                        </button>
                    </div>
                </form>
            </div>
        `
        document.body.append(addListsPopup)

        removeListPopup()
}

const addTaskContentToDOM = (categoryId, categoryName) => {
    const categoriesContentsWrapper = document.querySelector('.categories-content-body')
    const newTaskContent = document.createElement('div')
    newTaskContent.classList.add('category-content')
    newTaskContent.setAttribute('data-id', categoryId)
    newTaskContent.innerHTML = `
        <h3 class="category-title">${categoryName}</h3>

        <div class="add-task-form-wrapper">
            <button class="btn toggle-task-form">
                <i class="ri-add-line"></i>
                Add new item
            </button>

            <form class="add-task-form" id="add-task" method="post" action="">

                <div class="form-row">
                    <div class="input-wrapper">
                        <input type="hidden" name="${categoryId}">
                    </div>
                </div>

                <div class="form-row">
                    <div class="input-wrapper">
                        <input type="text" id="add-task-name" name="task-name" placeholder="Task name">
                    </div>
                </div>

                <div class="form-row">
                    <div class="input-wrapper">
                        <textarea id="add-task-description" name="task-description"
                                  placeholder="Task description"></textarea>
                    </div>
                </div>

                <div class="submit-row">
                    <button class="btn" type="submit">
                        <i class="ri-play-list-add-line"></i>
                        Add item
                    </button>
                </div>

            </form>
        </div>
        <div class="tasks-list"></div>
        `
        categoriesContentsWrapper.prepend(newTaskContent)
}

const addNewCategory = () => {

    //add category to DOM
    function addCategoryToDOM(categoryName, categoryId){
        const categoriesList = document.querySelector('.categories-list')
        const newListItem = document.createElement('li')
        newListItem.setAttribute('data-id', categoryId)
        newListItem.innerHTML = `
            <span>${categoryName}</span>

            <div class="buttons">

                <button class="edit-category" data-category-id="${categoryId}">
                    <i class="ri-edit-line"></i>
                </button>

                <button class="remove-category" data-category-id="${categoryId}">
                    <i class="ri-delete-bin-line"></i>
                </button>

            </div>
        `

        categoriesList.prepend(newListItem)
        document.querySelector('.to-do-list-wrapper aside').scrollTop = 0;
    }

    const addCategoryForm = document.getElementById('category-form')
    addCategoryForm.addEventListener('submit', (e) => {
        e.preventDefault()

        $.ajax({
            type: 'POST',
            url: '/add-category',
            data: {
                category: addCategoryForm.querySelector('#add-category-name').value
            },
            success: function(data){
                if( data.valid ){
                    addCategoryToDOM(data.category_name, data.category_id)
                    addTaskContentToDOM(data.category_id, data.category_name)
                    document.querySelector('.lists-popup-wrapper').remove()
                    setFirstPositionActive()
                    createMessagePopup(data.message, 'success')
                } else {
                    showListPopupError(data.message)
                }
            }
        });
    })
}

const editCategory = (targetLi, currentItemId) =>{

    createListPopup('edit-category-popup-wrapper', 'edit-category-form', 'edit-form', 'post', '/edit-category', 'edit-category-name', 'categoryId', 'New category name', 'edit-category-btn', 'ri-edit-2-fill', 'Edit name')
    const currentName = targetLi.querySelector('span').innerText
    document.querySelector('.edit-category-form input').value = currentName

    const editCategoryForm = document.getElementById('edit-form')
    editCategoryForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const newCategoryName = editCategoryForm.querySelector('#edit-category-name').value
        $.ajax({
            type: 'POST',
            url: '/edit-category',
            data: {
                categoryId: currentItemId,
                name: newCategoryName
            },
            success: function(data){
                if( data.valid ){
                    targetLi.querySelector('span').innerText = newCategoryName
                    document.querySelector(`.to-do-list-contents .category-content[data-id="${currentItemId}"] .category-title`).innerText = newCategoryName
                    document.querySelector('.lists-popup-wrapper').remove()
                    createMessagePopup(data.message, 'success')
                } else {
                    showListPopupError(data.message)
                }
            }
        });
    })
}

const deleteCategory = (currentItemId) => {
    const removingConfirmation = confirm('Are You sure?')
    if(removingConfirmation){
        $.ajax({
            type: 'POST',
            url: '/delete-category',
            data: {
                categoryId: currentItemId
            },
            success: function(data){
                if( data.valid ){
                    document.querySelector(`.categories-list li[data-id="${currentItemId}"]`).remove()
                    document.querySelector(`.to-do-list-contents .category-content[data-id="${currentItemId}"]`).remove()
                    setFirstPositionActive()
                    createMessagePopup(data.message, 'info')
                }
            }
        });
    }
}

const toggleTaskForm = (target)=> {
    const formElement = target.nextElementSibling
    if ( formElement.classList.contains('visible') ){
        formElement.style.maxHeight = "0px"
        formElement.classList.remove('visible')
        return
    }
    const contentHeight = formElement.scrollHeight
    formElement.style.maxHeight = contentHeight + "px"
    formElement.classList.add('visible')
}

const addNewTask = (btn) => {
    const addTaskForm = btn.closest('.add-task-form')

    addTaskForm.addEventListener('submit', (e) => {
        e.preventDefault()

        const newTaskName = addTaskForm.querySelector('.add-task-name').value
        const newTaskDescription = addTaskForm.querySelector('.add-task-description').value
        const taskParentCategoryId = addTaskForm.closest('.category-content').getAttribute('data-id')
        $.ajax({
            type: 'POST',
            url: '/add-task',
            data: {
                name: newTaskName,
                description: newTaskDescription,
                categoryId: taskParentCategoryId
            },
            success: function(data){
                if( data.valid ){
                    createMessagePopup(data.message, 'success')
                } else {
                    
                }
            }
        });
    })
}

//list event listener
const categoriesList = document.querySelector('.categories-list')

if(categoriesList){
    setFirstPositionActive()

    categoriesList.addEventListener('click', e =>{
        //nawigacja po elementach listy
        if ( e.target.tagName  === "SPAN" || e.target.tagName  === "LI" ) {
            listItemsNavigation(e)
        } 
        //edycja nazwy kategorii
        else if ( e.target.parentElement.classList.contains('edit-category') ) {
            const targetLi = e.target.parentElement.parentElement.parentElement
            const currentItemId = e.target.parentElement.parentElement.parentElement.getAttribute('data-id')
            editCategory(targetLi, currentItemId)
            console.log('edycja')
        }
        //usuwanie kategorii
        else if ( e.target.parentElement.classList.contains('remove-category') ) {
            const currentItemId = e.target.parentElement.parentElement.parentElement.getAttribute('data-id')
            deleteCategory(currentItemId)
            console.log('usuwanie')
        }
    })
}

//add category btn event listener
const addCategoryBtn = document.querySelector('.to-do-list-wrapper .add-category-btn')
if(addCategoryBtn){
    addCategoryBtn.addEventListener('click', ()=> {
        createListPopup('add-category-popup-wrapper', 'add-to-category-form', 'category-form', 'post', '/add-category', 'add-category-name', 'category', 'Category name', 'add-new-category-btn', 'ri-add-box-line', 'Add category')
        addNewCategory()
    })
}

//category content event listener
const listsContents = document.querySelector('.to-do-list-contents')
listsContents.addEventListener('click', e => {
    const target = e.target
    //toggle task form
    if ( target.classList.contains('toggle-task-form') ) {
        toggleTaskForm(target)
    }
    //add new task
    else if ( target.id === 'add-task' || target.parentElement.id === 'add-task' ) {
        addNewTask(target)
    }
})