test.cases <- c("(--9Hello----World...--)", "Can 0$9 ---you~", "13What213are;11you-123+138doing7")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		words_with_spaces <- gsub("[^[:alpha:]]", " ", test)
		just_words <- gsub("^ *|(?<= ) | *$", "", words_with_spaces, perl = TRUE)
		lower_words <- tolower(just_words)
	}
}), sep = "\n")