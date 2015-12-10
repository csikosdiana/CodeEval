test.cases <- c("5", "12")

fib <- function(x){
			if (x == 0 | x == 1){
				x
			} else {
				fib(x - 1) + fib(x - 2)
			}
}

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		num <- as.numeric(test)
		fib(num)
	}
}), sep = "\n")