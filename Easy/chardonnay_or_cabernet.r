test.cases <- c("Cabernet Merlot Noir | ot", "Chardonnay Sauvignon | ann", "Shiraz Grenache | o")

char_counter <- function(char, string) {
	s <- gsub(char, "" , string)
	nchar(string) - nchar(s)
}

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		test <- strsplit(test, split = " | ", fixed = TRUE)[[1]]
		wines <- strsplit(test[1], " ")[[1]]
		pattern <- test[2]
		characters <- strsplit(test[2], "")[[1]]
		Result <- c()
		for (x in wines){
			t <- TRUE
			for (c in characters) {
				if (char_counter(c, pattern) <= char_counter(c, x)) {
					t <- TRUE
				}else{
					t <- FALSE
					break
				}
			}
			if (t == TRUE){
				Result <- c(Result, x)
			}
		}
		if (length(Result) == 0) {
			Result <- "False"
		} else {
			Result <- paste(Result, sep = " ", collapse = " ")
		}
		Result
	}
}), sep = "\n")