int R = 250;

void setup()
{
  size(600, 600);
  background(255);
  strokeWeight(1);
}

PVector place_point(float angle)
{
  angle = radians(angle);
  //circle(R*sin(angle), R*cos(angle), 10);
  return(new PVector(R*sin(angle), R*cos(angle)));
}

void times_table(float times, int n)
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
        t = t - int(t/n) * n;
    }
    stroke(#fed8b1);
    line(points[i].x, points[i].y, points[t].x, points[t].y);
  }
}

float times = 1.0;
float speed = 0.02;

void keyPressed(){
  speed = 2;
}

void keyReleased(){
  speed = 0.02;
}

void draw()
{
  times += speed;
  times_table(times, 400);
}
