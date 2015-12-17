test.cases <- c("9 0 6 | 15 14 9",
				"5 | 8",
				"13 4 15 1 15 5 | 1 4 15 14 8 2")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		lists <- strsplit(test, split = "| ", fixed = TRUE)[[1]]
		L1 <- as.numeric(strsplit(lists[1], split = " ")[[1]])
		L2 <- as.numeric(strsplit(lists[2], split = " ")[[1]])
		paste(as.character(L1*L2), sep = " ", collapse = " ")
	}
}), sep = "\n")