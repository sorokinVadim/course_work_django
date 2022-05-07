const now = new Date()
now.setTime(now.getTime() + 3 * 60 * 60 * 1000)

const dateField = document.getElementById("id_save_until")
const addZero = (num) => num < 9 ? "0" + num : num
const nowDate = `${now.getFullYear()}-${addZero(now.getMonth() + 1)}-${addZero(now.getDay() + 1)}`
dateField.min = nowDate
console.log(dateField.min)
