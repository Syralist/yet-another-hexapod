use <baseplate.scad>;
use <raspi.scad>;
use <RB-65PG.scad>;

translate([45,-75,0])
baseplate();
translate([-28,-42.5,10])
raspi();