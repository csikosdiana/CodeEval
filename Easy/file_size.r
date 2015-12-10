my_file <- commandArgs(trailingOnly = TRUE)
cat(file.info(my_file)$size, sep="\n")