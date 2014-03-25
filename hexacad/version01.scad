use <baseplate.scad>;
use <raspi.scad>;
use <RB-65PG.scad>;

translate([90,-150,0])
	baseplate();
translate([-28,-42.5,10])
	raspi();
translate([-10,-10,-40])
	rotate([0,0,90])
		rb65pg();