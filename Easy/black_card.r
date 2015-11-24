cat(sapply(strsplit(readLines(tail(commandArgs(), n=1)), " | ", fixed=TRUE), function(s) {
	Names <- as.list(strsplit(s[1], " ")[[1]])
	idx <- as.integer(s[2])
	while(length(Names) > 1) {
		n <- idx %% length(Names)
		Names[[ifelse(n > 0, n, length(Names))]] <- NULL
	}
	Names[[1]]
}), sep="\n")