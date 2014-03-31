use <baseplate-parts.scad>;
use <raspi.scad>;
use <RB-65PG.scad>;

translate([90,-150,0])
	baseplatefromparts();
translate([90,-150,-55])
	baseplatefrompartsbottom();
translate([-28,-42.5,10])
	raspi();
translate([-60,-10,-50])
	rotate([0,0,90])
		rb65pg();