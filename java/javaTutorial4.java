import java.util.Scanner;
public class javaTutorial4 {
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		double a;
		double b;
		System.out.println("This program compares two numbers and tells you what the differents between the numbers is.");
		System.out.println("Please enter the first number you want to compare:");
		a=in.nextDouble();
		System.out.println("Please enter the second number you want to compare:");
		b=in.nextDouble();
		if(a == b)
			System.out.println("Your number are equal.");
			else if (a > b)
				System.out.println("Your first number is larger than your second number by " +(a-b));
					else
						System.out.println("Your second nmber is larger than your first number by " +(b-a));
		in.close();
	}

}
