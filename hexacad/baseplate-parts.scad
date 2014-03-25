use <baseplate.scad>;

module baseplatethird()
{
	intersection()
	{
	baseplate();
	translate([-200,0,-5])
	cube([250,100,20]);
	}
}

baseplatethird();
translate([0,100,0])
baseplatethird();
translate([0,200,0])
baseplatethird();