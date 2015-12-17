test.cases <- c("thisTHIS", "AAbbCCDDEE",
				"N", "UkJ")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		words <- strsplit(test, "")[[1]]
		whole = length(words)
		lower_part = length(words[words %in% letters])
		upper_part = length(words[words %in% LETTERS])
		L = format(round((lower_part / whole)*100, digits = 2), nsmall = 2)
		U = format(round((upper_part / whole)*100, digits = 2), nsmall = 2)
		paste(c("lowercase:", L, "uppercase:", U), sep = " ", collapse = " ")
	}
}), sep = "\n")