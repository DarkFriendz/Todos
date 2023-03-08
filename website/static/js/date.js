//vars
const dateInput = document.getElementById("date")

//Date Input
date = new Date().toISOString()
date = date.split("T")
date = date[0]+"T00:00:00"
dateInput.min = date