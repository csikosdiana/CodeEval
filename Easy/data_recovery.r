test.cases <- c("2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2",
					"programming first The language;3 2 1",
					"programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9",
					"It until Remington was at for I 1959 during 1955 period Rand UNIVAC the from developed the;1 16 9 2 8 4 7 17 11 15 13 10 6 12 14 3")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		parts <- strsplit(test, ";")[[1]]
		unrec <- strsplit(parts[1], " ")[[1]]
		code <- as.numeric(strsplit(parts[2], " ")[[1]])
		l <- length(unrec)
		vec <- c(1:l)
		diff_vec <- vec[!(vec %in% code)]
		rec <- vector(length = l)
		rec[code] <- unrec[c(1:(l-1))]
		diff_word <- unrec[!(unrec %in% rec)]
		if (length(diff_word) == 0){
			rec[diff_vec] <- unrec[l]
		} else {
			rec[diff_vec] <- diff_word
		}
		paste(rec, sep = " ", collapse = " ")
	}
}), sep = "\n")