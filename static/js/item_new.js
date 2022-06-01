try {
    const now = new Date()
const dateField = document.getElementById("id_save_until")
const addZero = (num) => num < 9 ? "0" + num : num
const nowDate = `${now.getFullYear()}-${addZero(now.getMonth() + 1)}-${addZero(now.getDate() + 2)}`
dateField.min = nowDate
console.log(dateField.min)
}
catch (e) {
   console.log(e)
}

try{
    console.log("hello")
    data = document.getElementById("id_save_until").value
    let day, month, year = data.split('.')
    console.log(year, month, day)
    document.getElementById("id_save_until").setFullYear(year, month, day)

} catch (e) {
   console.log(e)
}

