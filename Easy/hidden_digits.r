test.cases <- c("abcdefghik", "Xa,}A#5N}{xOBwYBHIlH,#W",
				"(ABW>'yy^'M{X-K}q,", "6240488")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
nums <- as.character(c(0:9))
names(nums) <- letters[1:10]
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		chars <- strsplit(test, "")[[1]]
		chars <- chars[chars %in% names(nums) | chars %in% as.character(c(0:9))]
		result <- c()
		for (ch in chars) {
			if (ch %in% names(nums)) {
				ch <- nums[[ch]]
				result <- c(result, ch)
			} else {
				result <- c(result, ch)
			}
		}
		if (length(result) == 0) {
			"NONE"
		} else {
			paste(result, sep = "", collapse = "")
		}
	}
}), sep = "\n")