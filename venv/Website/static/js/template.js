function warning(element) {
    element.remove()
}

let count = 0
InterfaceLanguage = document.getElementById('languages')

function language(x) {
    count = count + x
    if (count == 1) {
        for (let i = 0; i < InterfaceLanguage.children.length; i++) {
            InterfaceLanguage.children[i].style.display = "list-item";
        }
    } else {
        for (let i = 0; i < InterfaceLanguage.children.length; i++) {
            if (i != 0) {
                InterfaceLanguage.children[i].style.display = "None";
            }
        } 
        count = 0
    }
}

function done(element) {
    if (element.checked != false) {
        task = element.id.replace("done", "")
        window.location.href = 'http://127.0.0.1:5000/en/execute/done/'+task
    } else {
        task = element.id.replace("done", "")
        window.location.href = 'http://127.0.0.1:5000/en/execute/doneRemove/'+task
    }
}