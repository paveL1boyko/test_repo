// let elem = document.querySelector('form div')
function add_input() {
    let elem2 = document.querySelector('form>div:last-of-type')
    let copy_elem = elem2.cloneNode(true)
    let elem_input = copy_elem.querySelector('input')
    elem_input.value = ''
    let name = elem_input.getAttribute('name')
    let new_name = 'name' + (parseInt(name.match(/\d+/)) + 1)
    copy_elem.querySelector('strong').innerText = new_name
    elem_input.setAttribute('name',  new_name)
    elem2.after(copy_elem)
}

function remove_input() {
    let elem2 = document.querySelector('form>div:last-of-type')
    if (elem2.parentNode.childElementCount > 3) {
        elem2.remove()
    }
}
