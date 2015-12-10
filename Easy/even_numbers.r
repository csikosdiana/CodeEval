test.cases <- c("701", "4123", "2936")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		num <- as.numeric(test)
		even <- 0
		if (num %% 2 == 0){
			even <- 1
		}
		even
	}
}), sep = "\n")