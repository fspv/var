set terminal pngcairo transparent enhanced font "arial,10" fontscale 1.0 size 500,500
set zeroaxis

a = 1
k = 1
r(t) = a * cos(k * t)**2
phi_grad = phi / pi * 180
graph_title = sprintf("r=a cos(k*phi), a=%0.1f, k=%0.1f", a, k)
point_title = sprintf("phi=%0.1f, r=%0.1f*cos(%0.1f*%0.1f)^2=%0.2f", phi_grad, a, k, phi_grad, r(phi))
left = -1.5
right = 1.5
bottom = -1.5
top = 1.5

set parametric
system('mkdir -p animation')
outfile = sprintf('animation/rose2%0.1f.png', phi + 100)
set output outfile
set termoption dash
set for [i=1:5] linetype i lt i
set style line 1 lt 2 lc rgb "red" lw 2
set style line 2 lt 2 lc rgb "blue" lw 2
set style line 3 lt 1 lc rgb "black" lw 3
set samples 1024
plot [0:phi] [left:right] [bottom:top] \
        r(t) * cos(t), r(t) * sin(t) ls 3 title graph_title, \
        r(phi) * cos(phi), r(phi) * sin(phi) with points pointtype 7 lw 3 title point_title, \
        t * cos(phi) * 1000, t * sin(phi) * 1000 ls 1 title '', \
        - t * cos(phi) * 1000, - t * sin(phi) * 1000 ls 2 title ''

phi = phi + pi / 48
if(phi<end_time) reread;
