import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class times_table extends PApplet {

int R = 250;

public void setup()
{
  
  background(255);
  strokeWeight(1);
}

public PVector place_point(float angle)
{
  angle = radians(angle);
  //circle(R*sin(angle), R*cos(angle), 10);
  return(new PVector(R*sin(angle), R*cos(angle)));
}

public void times_table(float times, int n)
{
  translate(300, 300);
  circle(0, 0, R*2);
  PVector[] points = new PVector[n];
  for (int i=0; i<n; i++)
  {
    points[i] = place_point(360*(i)/n);
  }

  for (int i=0; i<n; i++)
  {
    int t = Math.round(i*times);
    if(t>=n) {
        t = t - PApplet.parseInt(t/n) * n;
    }
    stroke(0xfffed8b1);
    line(points[i].x, points[i].y, points[t].x, points[t].y);
  }
}

float times = 1.0f;
float speed = 0.02f;

public void keyPressed(){
  speed = 2;
}

public void keyReleased(){
  speed = 0.02f;
}

public void draw()
{
  times += speed;
  times_table(times, 300);
}
  public void settings() {  size(600, 600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "times_table" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
