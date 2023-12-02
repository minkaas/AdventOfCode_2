input <- readLines("input")
shapeyouselected <- 0
winyouselected <- 0
for (match in input) {
  moves <- strsplit(match, " ")[[1]]
  opponent <- moves[1]
  you <- moves[2]
  if (opponent == "A") {                               # Rock
    if (you == "X") {                                  # Rock or lose
      shapeyouselected <- shapeyouselected + 1 + 3
      winyouselected <- winyouselected + 0 + 3
    } else if (you == "Y") {                           # Paper or draw
      shapeyouselected <- shapeyouselected + 2 + 6
      winyouselected <- winyouselected + 3 + 1
    } else {
      shapeyouselected <- shapeyouselected + 3 + 0     # Scissors or win
      winyouselected <- winyouselected + 6 + 2
    }                     
  } else if (opponent == "B") {                        # Paper
    if (you == "X") {                                  # Rock or lose
      shapeyouselected <- shapeyouselected + 1 + 0
      winyouselected <- winyouselected + 0 + 1
    } else if (you == "Y") {                           # Paper or draw
      shapeyouselected <- shapeyouselected + 2 + 3
      winyouselected <- winyouselected + 3 + 2
    } else {
      shapeyouselected <- shapeyouselected + 3 + 6     # Scissors or win
      winyouselected <- winyouselected + 6 + 3
    }  
  } else {                                             # Scissors
    if (you == "X") {                                  # Rock or lose
      shapeyouselected <- shapeyouselected + 1 + 6
      winyouselected <- winyouselected + 0 + 2
    } else if (you == "Y") {                           # Paper or draw
      shapeyouselected <- shapeyouselected + 2 + 0
      winyouselected <- winyouselected + 3 + 3
    } else {
      shapeyouselected <- shapeyouselected + 3 + 3     # Scissors or win
      winyouselected <- winyouselected + 6 + 1
    }  
  }
}
print(shapeyouselected)
print(winyouselected)
