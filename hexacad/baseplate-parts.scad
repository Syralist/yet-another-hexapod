use <baseplate.scad>;
use <RB-65PG.scad>;

module baseplatethird()
{
	difference()
	{
		intersection()
		{
			baseplate();
			translate([-200,0,-5])
				cube([250,100,20]);
		}
		translate([-50,0,0])
			cylinder(r=20,h=20,center=true);
		translate([-130,0,0])
			cylinder(r=20,h=20,center=true);
		translate([-50,100,0])
			cylinder(r=20,h=20,center=true);
		translate([-130,100,0])
			cylinder(r=20,h=20,center=true);
	}

}

//module baseplatefromparts(){
//	translate([-90,50,0])
//	rotate([0,0,180])
//	translate([90,-50,0])
//	baseplatethirdouter();
//	translate([0,100,0])
//	baseplatethirdmiddle();
//	translate([0,200,0])
//	baseplatethirdouter();
//}

module baseplatethirdmiddle()
{
	difference()
	{
		baseplatethird();
		translate([-25,5,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-80,5,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-100,5,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-155,5,0])
			cylinder(r=2.5,h=20,center=true);
		
		translate([-25,95,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-80,95,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-100,95,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-155,95,0])
			cylinder(r=2.5,h=20,center=true);
	}

}

module baseplatethirdouter()
{
	difference()
	{
		baseplatethird();
		translate([-25,5,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-80,5,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-100,5,0])
			cylinder(r=2.5,h=20,center=true);
		translate([-155,5,0])
			cylinder(r=2.5,h=20,center=true);
	}
}

module compartment(complength)
{
	compheight = 26.5;
	
	wallwidth = 5;
	wallwidth2 = 7;
	
	ypos1 = 0;
	translate([0,ypos1,0])
		cube([complength,wallwidth,compheight]);
	ypos2 = ypos1+20+wallwidth;
	translate([0,ypos2,0])
		cube([complength,wallwidth,compheight]);
	translate([0,ypos1,0])
		cube([wallwidth2,20+2*wallwidth,compheight]);
}

module baseplatethirdbottom()
{
	complength = 48;
	ypos1 = 100/2-10-5;
	plateheight = 5;
	union()
	{
		translate([-complength+10,ypos1,plateheight])
			compartment(complength);
		translate([-190+complength,ypos1+20+10,plateheight])
			rotate([0,0,180])
				compartment(complength);
		baseplatethirdmiddle();
	}
}

module baseplatefromparts(){
	baseplatethirdmiddle();
	translate([0,100,0])
		baseplatethirdmiddle();
	translate([0,200,0])
		baseplatethirdmiddle();
}

module baseplatefrompartsbottom(){
	baseplatethirdbottom();
	translate([0,100,0])
		baseplatethirdbottom();
	translate([0,200,0])
		baseplatethirdbottom();
}

//baseplatefromparts();
//baseplatethirdouter();
//baseplatethirdmiddle();
translate([-30,60,5])rotate([0,0,-90])rb65pg();
baseplatethirdbottom();

