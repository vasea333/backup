import java.util.Scanner;
public class javaTutorial3 
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int height;
		int age;
		System.out.println("How toll are you in inches?");
		height=in.nextInt();
		System.out.println("What in your age i years?");
		age=in.nextInt();
		if ((height >= 52)&&(age >= 9))
			System.out.println("You can ride!");
		else
			System.out.println("You can't ride!");
		in.close();
	}
}
