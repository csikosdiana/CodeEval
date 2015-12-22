test.cases <- c("Hello World,r",
				"Hello CodeEval,E")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		parts <- strsplit(test, ",")[[1]]
		S <- strsplit(parts[1], "")[[1]]
		x <- parts[2]
		idx <- which(S == x)
		if (length(idx) == 0) {
			-1
		} else {
			max(idx) - 1
		}
	}
}), sep = "\n")