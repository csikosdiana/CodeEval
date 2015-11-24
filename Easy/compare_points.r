test.cases <- c("0 0 1 5", "12 13 12 13", "0 1 0 5")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		nums <- strsplit(test, split = " ")[[1]]
		N <- as.numeric(nums)
		R <- NULL
		if ((N[3] - N[1] == 0) & (N[4] - N[2] == 0)) {
			R <- "here"
		}
		else if (N[3] - N[1] == 0) {
			if (N[4] - N[2] > 0) {
				R <- "N"
			}else {
				R <- "S"
			}
		}
		else if (N[4] - N[2] == 0) {
			if (N[3] - N[1] > 0) {
				R <- "E"
			}else {
				R <- "W"
			}
		}
		else if ((N[3] - N[1] > 0) & (N[4] - N[2] > 0)) {
			R <- "NE"
		}
		else if ((N[3] - N[1] < 0) & (N[4] - N[2] > 0)) {
			R <- "NW"
		}
		else if ((N[3] - N[1] < 0) & (N[4] - N[2] < 0)) {
			R <- "SW"
		}else {
			R <- "SE"
		}
		R
	}
}), sep = "\n")