package Year2021

object Day1 {
  def main(args: Array[String]): Unit = {
    def readFileToListOfInts(filename: String): Seq[Int] = {
      val bufferedSource = io.Source.fromFile(filename)
      val lines = (for (line <- bufferedSource.getLines()) yield line.toInt).toList
      bufferedSource.close
      lines
    }

    def countOfBiggerItems(l: Seq[Int], window: Int): Int = {
      l.sliding(window + 1)
        .filter(t => t.length > window && t(0) < t(window))
        .toList.length
    }

    val lines = readFileToListOfInts("/Users/ben/git/advent_of_code/input/2021/1/input")
    println(countOfBiggerItems(lines, 1))
    println(countOfBiggerItems(lines, 3))
  }
}
