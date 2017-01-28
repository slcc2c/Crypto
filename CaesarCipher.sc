def shiftLetter(letter: Char, shift: Int) = {
  val letter_shifted:Int = ((((letter.toInt) % 97) + shift) % 26)+97
  letter_shifted.toChar
}

def encrypt(word: String, key: Int) = {
  val output = for (c <- word) yield shiftLetter(c,key)
  output
}

def decrypt(word: String, key: Int) = {
  val output = for (c <- word) yield shiftLetter(c, key)
  output
}

