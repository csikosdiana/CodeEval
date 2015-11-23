test.cases <- c("ABbCcc", "Good luck in the Facebook Hacker Cup this year!", "Ignore punctuation, please :)",
				"Sometimes test cases are hard to make up.", "So I just go consult Professor Dalves")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		string1 <- tolower(c(test))
		string1 <- gsub("[^a-z]", "", string1)
		string <- paste(sort(strsplit(string1, split = "")[[1]], decreasing = TRUE), collapse = "")
		string <- gsub("([A-Za-z])\\1+","\\1", string)
		string <- strsplit(string, split = "")
		Counts <- c()
		k <- 26
		for (l in string[[1]]){
			s <- gsub(l,"",string1)
			occurrence <- nchar(string1) - nchar(s)
			Counts <- c(Counts, occurrence)
			k <- k - 1
		}
		Counts <- sort(Counts, decreasing = TRUE)
		Beauty <- 0
		k <- 26
		for (i in Counts){
			Beauty <- Beauty + k*i
			k <- k - 1
		}
		Beauty
	}
}), sep = "\n")