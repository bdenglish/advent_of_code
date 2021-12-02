package Year2021

object Day2 {
  def main(args: Array[String]): Unit = {
    def readFileToListOfStrings(year: Int, day: Int): List[List[String]] = {
      val base_dir = scala.util.Properties.envOrElse("ADVENT_OF_CODE_BASE", "undefined")
      val bufferedSource = io.Source.fromFile(s"$base_dir/input/$year/$day/input")
      val lines = (for (line <- bufferedSource.getLines()) yield line.split(" ").toList).toList
      bufferedSource.close
      lines
    }

    def move(cmds: List[String]): List[Int] = {
      if(cmds(0) == "forward"){
        List(0, cmds(1).toInt)
      } else if(cmds(0) == "down"){
        List(cmds(1).toInt, 0)
      } else if(cmds(0) == "up"){
        List(cmds(1).toInt * -1, 0)
      } else {
        List(0, 0)
      }
    }

    val lines = readFileToListOfStrings(2021, 2)
    val positions = lines.map(move).transpose.map(_.sum)
    println(positions(0) * positions(1))

    var h = 0
    var d = 0
    var aim = 0
    for (cmds <- lines) {
      if(cmds(0) == "forward"){
        h = h + cmds(1).toInt
        d = d + cmds(1).toInt * aim
      } else if(cmds(0) == "down"){
        aim = aim + cmds(1).toInt
      } else if(cmds(0) == "up"){
        aim = aim - cmds(1).toInt
      }
    }
    println(h * d)
  }
}
