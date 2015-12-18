test.cases = c("Tom exhibited.",
		"Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look.",
		"Tom was tugging at a button-hole and looking sheepish.",
		"Two thousand verses is a great many - very, very great many.",
		"Tom's mouth watered for the apple, but he stuck to his work.",
		"123456789A 23456 89B123456789C123456789D123456789E123456789F123456789G",
		"123456789A123456789B123456789C123456789D123456789E1234 6")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		if (nchar(test) <= 55) {
			test
		} else {
			s <- substr(test, 1, 40)
			i <- max(gregexpr(pattern = " ",s)[[1]])
			if (i == -1) {
				paste(c(s, "... <Read More>"), sep = "", collapse = "")
			} else {
				s <- substr(s, 1, i-1)
				paste(c(s, "... <Read More>"), sep = "", collapse = "")
			}
		}
	}
}), sep = "\n")