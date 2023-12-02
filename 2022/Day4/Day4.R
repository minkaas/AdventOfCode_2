input <- readLines("input")
fullycontained <- 0
partlycontained <- 0
for (assignments in input) {
  asses <- strsplit(assignments, ",")[[1]]
  ass <- strsplit(asses[1], "-")[[1]]
  one <- as.numeric(ass[1])
  two <- as.numeric(ass[2])
  ign <- strsplit(asses[2], "-")[[1]]
  three <- as.numeric(ign[1])
  four <- as.numeric(ign[2])
  if ((one >= three && four >= two) || (one <= three && four <= two)) {
    fullycontained <- fullycontained + 1
  }
  if ((max(one, three) <= min(two, four))) {
    partlycontained <- partlycontained + 1
  } 
}
print(fullycontained)
print(partlycontained)
