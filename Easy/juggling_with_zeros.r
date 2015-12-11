test.cases <- c("00 0 0 00 00 0",
				"00 0",
				"00 0 0 000 00 0000000 0 000",
				"0 000000000 00 00",
				"00 00000 0 0 00 00 0 0 00 00 0 0 00 00000 0 00 00 0000 0 00 00 0 0 0 00 00 0 0 00 00")

binary_to_dec <- function(x) {
					vec <- strsplit(x, "")[[1]]
					vec <- rev(vec)
					dec <- 0
					for (i in 1: length(vec)) {
						if (vec[i] == "1") {
							dec <- dec + 2^(i-1)
						}
					}
					dec
}

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		zeros <- strsplit(test, " ")[[1]]
		binary <- c()
		for (i in seq(1, length(zeros), 2)) {
			if (zeros[i] == "00") {
				l = nchar(zeros[i+1])
				new <- paste(rep("1", l), sep = "", collapse = "")
				binary <- c(binary, new)
			} else {
				binary <- c(binary, zeros[i+1])
			}
		}
		binary <- paste(binary, sep = "", collapse = "")
		binary_to_dec(binary)
	}
}), sep = "\n")