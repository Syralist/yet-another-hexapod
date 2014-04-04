use <small-parts.scad>
use <femur.scad>

module coxa()
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
			translate([length,0,0])
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

module femurconture()
{
	wall = 5;
	difference()
	{
		femurbase();
		difference()
		{
			femurbase();
			translate([-15,20,-2])
				cylinder(r=20.5,h=wall+4);
			translate([-60,20,-2])
				rotate([0,0,-3.5])
					cube([70,120,wall+4]);
		}
		difference()
		{
			femurbase();
			translate([-15,99,-2])
				cylinder(r=20.5,h=wall+4);
			translate([-40,-20,-2])
				rotate([0,0,3.5])
					cube([70,120,wall+4]);
		}
	}
}

module femur()
{
	wall = 5;
	radiusaxle = 8.7/2;
	radiuswheel = 20.7/2;
	heightwheel = 2.5;
	difference()
	{
		femurconture();
		translate([-16,radiuswheel+5,0])
			cylinder(r=radiusaxle,h=wall);
		translate([-16,radiuswheel+5,heightwheel])
			cylinder(r=radiuswheel,h=wall);
		translate([-16,120-radiuswheel-5,0])
			cylinder(r=radiusaxle,h=wall);
		translate([-16,120-radiuswheel-5,heightwheel])
			cylinder(r=radiuswheel,h=wall);
	}
}


//coxa();
//translate([80-8,-20,0])rotate([0,90,0])servo_u_holder();
projection(cut=true)
femur();

