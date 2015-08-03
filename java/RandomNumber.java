import java.util.*;
public class RandomNumber {
public static void main(String[] args)
{
	Random random = new Random();
	int a = random.nextInt(3)+1;
	int b = 3;
	while(b>0)
	{
		System.out.println(b);
		b--;
		int c=2;
		 while (c>0)
		{
			System.out.println("hi!");
			c--;
		}
	}
	System.out.println("End!" +a);
 }
//Scanner keyboard = new Scanner(System.in);
//keyboard.nextLine();
}
