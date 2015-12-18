test.cases <- c("#########_##",
				"########C_##",
				"#######_####",
				"######_#C###",
				"#######_C###",
				"#######_####",
				"######C#_###",
				"######C_####",
				"#######_####",
				"#######_####")


#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
position <- 0
for (test in test.cases) {
	way <- strsplit(test, "")[[1]]
	if (position == 0) {
		if ("C" %in% way) {
			i <- which(way == "C")
		} else {
			i <- which(way == "_")
		}
		position <- i
		way[i] <- "|"
		cat(paste(way, sep = "", collapse = ""), "\n")
		
	} else {
		if ("C" %in% way) {
			i <- which(way == "C")
			
		} else {
			i <- which(way == "_")
		}
		
		if (i < position) {
			way[i] <- "/"
			cat(paste(way, sep = "", collapse = ""), "\n")
		}
		else if (i == position) {
			way[i] <- "|"
			cat(paste(way, sep = "", collapse = ""), "\n")
		} else {
			way[i] <- "\\"
			cat(paste(way, sep = "", collapse = ""), "\n")
		}
		position <- i
	}
}