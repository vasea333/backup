import java.util.Scanner;
public class pizzeriaNapolitana {
	public static void main(String[] args)
	{
		double pizzaPrice=15.00;
		double saladPrice=8.00;
		double spritePrice=1.09;
		int pizzaAmount;
		int saladAmount;
		int spriteAmount;
		double taxRate=1.15;
		double endPrice;
		welcom();
		prices(pizzaPrice, saladPrice, spritePrice);
		pizzaAmount=pizzaNumber();
		saladAmount=saladNumber();
		spriteAmount=spriteNumber();
		endPrice=calculateTotal(pizzaAmount, saladAmount, spriteAmount, pizzaPrice, saladPrice, spritePrice, taxRate);
		System.out.println("Your total bill comes to: $"+endPrice);
	}
    static void prices(double a, double b,double c) {
		System.out.println("Pizza $"+a);
		System.out.println("Salad $"+b);
		System.out.println("Sprite $"+c);
	}
	static void welcom()
     {
    	 System.out.println("Welcome to the Pizzeria Napolitana!");
     }
	static int pizzaNumber()
	{
		Scanner in = new Scanner(System.in);
		System.out.println("How many Pizzas would you like?" );
		int p;
		p = in.nextInt();
		in.close();
		return p;
		
	}
	static int saladNumber()
	{
		Scanner in = new Scanner(System.in);
		System.out.println("How many Salads would you like?" );
		int s;
		s = in.nextInt();
		in.close();
		return s;
	}
	static int spriteNumber()
	{
		Scanner in = new Scanner(System.in);
		System.out.println("How many cups of Sprite would you like?" );
		int sp;
		sp = in.nextInt();
		in.close();
		return sp;
	}
	static  double calculateTotal(int a, int b, int c, double d, double e, double f, double g)
	{
		double h;
		h=(g*((a*d)+(b*e)+(c*f)));
		return h;
	}
	
}
