
<<<<<<< HEAD
	subroutine SLHARead( error, slhadata, filename, abort )
	integer error, abort 
	double precision slhadata(*)
	character *(*) filename
	character (1000) temp

	print *, filename
	print *, filename


	open(unit=1,file=filename)
	do i = 1, 1
        read(1,'(A)',iostat=ios) temp
        print *, temp
	enddo
=======
	subroutine SLHARead( error, sd, filename, abort )
	integer error, abort
	character*(*) filename
	double precision sd(*)
	print *, sd(1)
	print *, filename
>>>>>>> 617e607813e3666ef2e206307cc6c86638225fc7
	end
