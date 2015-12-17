test.cases <- c("a b c d",
				"a b c d e f g h i j k l m n o p",
				"a b c d e f g h i")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		L <- strsplit(test, " ")[[1]]
		len <- sqrt(length(L))
		Matrix <- matrix(L, len, len, byrow = TRUE)
		Matrix <- t(Matrix)[ , ncol(Matrix):1]
		M <- c(t(Matrix))
		paste(M, sep = " ", collapse = " ")
	}
}), sep = "\n")