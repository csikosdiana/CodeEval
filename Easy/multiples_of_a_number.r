test.cases <- c("13,8", "17,16")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		nums <- as.numeric(strsplit(test, ",")[[1]])
		x <- nums[1]
		n <- nums[2]
		if (n >= x) {
			n*2
		} else {
			m <- ceiling(x/n)
			n*m
		}
	}
}), sep = "\n")