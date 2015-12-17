test.cases <- c("some line with text", "another line")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		words <- strsplit(test, " ")[[1]]
		len <- words
		len <- sapply(len, function(x) {nchar(x)})
		M <- max(len)
		names(len[len == M])[1]
	}
}), sep = "\n")