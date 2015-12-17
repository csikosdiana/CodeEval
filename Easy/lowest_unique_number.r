test.cases <- c("3 3 9 1 6 5 8 1 5 3",
				"9 2 9 9 1 8 8 8 2 1 1")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		nums <- strsplit(test, " ")[[1]]
		T <- table(nums)
		L <- as.vector(T)
		N <- names(T)
		result <- N[L == 1]
		if (length(result) == 0) {
			0
		} else {
			result <- as.numeric(result)
			R <- as.character(min(result))
			which(nums == R)
		}
	}
}), sep = "\n")