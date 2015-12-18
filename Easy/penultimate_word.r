test.cases <- c("some line with text",
				"another line")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		words <- strsplit(test, " ")[[1]]
		words[length(words)-1]
	}
}), sep = "\n")