def readFileToListOfInts(filename: String): Seq[Int] = {
  val bufferedSource = io.Source.fromFile(filename)
  val lines = (for (line <- bufferedSource.getLines()) yield line.toInt).toList
  bufferedSource.close
  lines
}

def countOfBiggerItems(l: Seq[Int]): Int = {
  val result = l.sliding(2)
    .filter( t => t.length > 1 && t(0) < t(1))
    .toList :+ l.last
  result.length

}
val lines = readFileToListOfInts("/Users/ben/git/advent_of_code/2021/1/input")
println(countOfBiggerItems(lines))