	 program test
 
 
         integer :: jmax,tstpi,j
         real*8 :: tlo, thi, tsav, tj, tstp
 
         jmax = 20
 
         tlo   = 3.00
         thi   = 13.0
         tstp  = (thi - tlo)/(jmax-1)
         write(*,*) tstp
         tstpi = 1.0d0/tstp
 
 
          do j=1,jmax
          tsav = tlo + (j-1)*tstp
          tj = 10.0d0**(tsav)
          write(*,*) tsav, tj
 
          enddo
 
          stop
          end
