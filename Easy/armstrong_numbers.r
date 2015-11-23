test.cases <- c("6", "153", "351")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		len <- nchar(test)
		nums <- strsplit(test, split = "")
		A <- as.integer(nums[[1]])
		S <- sum(sapply(A, function(x){x^len}))
		if (S == as.integer(test)){
			"True"
		}else{
			"False"
		}
	}
}), sep = "\n")