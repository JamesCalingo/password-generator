const generatePassword = require("./password");

test("generates a password of length num", () => {
  expect(generatePassword(15).length).toBe(15);
});
