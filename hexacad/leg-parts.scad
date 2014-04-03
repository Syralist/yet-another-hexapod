use <small-parts.scad>

module shoulder()
{
	width = 40;
	length = 80;
	wall = 5;
	radiusaxle = 8.7/2;
	radiuswheel = 20.7/2;
	heightwheel = 2.5;
	compwidth = 26;
	compheight = 20;
	compwall = 8;
	servowidth = 41;
	difference()
	{
		union()
		{
			cylinder(r=width/2,h=wall);
			translate([0,-width/2,0])
				cube([length, width, wall]);
		}
		cylinder(r=radiusaxle,h=wall);
		translate([0,0,heightwheel])
			cylinder(r=radiuswheel,h=wall);
	}
	union()
	{
		//translate([length-compwall,-width/2,-compheight])
			//cube([compwall,compwidth,compheight]);
		translate([length-2*compwall-servowidth,-width/2,-compheight])
			cube([compwall,compwidth,compheight]);
		translate([length-2*compwall-servowidth,-width/2,-compheight-wall])
			cube([servowidth+2*compwall,compwidth,wall]);
	}
}

shoulder();
//translate([80-8,-20,0])rotate([0,90,0])servo_u_holder();