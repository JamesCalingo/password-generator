const generatePassword = (length) => {

  // if(typeof(length) !== Number) {
  //   console.log("Please use a number for your length!")
  //   return
  // }
let password = ''
let charStr = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&'
let addChar = () => {
  const random = Math.floor(Math.random() * charStr.length)
  password += charStr[random]
}
for(let i = 0; i < length; i++) {
  addChar()
if(password[i] === password[i - 1]) {
  password = password.slice(0, -1)
  addChar()
}
}
return password
}

module.exports = generatePassword

console.log(generatePassword())
