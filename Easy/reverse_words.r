args <- commandArgs(trailingOnly=TRUE)
test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		test <- strsplit(test, " ")[[1]]
		paste(rev(test), collapse = " ")
	}
}), sep = "\n")