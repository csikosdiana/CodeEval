test.cases <- c(".- ...- ..--- .-- .... .. . -.-. -..-  ....- .....",
				"-... .... ...--")

morse_code <- c('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', 
			'--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', 
			'-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', 
			'---..', '----.')
names(morse_code) <- c(LETTERS, as.character(c(0:9)))

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		words <- strsplit(test, "  ")[[1]]
		result <- c()
		for (j in words) {
			Code <- strsplit(j, " ")[[1]]
			decoded <- c()
			for (i in Code){
				new_char <- names(morse_code)[morse_code == i]
				decoded <- c(decoded, new_char)
			}
			result <- c(result, paste(decoded, sep = "", collapse = ""))
		}
		paste(result, sep = " ", collapse = " ")
	}
}), sep = "\n")
