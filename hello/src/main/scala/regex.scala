package hello.regex_ex

def t1 =
  val os_release_info = """PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/""""

  val lines = os_release_info.split("\n").map { x =>
    val regex = raw"([A-Z_]+)=\"?([0-9a-zA-Z:/\. ]*)\"?".r
    val m = regex.findFirstMatchIn(x).get
    (m.group(1), m.group(2))
  }
  def parse_os_release(lines: String) =
    val regex = raw"([A-Z_]+)=\"?([0-9a-zA-Z:/\. ]*)\"?".r
    for m <- "([A-Z_]+)=\"*([.*])\"*".r.findAllMatchIn(lines) do
      println(s"${m.group(1)}, ${m.group(2)}")

  val regex = raw"([A-Z_]+)=\"?([0-9a-zA-Z:/\. ]*)\"?".r
  val b = regex.findFirstMatchIn("VERSION_ID=\"11\"")


  val regex = raw"([A-Z_]+)=\"?([0-9a-zA-Z:/\. ]*)\"?".r
  val b = regex.findFirstMatchIn("ffffVERSION_ID=\"11\"")

  val keyValPattern = "([0-9a-zA-Z- ]+): ([0-9a-zA-Z-#()/. ]+)".r
  val m = keyValPattern.findFirstMatchIn("background-color: #A03300;")

  val target_string = "The price of PINEAPPLE ice cream is 20"
  val m2=raw"(\b[A-Z]+\b)".r.findFirstMatchIn(target_string)


  val m=raw".+".r.findFirstMatchIn(".  ")
  val target_string = "The price of PINEAPPLE ice cream is 20"
  val m2=raw"(\b[A-Z]+\b)\.+(\b[0-9]+)".r.findFirstMatchIn(target_string)
def t2=
  "[0-9]".r.findFirstMatchIn("awesomepassword") match {
  case Some(_) => println("Password OK")
  case None => println("Password must contain a number")
}
