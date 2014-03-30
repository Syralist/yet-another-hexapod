use <baseplate-parts.scad>;
use <raspi.scad>;
use <RB-65PG.scad>;

translate([90,-150,0])
	baseplatefromparts();
translate([90,-150,-55])
	baseplatefromparts();
translate([-28,-42.5,10])
	raspi();
translate([-55,-10,-47])
	rotate([0,0,90])
		rb65pg();