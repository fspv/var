set terminal pngcairo transparent enhanced font "arial,10" fontscale 1.0 size 500,500
set zeroaxis

k = 0.5
b = 1
x = x + 0.1
y = k * x + b
graph_title = sprintf("y=kx+b, k=%0.1f, b=%0.1f", k, b)
point_title = sprintf("x=%0.1f, y=%0.1f*%0.1f+%0.1f=%0.2f", x, k, x, b, y)
right = 10
bottom = -1
top = 10

if(!exists("left")) {
    left = x
}
set parametric
system('mkdir -p animation')
outfile = sprintf('animation/sline%0.1f.png', x + 100)
set output outfile
plot [left:x] [left:right] [bottom:top] \
        t, k * t + b lw 3 title graph_title, \
        x, y with points pointtype 7 title point_title
if(x<end_time) reread;

