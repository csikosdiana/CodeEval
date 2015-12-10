test.cases <- c("14:01:57 12:47:11", "13:09:42 22:16:15",
				"08:08:06 08:38:28", "23:35:07 02:49:59",
				"14:31:45 14:46:56")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		times <- strsplit(test, " ")[[1]]
		time_1 <- strptime(times[1], format = "%H:%M:%S")
		time_2 <- strptime(times[2], format = "%H:%M:%S")
		delta <- as.integer(abs(difftime(time_1, time_2, units = "sec")))
		H = as.character(floor(delta / 3600))
		m = as.character(floor((delta %% 3600) / 60))
		s = as.character(((delta %% 3600) %% 60))
		D <- paste(c(H, m, s), sep = " ", collapse = ":")
		only_time <- format(strptime(D, format="%H:%M:%S"), format="%H:%M:%S")
		only_time
	}
}), sep = "\n")