reset;
plot "e.dat" u 1:2 w l title "Ep"; 
replot "e.dat" u 1:3 w l title "Ec"; 
replot "e.dat" u 1:4 w l title "Et";
set xlabel "t"
replot