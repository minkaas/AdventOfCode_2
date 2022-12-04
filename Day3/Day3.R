letter_to_number <- function(letter) {
  return_value <- match(tolower(letter), letters[1:26])
  if (letter == toupper(letter)) {
    return_value <- return_value + 26
  }
  return_value
}

input <- readLines("input")
i <- 0
priorityone <- 0
prioritytwo <- 0
threesacks <- vector()
allsacks <- vector()
for (rucksack in input) {
  threesacks <- append(threesacks, rucksack)
  i <- i + 1
  if (i > 2) {
    one <- unique(strsplit(threesacks[1], "")[[1]])
    two <- unique(strsplit(threesacks[2], "")[[1]])
    three <- unique(strsplit(threesacks[3], "")[[1]])
    allsacks <- append(allsacks, intersect(intersect(one, two), three))
    threesacks <- vector()
    i <- 0
  }
  length <- nchar(rucksack)
  firstcomp <- unique(strsplit(substr(rucksack, 0, length/2), "")[[1]])
  sexcomp <- unique(strsplit(substr(rucksack, length/2+1, length), "")[[1]])
  priority <- intersect(firstcomp, sexcomp)[[1]]
  priorityone <- priorityone + letter_to_number(priority)
}
for (priorities in allsacks) {
  prioritytwo <- prioritytwo + letter_to_number(priorities)
}

print(priorityone)   # Part 1
print(prioritytwo)   # Part 2


