Matrix <- c()
for (i in 1:12) {
	Matrix <- rbind(Matrix, seq(i, i*12, i))
}

write.table(format(Matrix, justify="right"), row.names=F, col.names=F, quote=F)