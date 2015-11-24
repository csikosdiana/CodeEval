test.cases <- c("Hello world", "javaScript language",
				"a letter", "1st thing")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		words <- strsplit(test, " ")[[1]]
		words <- sapply(words, function(s){paste(toupper(substring(s, 1, 1)), substring(s, 2), sep = "", collapse = "")})
		paste(words, sep = " ", collapse = " ")
	}
}), sep = "\n")