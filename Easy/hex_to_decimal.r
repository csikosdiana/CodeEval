test.cases <- c("9f", "11")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		hex <- strsplit(test, split = "")[[1]]
		hex <- rev(hex)
		nums <- as.character(c(10:15))
		names(nums) <- letters[1:6]
		dec <- 0
		for (i in 1:length(hex)){
			if (hex[i] %in% names(nums)){
				k <- nums[[hex[i]]]
				dec <- dec + as.numeric(k)*16^(i-1)
			} else {
				dec <- dec + as.numeric(hex[i])*16^(i-1)
			}
		}
		dec
	}
}), sep = "\n")