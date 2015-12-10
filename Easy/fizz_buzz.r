test.cases <- c("3 5 10",
				"2 7 15")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		nums <- as.numeric(strsplit(test, " ")[[1]])
		vec <- c(1:nums[3])
		fizz_buzz <- c()
		fb <- vec[vec %% nums[1] == 0 & vec %% nums[2] == 0]
		if (length(fb) != 0) {
			fizz_buzz[fb] <- "FB"
		}
		f <- vec[vec %% nums[1] == 0 & vec %% nums[2] != 0]
		if (length(f) != 0) {
			fizz_buzz[f] <- "F"
		}
		b <- vec[vec %% nums[1] != 0 & vec %% nums[2] == 0]
		if (length(b) != 0) {
			fizz_buzz[b] <- "B"
		}
		e <- vec[vec %% nums[1] != 0 & vec %% nums[2] != 0]
		if (length(e) != 0) {
			fizz_buzz[e] <- as.character(vec[e])
		}
		paste(fizz_buzz, sep = " ", collapse = " ")
	}
}), sep = "\n")