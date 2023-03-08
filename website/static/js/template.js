//vars
const formLanguage = document.getElementById("formLanguage")
const selectInput = document.getElementById("language")

//Select Input
selectInput.addEventListener("change", function() {
    formLanguage.submit()
})