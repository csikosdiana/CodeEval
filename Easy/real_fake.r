test.cases <- c("9999 9999 9999 9999",
				"9999 9999 9999 9993")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		card <- gsub(" ", "", test)
		card <- strsplit(card, split = "")[[1]]
		card <- as.numeric(card)
		double_nums <- sum(card[seq(1,16,2)] * 2)
		single_nums <- sum(card[seq(2,16,2)])
		Valid <- double_nums + single_nums
		if (Valid %% 10 == 0) {
			"Real"
		} else {
			"Fake"
		}
	}
}), sep = "\n")