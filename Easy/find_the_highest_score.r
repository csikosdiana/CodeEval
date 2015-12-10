test.cases <- c("72 64 150 | 100 18 33 | 13 250 -6",
				"10 25 -30 44 | 5 16 70 8 | 13 1 31 12",
				"100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		rows <- strsplit(test, " | ", fixed = TRUE)[[1]]
		M <- c()
		for (r in rows){
			r <- as.numeric(strsplit(r, split = " ")[[1]])
			M <- rbind(M, r)
		}
		Maxi <- as.character(apply(M, 2, max))
		paste(Maxi, sep = " ", collapse = " ")
	}
}), sep = "\n")