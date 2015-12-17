test.cases <- c("330.39991833", "0.001",
				"14.64530319", "0.25",
				"254.16991217")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		angle <- as.numeric(test)
		whole <- floor(angle)
		frac_1 <- floor((angle - whole)*60)
		frac_2 <- floor((((angle - whole) * 60) - frac_1) * 60)
		D <- as.character(whole)
		M <- as.character(frac_1)
		if (nchar(M) == 1) {
			M <- paste(c("0", M), sep = "", collapse = "")
		}
		S <- as.character(frac_2)
		if (nchar(S) == 1) {
			S <- paste(c("0", S), sep = "", collapse = "")
		}
		paste(c(D, ".", M, "'", S, '"'), sep = "", collapse = "")
	}
}), sep = "\n")