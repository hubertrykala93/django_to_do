/**
      * TABS LOGIC
        */

    //tabs navigation
    const tabsWrapper = document.querySelector('.tabs-wrapper')
    const tabsNavItems = tabsWrapper.querySelectorAll('.tabs-nav li')
    const tabsContentItems = tabsWrapper.querySelectorAll('.tabs-contents .tab-content')

    tabsContentItems[0].classList.add('active')
    tabsNavItems[0].classList.add('active')

    tabsNavItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            tabsContentItems.forEach((content) => {content.classList.remove('active')})
            tabsContentItems[index].classList.add('active')

            tabsNavItems.forEach(item =>{item.classList.remove('active')})
            tabsNavItems[index].classList.add('active')
        })
    })