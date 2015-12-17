test.cases <- c("5;7 -3 -10 4 2 8 -2 4 -5 -2",
				"6;-4 3 -10 5 3 -7 -3 7 -6 3",
				"3;-7 0 -45 34 -24 7")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		test <- strsplit(test, ";")[[1]]
		r <- as.numeric(test[1])
		nums <- as.numeric(strsplit(test[2], " ")[[1]])
		M <- min(nums)
		i <- 1
		while (i < length(nums) - r + 2) {
			s <- sum(nums[i:(i+r-1)])
			if (s > M) {
				M <- s
			}
			i <- i + 1
		}
		if (M < 0) {
			0
		} else {
			M
		}
	}
}), sep = "\n")