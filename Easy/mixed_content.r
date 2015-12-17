test.cases <- c("8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21",
					"24,13,14,43,41")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		words <- strsplit(test, ",")[[1]]
		T <- grep("[[:lower:]]", words, value=T)
		nums <- words[! words %in% T]
		P1 <- paste(T, sep = ",", collapse = ",")
		P2 <- paste(nums, sep = ",", collapse = ",")
		if (length(T) == 0) {
			P2
		}
		else if (length(nums) == 0) {
			P1
		} else {
			paste(c(P1, P2), sep = "|", collapse = "|")
		}
	}
}), sep = "\n")