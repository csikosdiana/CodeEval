args <- commandArgs(trailingOnly=TRUE)
test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		test <- gsub("[^- 0123456789]", "", test)
		test <- strsplit(test, " ")[[1]]
		test <- sapply(test, as.integer)
		x <- test[1] - test[3]
		y <- test[2] - test[4]
		as.integer(sqrt(x*x + y*y))
	}
}), sep = "\n")
