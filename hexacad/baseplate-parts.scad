use <baseplate.scad>;

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

module baseplatefromparts(){
	baseplatethirdmiddle();
	translate([0,100,0])
	baseplatethirdmiddle();
	translate([0,200,0])
	baseplatethirdmiddle();
}

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

baseplatefromparts();
//baseplatethirdouter();
//baseplatethirdmiddle();

