datetime = new Date()
const year = datetime.getFullYear();
const month = ('0' + (datetime.getMonth() + 1)).slice(-2);
const day = ('0' + (datetime.getDate()+1)).slice(-2);
const formattedDate = `${year}-${month}-${day} 00:00:00`;


date = document.getElementById('date')
date.min = formattedDate