test.cases <- c("20,6", "2,3")

modulo <- function(N, M) {
			k <- floor(N/M)
			return(N - M*k)
}

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		nums <- as.numeric(strsplit(test, ",")[[1]])
		N <- nums[1]
		M <- nums[2]
		modulo(N, M)
	}
}), sep = "\n")