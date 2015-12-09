test.cases <- c("40 40 40 40 29 29 29 29 29 29 29 29 57 57 92 92 92 92 92 86 86 86 86 86 86 86 86 86 86",
				"73 73 73 73 41 41 41 41 41 41 41 41 41 41",
				"1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2",
				"7")
				
stat_fv <- function(x, y){
	S <- c()
	l <- length(x)
	for (i in 1:l){
		S <- c(S, c(x[i]))
		S <- c(S, c(y[i]))
	}
	S
}


#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		nums <- strsplit(test, split = " ")[[1]]
		N <- as.numeric(nums)
		r <- rle(N)
		x <- r$lengths
		y <- r$values
		Result <- as.character(stat_fv(x, y))
		paste(Result, sep = " ", collapse = " ")
	}
}), sep = "\n")