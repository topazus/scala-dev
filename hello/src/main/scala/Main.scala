
@main def hello: Unit =
  println("hello")

def t1 =
  import java.nio.file.Files
  import java.nio.file.Paths
  import scala.util.Random
  val a =
    scala.io.Source.fromFile("/workspaces/scala-dev/debian.txt").getLines.toList

  val b =
    a.map(x => if x.startsWith("# deb-src") then x.stripPrefix("# ") else x)
  // write to file
  Files.writeString(
    Paths.get("/workspaces/scala-dev/debian-mod.txt"),
    b.mkString("\n")
  )

def write_files=
  val file_name="/tmp/1.txt"

//java.io.PrintWriter
  val f=java.io.PrintWriter(java.io.File(file_name))
  f.write("hello")
  f.close()

  //java.io.FileWriter
  val f2=java.io.FileWriter(java.io.File(file_name))
  val text = "We are learning Scala programming language"
  f2.write(text)
  f2.close()

  // java.nio
  import java.nio.file.Files
  //import java.nio.charset.StandardCharsets
  val f3=Files.write(java.nio.file.Paths.get(file_name),text.getBytes)
