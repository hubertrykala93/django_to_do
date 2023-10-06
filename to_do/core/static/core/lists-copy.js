//add task content
function addTaskContentToDOM(categoryId, categoryName) {
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
        `
        categoriesContentsWrapper.prepend(newTaskContent)

        const categoriesContentsItems = document.querySelectorAll('.categories-content-body .category-content')
        categoriesContentsItems.forEach(item => {
            item.classList.remove('active')
        })
        categoriesContentsItems[0].classList.add('active')
}

//add category to DOM and close popup
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

    const categoriesListItems = document.querySelectorAll('.categories-list li')
    categoriesListItems.forEach(item => {
        item.classList.remove('active')
    })
    categoriesListItems[0].classList.add('active')

    document.querySelector('.to-do-list-wrapper aside').scrollTop = 0;
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
                addCategoryToDOM(data.category_name, data.category_id)
                addTaskContentToDOM(data.category_id, data.category_name)
                document.querySelector('.lists-popup-wrapper').remove()
                createMessagePopup(data.message, 'success')
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

//ajax remove category
function removeCategoryAjax(){
    const categoriesList = document.querySelector('.categories-list')
    if (categoriesList){
        categoriesList.addEventListener('click', e =>{
            const target = e.target.parentElement
            if ( target.classList.contains('remove-category') ){
                const currentItemId = target.parentElement.parentElement.getAttribute('data-id')

                const removingConfirmation = confirm('Are You sure?')
                if(removingConfirmation){
                    $.ajax({
                        type: 'POST',
                        url: '/delete-category',
                        data: {
                            categoryId: currentItemId
                        },
                        success: function(data){
                            console.log(data)
                            if( data.valid ){
                                document.querySelector(`.categories-list li[data-id="${currentItemId}"]`).remove()
                                document.querySelector(`.to-do-list-contents .category-content[data-id="${currentItemId}"]`).remove()
                                createMessagePopup(data.message, 'info')
                            } else {

                            }
                        }
                    });
                }
            }
        })
    }
}
removeCategoryAjax()

//ajax edit category
function editCategoryAjax(){
    const categoriesList = document.querySelector('.categories-list')
    if(categoriesList){
        categoriesList.addEventListener('click', e =>{
            const target = e.target.parentElement
            if ( target.classList.contains('edit-category') ){
                const currentItemId = target.parentElement.parentElement.getAttribute('data-id')
                createListPopup('edit-category-popup-wrapper', 'edit-category-form', 'edit-form', 'post', '/edit-category', 'edit-category-name', 'categoryId', 'New category name', 'edit-category-btn', 'ri-edit-2-fill', 'Edit name')
                const currentName = target.parentElement.parentElement.querySelector('span').innerText
                document.querySelector('.edit-category-form input').value = currentName
                $('#edit-form').on('submit', function (e){
                    e.preventDefault();
                    $.ajax({
                        type: 'POST',
                        url: '/edit-category',
                        data: {
                            categoryId: currentItemId,
                            name: document.querySelector('#edit-form input').value
                        },
                        success: function(data){
                            if( data.valid ){
                                target.parentElement.parentElement.querySelector('span').innerText = document.querySelector('#edit-form input').value
                                document.querySelector('.lists-popup-wrapper').remove()
                                createMessagePopup(data.message, 'success')
                            } else {

                            }
                        }
                    });
                });

            }
        })
    }

}
editCategoryAjax()

//popup remove
function removeListPopup(){
    const closeAddListsPopup = document.querySelector('#close-lists-popup')
    closeAddListsPopup.addEventListener('click', ()=> {
        document.querySelector('.lists-popup-wrapper').remove()
    })
}

//popup constructor
function createListPopup(wrapperClass, formClass, formId, method, action, inputId, inputName, inputPlaceholder, btnClass, btnIcon, btnText){

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
                        <i class="${btnIcon}"></i>
                        ${btnText}
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
        createListPopup('add-category-popup-wrapper', 'add-to-category-form', 'category-form', 'post', '/add-category', 'add-category-name', 'category', 'Category name', 'add-new-category-btn', 'ri-add-box-line', 'Add category')
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
    if (listsContents){
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
}
toggleTaskForm()