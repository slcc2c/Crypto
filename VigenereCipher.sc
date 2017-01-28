def shiftLetter(letter: Char, shift: Char) = {
  val letter_shifted:Int = ((((letter.toInt) % 97) + (shift.toInt)%97) % 26)+97
  letter_shifted.toChar
}

def encrypt(word: String, key: Char) = {
  val output = for (c <- word) yield shiftLetter(c,key)
  output
}

def decrypt(word: String, key: Char) = {
  val output = for (c <- word) yield shiftLetter(c, key)
  output
}