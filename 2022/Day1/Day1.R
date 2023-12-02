input <- readLines("input")
input <- as.numeric(input)
caloriesums <- vector()
tempsums <- vector()
for (calories in input) {
  if (is.na(calories)) {
    caloriesums <- append(caloriesums, sum(tempsums))
    tempsums <- vector()
  } else {
    tempsums <- append(tempsums, calories)
  }
}
part1 <- head(sort(caloriesums, decreasing = TRUE), n=1)
part2 <- sum(head(sort(caloriesums, decreasing = TRUE), n=3))
print(part1)
print(part2)
